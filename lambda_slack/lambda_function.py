import os
import logging
import json
import urllib.request
import boto3
from boto3.dynamodb.conditions import Key
import random

# ログ設定
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    
    logging.info(json.dumps(event))

    if "challenge" in event:
        return event["challenge"]

    if not is_verify_token(event):
        return "ERR1"    

    if not is_app_mention(event):
        return "ERR2"    
        
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('sample01')
    
    select = random.randint(1, 3)

    response = table.query(
        KeyConditionExpression=Key('ID').eq(str(select))
    )

    print(response)

    for result in response['Items']:
        post_message_to_channel(event.get("event").get("channel"), result['Message'])

    return 'OK'


def post_message_to_channel(channel, message):
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": "Bearer {0}".format(os.environ["SLACK_BOT_USER_ACCESS_TOKEN"])
    }
    data = {
        "token": os.environ["SLACK_BOT_VERIFY_TOKEN"],
        "channel": channel,
        "text": message,
    }

    req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), method="POST", headers=headers)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        logging.debug(the_page)

def is_verify_token(event):

    token = event.get("token")
    if token != os.environ["SLACK_BOT_VERIFY_TOKEN"]:
        return False

    return True

def is_app_mention(event):
    return event.get("event").get("type") == "app_mention"
    
