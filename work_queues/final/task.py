import sys
import pika
from utils.connect import get_rabbitmq_connection

connection, channel = get_rabbitmq_connection()
DURABLE_QUEUE_NAME='TASK_QUEUE'

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.queue_declare(queue=DURABLE_QUEUE_NAME, durable=True)

channel.basic_publish(
  exchange='', 
  routing_key=DURABLE_QUEUE_NAME,
  body=f'Durable {message}',
  properties=pika.BasicProperties(
    delivery_mode=2,
  )
)

print(f" [X] Sent {message}")
connection.close()