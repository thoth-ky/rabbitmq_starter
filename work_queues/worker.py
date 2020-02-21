from utils.connect import get_rabbitmq_connection
from utils.utils import callback_no_ack as callback

connection, channel = get_rabbitmq_connection()

QUEUE_NAME='WORKER_QUEUE'

# ensure queue exists
channel.queue_declare(queue=QUEUE_NAME)

channel.basic_consume(
  queue=QUEUE_NAME,
  auto_ack=True,
  on_message_callback=callback
)


print(' [X] Waiting for messages. To exit press CTRL + C')

channel.start_consuming()