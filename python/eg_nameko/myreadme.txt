1) Start rabbitmq docker instance
    portforward settings to localhost
    15672 for http admin page
    5672 for amqp
    25672 for clustering

2) Start service

Either  :
    nameko run HelloWorld --broker amqp://127.0.0.1:5672
or
    nameko run HelloWorld --config nameko.yml


3) To test using Nameko shell

  $> nameko shell --config nameko.yml
    In [4]: n.rpc.helloworld.hello('calvin soh')
    Out[4]: 'Hello, calvin soh!'

