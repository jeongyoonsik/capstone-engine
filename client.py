import beanstalkc
import json
import socket

HOST = ''  # IP of remote host
PORT = 45813  # arbirary port corresponding to server

# result = ""

try:
    beanstalk = beanstalkc.Connection(host="localhost", port=11300)
    beanstalk.watch("alprd")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    with open("/path/to/output/alpr_results.json", 'w') as outfile:
        while True:
            job = beanstalk.reserve()
            data = job.body
            print(data)
            json.dump(data, outfile)
            bytestring = data.encode('utf-8')
            s.sendall(bytestring)
            data = s.recv(1024)
            job.delete()
finally:
    s.close()
