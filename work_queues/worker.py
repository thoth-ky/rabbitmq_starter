import time
from utils.connect import get_rabbitmq_connection



connection, channel = get_rabbitmq_connection()

QUEUE_NAME='WORKER_QUEUE'

# ensure queue exists
channel.queue_declare(queue=QUEUE_NAME)

def callback(ch, methos, properties, body):
  print(f'[X] received {body}')
  time.sleep(body.count(b'.'))
  print(' [X] Done')

channel.basic_consume(
  queue=QUEUE_NAME,
  auto_ack=True,
  on_message_callback=callback
)


print(' [X] Waiting for messages. To exit press CTRL + C')

channel.start_consuming()