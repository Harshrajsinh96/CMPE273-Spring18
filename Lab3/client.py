import zmq
from threading import Thread
import sys


#Creating ZMQ context
context = zmq.Context()

#Defining the socket
send = context.socket(zmq.PUSH)
send.connect("tcp://127.0.0.1:5678")

client_user = sys.argv[1]
print("User [" + client_user +"] Connected to the chat server.")

def fun():
	run = Thread(target=sub)
	run.start()

def sub():
	sub = context.socket(zmq.SUB)
	sub.connect("tcp://127.0.0.1:5613")
	sub.setsockopt_string(zmq.SUBSCRIBE, '') 

	while True:
		msg = sub.recv().decode()
		if(msg and "[{}]: ".format(client_user) not in msg):
			print ("\n{}".format(msg)+"\n[{}] :".format(client_user), end="")
        
fun()
while True:
    new_input = input("[{}] :".format(client_user))
    new_input = "[" + client_user +"] :" + new_input + " "
    send.send_string(new_input)