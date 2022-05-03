import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.107", 1234))

while True:
	print("in")
	msg = s.recv(1024)
	print(msg.decode("utf-8"))