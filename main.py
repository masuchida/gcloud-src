import base64
import json
import _datetime

TOKEN = ('CW_TOKEN')
ROOMID = ('CW_ROOMID')
URL = 'https://api.chatwork.com/v2/'

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = json.loads(base64.b64decode(event['data']).decode('utf-8'))

    message = pubsub_message['incident']
    incidentFlag = message['state']
    datetime = _datetime.datetime.fromtimestamp(message['started_at'])
    summary = message['summary']

    if summary == 'An uptime check on gcp-test-271312 gcp-test is failing.':
        summary = 'サーバーダウンを検知しました。'
    elif summary == 'The uptime check for gcp-test-271312 gcp-test has returned to a normal state.':
        summary = 'サーバー回復を確認しました。'

    if incidentFlag == 'open':
        title = '障害発生'
    elif incidentFlag == 'closed':
        title = '回復'

    mes = """
        Title: % s
        発生時刻: % s
        発生した事項: % s
        リソース名: % s
        URL: % s
        """ % (
            title,
            datetime,
            summary,
            message['resource_display_name'],
            message['url']
        )

    print(mes)
