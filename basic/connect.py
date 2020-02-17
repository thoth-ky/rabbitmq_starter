import pika

def get_rabbitmq_connection(host='localhost'):
  connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
  channel = connection.channel()

  return connection, channel