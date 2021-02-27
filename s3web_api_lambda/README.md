<h1>S3で静的コンテンツ作ってAPI Gatewayを呼び出すチュートリアル</h1>

# S3準備

## バケット作成

```
aws s3 mb s3://（任意のバケット名）
```

## チュートリアルのS3をコピー

```
git clone https://github.com/abenben/python_aws_sample.git
cd s3
aws s3 cp ./ s3://（任意のバケット名） --recursive
```

## S3バケットの設定

* 「アクセス許可」設定
 * 「ブロックパブリックアクセス」はとりあえず全てブロックしない
 * [バケットポリシー]を編集する

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadForGetBucketObjects",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::abenben-test-web1/*"
        }
    ]
}
```

* 「プロパティ」の「静的ウェブサイトホスティング」
 * 「静的ウェブサイトホスティング」を有効にする
 * 「ホスティングタイプ」の「静的ウェブサイトをホストする」を選択
 * 「インデックスドキュメント」を"index.html"に設定

# Lambda準備

## Lambda関数を作成する
 
チュートリアルのapp.pyの内容をコピペする。

## API Gatewayの作成

## 動作確認

