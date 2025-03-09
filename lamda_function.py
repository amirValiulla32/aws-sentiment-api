import json
import boto3

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        text = body.get("text", "")

        if not text:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Text input is required"})
            }

        comprehend = boto3.client("comprehend")
        response = comprehend.detect_sentiment(Text=text, LanguageCode="en")

        sentiment = response["Sentiment"]
        sentiment_score = {k: round(v, 2) for k, v in response["SentimentScore"].items()}

        return {
            "statusCode": 200,
            "body": json.dumps({
                "sentiment": sentiment,
                "sentiment_score": sentiment_score
            }),
            "headers": {
                "Content-Type": "application/json"
            }
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
