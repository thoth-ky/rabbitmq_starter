from utils.connect import get_rabbitmq_connection
from utils.utils import pseudo_heavy_task_callback as callback

connection, channel = get_rabbitmq_connection()

DURABLE_QUEUE_NAME='TASK_QUEUE'

# ensure queue exists
channel.queue_declare(queue=DURABLE_QUEUE_NAME, durable=True)

channel.basic_consume(
  queue=DURABLE_QUEUE_NAME,
  on_message_callback=callback
)

print(' [X] Waiting for messages. To exit press CTRL + C')

channel.start_consuming()