from socket import *

HOST='' #Empty, than the curl host will be the server

PORT=8000 	#You can use any port you want, but client and
			#server need to use the same

s = socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
ip=gethostname()

s.bind((HOST,PORT))
s.listen(1) # How many connections it can receive at one time
conn, addr = s.accept()
print("CONNECTED TO: ", addr," at IP: ", ip)  # tell us the address of the connected person

i = True
while (i is True):
	data = conn.recv(1024)
	data=data.decode()
	print("=============> CLIENT:  ", repr(data),"\n") #data = user's message
	reply=input("Reply:\n")
	reply=reply.encode()
	conn.sendall(reply) #sendall => send to all nodes connected | send => one specific node
conn.close()
