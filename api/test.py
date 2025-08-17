import json

def handler(request, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'message': 'Test API is working!',
            'status': 'success',
            'timestamp': '2024-01-01'
        })
    }
