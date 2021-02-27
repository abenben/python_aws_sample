import json
import logging

# ログ設定
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):

    logging.info(json.dumps(event))
    
    edited_message=""
    if 'param1' in event:

        message = event['param1']
        edited_message = 'input - ' + message + ' OK}'
    else:
        edited_message = 'PARAM ERROR'
    

    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        },
        'body': json.dumps(edited_message)
    }
