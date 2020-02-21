import time
from utils.connect import get_rabbitmq_connection



connection, channel = get_rabbitmq_connection()

QUEUE_NAME='WORKER_QUEUE'

# ensure queue exists
channel.queue_declare(queue=QUEUE_NAME)

def callback(ch, method, properties, body):
  print(f'[X] received {body}')
  time.sleep(body.count(b'.'))
  print(' [X] Done')
  ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(
  queue=QUEUE_NAME,
  # auto_ack=True, --> This tunrs on Manual Message Acknowledgements
  on_message_callback=callback
)

print(' [X] Waiting for messages. To exit press CTRL + C')

channel.start_consuming()