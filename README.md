AWS Sentiment Analysis API 

This is a serverless sentiment analysis API built using:
- AWS Lambda(Backend processing)
- AWS API Gateway (Public API endpoint)
- AWS Comprehend (Sentiment analysis)

 How It Works
1. Users send a POST request with text input to the API Gateway URL.
2. AWS Lambda extracts the text and sends it to AWS Comprehend.
3. Comprehend analyzes the sentiment and returns a classification.
4. Lambda returns a JSON response with the sentiment results.

Example Request:

You can test the API using curl:

curl -X POST "https://30wpw0kkxf.execute-api.us-east-1.amazonaws.com/prod/analyze" \
     -H "Content-Type: application/json" \
     -d {"text": "I love AWS!"}

     
Example Response:

{
  "sentiment": "POSITIVE",
  "sentiment_score": {
    "Positive": 0.99,
    "Negative": 0.01,
    "Neutral": 0.00,
    "Mixed": 0.00
  }
}
