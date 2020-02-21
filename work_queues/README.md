# Intro
- Work queues allow you to distribute time-consuming tasks among multiple workers.
- Avoid doing a resource-intensive task immediately and having to wait for it to cpmplete, so instead it scheduled to be done later.
- If many workers are running in the background, the tasks are shared between them.

This bit uses the time,sleep function to simulate a heavy task. The number of dots dtermine the time.


# Round-Robin Distribution

By default, for each message Rabbit sends to the next consumer in sequence.
 ## Steps

 1. Start 2 Terminals
 2. In terminal 1 & 2 start worker
 ```bash
  $ python -m work_queues.worker
 ```
 2. In the third initiate tasks one afte the other and notice how they get distributed amongst the 2 workers
    ```bash
    $ python-m work_queues.new_task
    ```

# Message Acknowledgment
-  Allows for worker to acknowledge once task is done, that way if it dies without finishing the task, the task can be reallocated to other workers

To test this out, use similar steps as for Round-Robin above. but instead use the `worker_ack.py` worker.
```bash
  $ python -m work_queues.worker_ack
```
After sending a couple of messages. Close on of the workers and then run the following on MAC to see any unacknowledged messages:
```bash
  $ sudo rabbitmqctl list_queues name messages_ready messages_unacknowledged
```

# Message Durability

What happens when RabbitMQ server quits? It will forgwt the queues and messages unless explicitly told not to.
You can do this by adding the keyword argument `durable=True`, to queue declaration.

A new queue is declared in  `durable_task.py` and `durable_worker.py` that is made durable

To ensure the message is durable, we supply a `delivery_mode` property with value `2` to the publisher.

Testing steps don't change

# Fair Dispatch

To avoid overwhelming thea worker, we can set `prefetch_count=1`. This will tell RabbitMQ not to give more than one message to the worker at a time.

The, A new producer and consumer putting all these ideas together has been shown in the `final` folder.

Run Worker: ```bash $ python -m worker_queues.final.worker```
Run Producer: ```bash $ python -m worker_queues.final.task ```