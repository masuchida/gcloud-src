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

    incidentFlag = pubsub_message['incident']['state']
    message = pubsub_message['incident']
    datetime = _datetime.datetime.fromtimestamp(message['started_at'])

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
            message['summary'],
            message['resource_display_name'],
            message['url']
        )

    print(mes)
