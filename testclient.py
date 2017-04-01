import socket
import json

HOST = '127.0.0.1'    # The remote host
PORT = 45813              # The same port as used by the server

result = ""

with open('example_output.json') as jsondata:
    result = json.load(jsondata)

    # jsondata.close()
data = json.dumps(result)


bytestring = data.encode('utf-8')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.sendall(b'Hello, world')
    s.sendall(bytestring)
    data = s.recv(1024)
print('Received', repr(data))
