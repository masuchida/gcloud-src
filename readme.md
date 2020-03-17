# 目的

顧客へのサービス提供のため

# 手段

サーバー死活監視

## 手法

GCEインスタンスを生成し、Stackdriver-Monitoringにて監視を行う。

Loggingに吐き出されたログを見に行って、`"compute.instances.stop" or "compute.instaces.start"`があったとき

LoggingからPub/Subにエクスポートする。

CloudfunctionsにてPub/Subを随時確認しており、Pub/Sub内にログがあった場合に

Cloudfunctionsはそれを受け取り、Chatworkへ通知を飛ばす。

今週中に全部終わらす！！

今日中にChatworkに飛ぶ機構は作りたい！！