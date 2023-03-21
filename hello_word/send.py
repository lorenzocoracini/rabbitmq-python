import pika

# create connection to rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create the hello queue
channel.queue_declare(queue='hello')

# send hello word
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

# closing the connection
connection.close()
