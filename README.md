# Serverless URL Shortener (AWS)

A URL shortener built using AWS serverless architecture (like Bitly).

##  Features
- Convert long URLs into short links
- Redirect users using short URL
- Fully serverless (no servers required)

##  Tech Stack
- AWS Lambda
- API Gateway
- DynamoDB
- IAM

## Architecture
User → API Gateway → Lambda → DynamoDB

## API Endpoints

### POST /shorten
Request:
{
  "url": "https://google.com"
}

Response:
{
  "short_url": "https://your-api/dev/abc123"
}

### GET /{shortId}
Redirects to original URL

## Learnings
- Serverless architecture
- API design
- AWS IAM permissions
- Debugging using CloudWatch

## 📸 Screenshots
(Add screenshots here)

##  Author
Rohit Patil
