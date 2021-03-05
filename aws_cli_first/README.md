<h1> AWS CLIの初期設定

---

# AWS CLIインストール

* CLI Version 1.0

```
$ sudo pip install awscli

or

$ brew install awscli
```

---

# アクセスキーなどの設定

```
$ aws configure --profile finpy-abe
AWS Access Key ID [None]: {アクセスキー(各自)}
AWS Secret Access Key [None]: {シークレットアクセスキー(各自)}
Default region name [None]: ap-northeast-1
Default output format [None]: json
```

---

# 確認

```
$ aws configure list
$ aws configure list --profile finpy
```

--

# デフォルト変更

```
$ export AWS_DEFAULT_PROFILE=finpy
```

---

# S3バケットを作成

AWSコンソールから適当なユニークなバケット名を作成する。

*面倒なのでコマンドでw
```
$ aws s3 mb s3://finpy-abenben-bucket
```

---

# S3バケットを確認

```
$ aws s3 ls
```

---

# S3バケットにファイルをアップロード

```
$ cd /tmp
$ echo "test" > sample.txt
$ aws s3 cp ./sample.txt s3://finpy-abenben-bucket
```

---

# S3バケットからファイルをダウンロード

```
$ cd /tmp
$ echo "test" > sample.txt
$ aws s3 cp s3://finpy-abenben-bucket/sample.txt ./sample.txt
$ cat ./sample.txt
$ #確認できたら削除
$ cd /tmp
$ rm ./sample.txt

```

---

# Pythonからもダウンロードしてみる

* ① boto3をインストール

```
pip3 install boto3
```

* ② boto3でS3からファイルをダウンロード

```
python
>>> import boto3
>>> s3 = boto3.resource('s3')
>>> bucket = s3.Bucket('finpy-abenben-bucket')
>>> bucket.download_file('sample.txt', '/tmp/sample.txt')
>>> exit()
```
