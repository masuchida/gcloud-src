import base64
import json

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = json.loads(base64.b64decode(event['data']).decode('utf-8'))

    message = pubsub_message
    mes = """
    Title: %s
    発生時刻: %s
    発生した事項: %s
    リソース名: %s
    詳細: %s
    """ % (
        '死活監視　通知',
        message['receiveTimestamp'],
        message['jsonPayload']['event_subtype'],
        message['jsonPayload']['resource']['name'],
        message['logName']
    )

    json.dumps(mes)
