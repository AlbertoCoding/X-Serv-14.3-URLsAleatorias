#!/usr/bin/python3
"""
Simple HTTP Server version 3: included link that responds with random URLs.

Alberto Rafael Rodriguez Iglesias
SAT (Universidad Rey Juan Carlos)
"""

import socket
import random

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind((socket.gethostname(), 1234))
#mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests
mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)

try:
	while True:
		randnum = random.randint(1,1000000000)

		print('Waiting for connections')
		(recvSocket, address) = mySocket.accept()
		print('Request received:')
		print(recvSocket.recv(1024))
		print('Answering back...')

		recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                        b"<html><body><h1>Hola." +
						b"<a href='http://" +
						socket.gethostname() +
						b":1234/" +
						bytes(str(randnum).encode("utf-8")) +
						b"'> Dame otra''</a>" +
                        b"</h1></body></html>" +
                        b"\r\n")
		recvSocket.close()
except KeyboardInterrupt:
	print("Closing binded socket")
	mySocket.close()
