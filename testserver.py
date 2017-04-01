import socket
from plate import Plate
import json

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 45813              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(2048)

            # print(data)
            if not data:
                break
            try:
                unicode_text = data.decode('utf-8')
                # print(unicode_text)
                result = json.loads(unicode_text)

                plate = result['results'][0]['plate']
                entrance_time = result['epoch_time']  # convert time?
                confidence = result['results'][0]['confidence']
                location = result['site_id']
                candidates = result['results'][0]['candidates']
                processing_time = result['processing_time_ms']
                plate_processing = result['results'][0]['processing_time_ms']

                myplate = Plate(plate, entrance_time, confidence, location,
                                candidates, processing_time, plate_processing)
                myplate.debug_print()
                try:
                    myplate.write_to_db()
                except Exception as e:
                    print("failed to write to db, ", e)
                conn.sendall(b"recieved plate")
            except Exception as e:
                print("Exception: ", e)
                conn.sendall(b"error")
