from connect import get_rabbitmq_connection

connection, channel = get_rabbitmq_connection()
QUEUE_NAME='hello'

# must create a queue first
channel.queue_declare(queue=QUEUE_NAME)

for i in range(50):
  channel.basic_publish(
    exchange='', # use default exachebe
    routing_key=QUEUE_NAME, # queue name
    body=f'We are at index{i}' # message here
  )

connection.close()