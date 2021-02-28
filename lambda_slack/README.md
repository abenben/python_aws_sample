<h1>Lambdaでbotを作るチュートリアル</h1>

# ここで使うAWSサービス

* Lambda
* API Gateway
* Dynamo DB
* CloudWatch
* IAM
* その他の外部サービス（Slack）

# 作成開始

説明書こうと思いましたが、以下のサイトが完璧なので、これをみんなで見ながら補足したいと思います。
 https://nmmmk.hatenablog.com/entry/2018/10/10/001548

## 1.Lambda関数作成

### 疎通版を作成してテスト

function.py

``` python
def lambda_handler(event, context):
    
    # SlackのEvent APIの認証
    if "challenge" in event:
        return event["challenge"]
    
    return "OK"   
```

### Lambdaでテスト

## 2.API Gateway作成

prodにデプロイ
API Gatewayでテスト

API GatewayはSwagger設定にも対応している。

## 3.curlで疎通通信

curlからテスト

```
curl -X POST -H "Content-Type: application/json" -d '{"nesseage":"100"}'  https://ps2wuqv8dg.execute-api.ap-northeast-1.amazonaws.com/prod/SlackTestAbe
```

## 4.CloudWatchでログを確認する

API GatewayにIAM権限設定
API Gatewayでログの有効化

## 5.SlackのBOT作成

API GatewayのURL疎通確認

## 6.Lambdaコード修正

コードの修正
LambdaからDynamoDBへのアクセス権限付与

## 7.DynamoDB準備

DynamoDBにサンプル格納

```
import boto3

def create_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName='sample01',
        KeySchema=[
            {
                'AttributeName': 'ID',
                'KeyType': 'HASH'  # Partition key
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'ID',
                'AttributeType': 'N'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


def input_table():
    dynamodb = boto3.resource('dynamodb')
    sample = dynamodb.Table('sample01')

    data = {"ID": 1, "Message": "おはよう", "Price": 1000}
    sample.put_item(Item=data)
    data = {"ID": 2, "Message": "こんにちは", "Price": 2000}
    sample.put_item(Item=data)
    data = {"ID": 3, "Message": "こんばんは", "Price": 5000}
    sample.put_item(Item=data)
    return sample


if __name__ == '__main__':
    #create_movie_table()
    input_table()
```

## 8.Slackアプリをチャンネルに登録

## 9.Slackから動作確認

## 10.slackbot パッケージインストール

（続く）
* パッケージの追加

```
pip3 install slackbot
```

* 汎用パッケージのLayerの追加

``` shell
chmod 755 bootstrap
zip awscli.zip bootstrap
aws --profile igs-star lambda publish-layer-version --layer-name awscli-sh --zip-file fileb://awscli.zip
ZIP_FILE="lambda_deploy.zip"
zip -r $ZIP_FILE index.js star-seminar-access-check.sh
aws --profile igs-star lambda create-function \
    --function-name star-pre-prod-operation-check-seminar-access \
    --runtime nodejs12.x \
    --role arn:aws:iam::XXXXXXXX:role/YYYYYYYYYY \
    --handler index.handler \
    --zip-file fileb://$ZIP_FILE \
    --region ap-northeast-1
```

# 参考にしたサイト

「AWS(API Gateway + Lambda(Python)) + Slack APIを使ったBot作成」
https://nmmmk.hatenablog.com/entry/2018/10/10/001548

# 番外編

## Pycharm AWS ToolkitでAPI Gateway&Lambdaテスト・デプロイ

localのDockerでテストしてからデプロイできる
AWSのプロファイル切り替えに対応
S3バケット経由でデプロイ（CDK）

# 番外編（その2）

AWS Chatbotをいうサービス自体があります（Slackと連携可能）。
今回はLambdaやAPI Gatewatを理解するのが目的なのでこちらは使いません。
