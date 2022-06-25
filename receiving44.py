import socket               

sock = socket.socket()

host = "192.168.43.44" #ESP32 IP in local network
port = 80             #ESP32 Server Port    

sock.connect((host, port))


      

while True:
	data = sock.recv(4096)
	print(data)

sock.close()

