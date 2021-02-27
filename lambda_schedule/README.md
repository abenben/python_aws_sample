<h1>Lambdaをスケジュール実行する</h1>

---

# 1.Lambda関数の準備

なんか適当に作る


```
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logging.info("START")
    print("Hello Worle!"）
    logging.info("END")

```


# 2.CloudWatch Eventsで設定

CloudWatchでルールを作成するだけ。
イメージ画像参照

<img src="/lambda_schedule/images/event_lambda.png" height="500">
