import time

def basic_callback(ch, methos, properties, body):
  print(f'[x] received {body}')

def callback_no_ack(ch, method, properties, body):
  print(f'[X] received {body}')
  time.sleep(body.count(b'.'))
  print(' [X] Done')


def pseudo_heavy_task_callback(ch, method, properties, body):
  print(f'[X] received {body}')
  time.sleep(body.count(b'.'))
  print(' [X] Done')
  ch.basic_ack(delivery_tag=method.delivery_tag)