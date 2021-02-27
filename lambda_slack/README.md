<h1>Lambdaでbotを作るチュートリアル</h1>

# ここで使うAWSサービス

* Lambda
* API Gateway
* Dynamo DB
* CloudWatch
* IAM
* その他の外部サービス（Slack）

# 作成開始

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

## 3.Curlで疎通通信

Curlからテスト

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

## 8.Slackアプリをチャンネルに登録

## 9.Slackから動作確認

## 10.Slackパッケージインストール

（続く）
* パッケージの追加
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
