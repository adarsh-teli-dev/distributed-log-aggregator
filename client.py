import socket
import ssl
import time
from datetime import datetime

HOST = "127.0.0.1"
PORT = 9000

client_id = "CLIENT_1"

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

secure_client = context.wrap_socket(raw_socket)

secure_client.connect((HOST, PORT))

print("[SECURE CONNECTION ESTABLISHED]")

while True:
    try:
        timestamp = datetime.now()

        log = f"{timestamp} | {client_id} | INFO | Secure log message"

        secure_client.send(log.encode())

        ack = secure_client.recv(1024).decode()

        print("[SERVER]", ack)

        time.sleep(2)

    except Exception as e:
        print("[CLIENT ERROR]", e)
        break

secure_client.close()