import zmq

#Creating ZMQ context
context = zmq.Context()

#Defining the socket

#Pull Socket
pullSock = context.socket(zmq.PULL)
pullSock.bind("tcp://127.0.0.1:5678")

#Pub socket
pubSock = context.socket(zmq.PUB)
pubSock.bind("tcp://127.0.0.1:5613")

while True:
    msg = pullSock.recv()
    pubSock.send(msg)
    print("[Server-Window] " + msg.decode())