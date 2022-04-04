import json

def lambda_handler(event, context):
    print(event)
    print(event['body'])
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": 'ok',
        }),
    }
