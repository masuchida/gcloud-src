import base64
import json
import _datetime
import requests
import os

TOKEN = os.environ.get('CW_TOKEN')
ROOMID = os.environ.get('CW_ROOMID')
URL = 'https://api.chatwork.com/v2/rooms'
POST = '{0}/{1}/messages'.format(URL, ROOMID)

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = json.loads(base64.b64decode(event['data']).decode('utf-8'))

    message = pubsub_message['incident']
    incident_flag = message['state']
    datetime = _datetime.datetime.fromtimestamp(message['started_at'])
    summary = message['summary']

    if summary == 'An uptime check on gcp-test-271312 gcp-test is failing.':
        summary = 'サーバーダウンを検知しました。'
    elif summary == 'The uptime check for gcp-test-271312 gcp-test has returned to a normal state.':
        summary = 'サーバー回復を確認しました。'

    if incident_flag == 'open':
        incident_flag = '障害発生'
    elif incident_flag == 'closed':
        incident_flag = '回復'

    mes = """
        検知: % s
        発生時刻: % s
        発生した事項: % s
        対象リソース名: % s
        エラー詳細URL: % s
        """ % (
            incident_flag,
            datetime,
            summary,
            message['resource_display_name'],
            message['url']
        )

    print(mes)

    data = mes.encode()

    headers = {
        'X-ChatWorkToken': TOKEN,
    }

    requests.post(POST, headers=headers, data=data)
