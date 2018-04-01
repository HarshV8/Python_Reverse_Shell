import socket

HOST = '0.0.0.0'
PORT = 5559
print("[+] Command & Control Server Running ")
HOST = str(input("[+] Enter Destination IP : "))
PORT = int(input("[+] Enter Port : "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while 1:
    sending_data = input("")
    sending_bytes = sending_data.encode()
    s.send(sending_bytes)
    data = s.recv(1024)
    data_recieved = data.decode()
    if(data_recieved!=""):
        print(str(data_recieved))
s.close()
