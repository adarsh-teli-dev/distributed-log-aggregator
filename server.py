import socket
import threading
import ssl
import time
import psutil

HOST = "0.0.0.0"
PORT = 9000
LOG_FILE = "server_logs.txt"

log_count = 0
start_time = time.time()


def handle_client(client_socket, addr):
    global log_count
    print(f"[NEW CONNECTION] {addr} connected.")

    try:
        while True:
            data = client_socket.recv(1024)

            if not data:
                print(f"[DISCONNECTED] {addr}")
                break

            log = data.decode()

            print(f"[LOG RECEIVED] {log}")

            try:
                with open(LOG_FILE, "a") as file:
                    file.write(log + "\n")
            except Exception as file_error:
                print("[FILE ERROR]", file_error)

            log_count += 1

            client_socket.send("ACK".encode())

    except Exception as e:
        print("[CLIENT ERROR]", e)

    finally:
        client_socket.close()


def monitor_performance():
    global log_count, start_time

    while True:
        time.sleep(1)

        print(f"[THROUGHPUT] {log_count} logs/sec")

        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent

        print(f"[SYSTEM] CPU: {cpu}% | Memory: {memory}%")

        log_count = 0
        start_time = time.time()


def start_server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server_cert.pem", keyfile="server_key.pem")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("[SECURE SERVER STARTED]")

    performance_thread = threading.Thread(target=monitor_performance, daemon=True)
    performance_thread.start()

    while True:
        client_socket, addr = server.accept()

        secure_socket = context.wrap_socket(client_socket, server_side=True)

        thread = threading.Thread(target=handle_client, args=(secure_socket, addr))
        thread.start()


if __name__ == "__main__":
    start_server()