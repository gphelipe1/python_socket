from socket import *

HOST ='192.168.0.9'
PORT=8000

s=socket(AF_INET, SOCK_STREAM) #SOCK_DGRAM->UDP
s.connect((HOST,PORT))

while (True):
	msg=input("Send:\n")
	if (msg=="EXIT NOW"):
		break
		conn.close()
	s.send(msg.encode())
	print(". . .")
	reply=s.recv(1024)
	reply=reply.decode()
	print("==========> SERVER:",repr(reply))
s.close()