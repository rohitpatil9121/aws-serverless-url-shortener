import json
import string
import random
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('URLTable')

def generate_short_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def lambda_handler(event, context):

    method = event.get('requestContext', {}).get('http', {}).get('method', '')

    if method == 'POST':
        body = json.loads(event.get('body', '{}'))
        long_url = body.get('url')

        short_id = generate_short_id()

        table.put_item(Item={
            'shortId': short_id,
            'longUrl': long_url
        })

        return {
            'statusCode': 200,
            'body': json.dumps({
                'short_url': f"https://u2jyqm8b7k.execute-api.us-east-1.amazonaws.com/dev/{short_id}"
            })
        }

    elif method == 'GET':
        short_id = event.get('pathParameters', {}).get('shortId')

        response = table.get_item(Key={'shortId': short_id})

        return {
            'statusCode': 302,
            'headers': {
                'Location': response['Item']['longUrl']
            }
        }
