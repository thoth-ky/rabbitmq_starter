try:
  from utils.connect import get_rabbitmq_connection
except ModuleNotFoundError:
  from ..utils.connect import get_rabbitmq_connection


connection, channel = get_rabbitmq_connection()

QUEUE_NAME='hello'

# ensure queue exists
channel.queue_declare(queue=QUEUE_NAME)

def callback(ch, methos, properties, body):
  print(f'[x] received {body}')

channel.basic_consume(
  queue=QUEUE_NAME,
  auto_ack=True,
  on_message_callback=callback
)


print(' [X] Waiting for messages. To exit press CTRL + C')

channel.start_consuming()