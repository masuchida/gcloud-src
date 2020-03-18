import base64
import json

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = json.loads(base64.b64decode(event['data']).decode('utf-8'))

    incidentFlag = pubsub_message['incident']['state']
    message = pubsub_message['incident']

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
            message['started_at'],
            message['summary'],
            message['resource_display_name'],
            message['url']
        )

    print(mes)
