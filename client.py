from socket import *

HOST ='' # Here you put the server IP. Eg: '192.168.0.2'  

PORT=8000	# You can use any port you want, but client and
			# server need to use the same

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