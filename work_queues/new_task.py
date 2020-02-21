import sys
from utils.connect import get_rabbitmq_connection

connection, channel = get_rabbitmq_connection()
QUEUE_NAME='WORKER_QUEUE'

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.queue_declare(queue=QUEUE_NAME)

channel.basic_publish(
  exchange='', 
  routing_key=QUEUE_NAME,
  body=message
)

print(f" [X] Sent {message}")
connection.close()