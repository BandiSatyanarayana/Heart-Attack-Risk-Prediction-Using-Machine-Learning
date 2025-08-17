import json

def handler(request, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'message': 'Heart Attack Risk Prediction API',
            'status': 'API is working!',
            'note': 'ML models will be added in next deployment'
        })
    }
