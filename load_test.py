import socket
import ssl
import threading
import time
import random
from datetime import datetime

HOST = "127.0.0.1"
PORT = 9000

# Demo-friendly configuration
NUM_CLIENTS = 5
LOG_INTERVAL = 1.5

messages = [
    "User login successful",
    "Database connection established",
    "Disk usage warning",
    "Cache refreshed",
    "Request processed",
    "API response sent",
    "Authentication failed",
    "File uploaded",
    "Query executed",
    "Connection timeout"
]

levels = ["INFO", "ERROR", "DEBUG", "WARNING"]


def simulate_client(client_id):
    try:
        # Create SSL context
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client = context.wrap_socket(raw_socket)

        client.connect((HOST, PORT))

        print(f"[CLIENT {client_id}] Connected")

        while True:
            timestamp = datetime.now()

            message = random.choice(messages)
            level = random.choice(levels)

            log = f"{timestamp} | CLIENT_{client_id} | {level} | {message}"

            start = time.time()

            client.send(log.encode())

            ack = client.recv(1024).decode()

            end = time.time()

            latency = end - start

            print(f"[CLIENT {client_id}] {ack} | latency={latency:.4f}s")

            time.sleep(LOG_INTERVAL)

    except Exception as e:
        print(f"[CLIENT {client_id} ERROR]", e)


def start_load_test():

    threads = []

    print(f"\nStarting demo with {NUM_CLIENTS} simulated clients...\n")

    for i in range(NUM_CLIENTS):
        thread = threading.Thread(target=simulate_client, args=(i,))
        thread.start()
        threads.append(thread)

        time.sleep(0.5)  # stagger client connections slightly


if __name__ == "__main__":
    start_load_test()