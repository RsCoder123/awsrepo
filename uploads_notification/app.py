import json
import boto3

sns = boto3.client('sns')
TOPIC_ARN = 'arn:aws:sns:us-east-1:911095257940:My-App-UploadsNotificationTopic'

def lambda_handler(event, context):
    for record in event['Records']:
        body = json.loads(record['body'])
        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="New Upload Notification",
            Message=json.dumps(body)
        )
    return {
        'statusCode': 200,
        'body': 'SNS notification sent'
    }
