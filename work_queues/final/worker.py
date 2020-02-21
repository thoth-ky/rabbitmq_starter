import time
from utils.connect import get_rabbitmq_connection

connection, channel = get_rabbitmq_connection()

DURABLE_QUEUE_NAME='TASK_QUEUE'

# ensure queue exists
channel.queue_declare(queue=DURABLE_QUEUE_NAME, durable=True)

print(' [X] Waiting for messages. To exit press CTRL + C')

def callback(ch, method, properties, body):
  print(f'[X] received {body}')
  time.sleep(body.count(b'.'))
  print(' [X] Done')
  ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)

channel.basic_consume(
  queue=DURABLE_QUEUE_NAME,
  on_message_callback=callback
)



channel.start_consuming()