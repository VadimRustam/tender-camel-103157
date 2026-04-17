import socket  # noqa: F401
import threading


def handle_connection(conn: socket.socket):
    while True:
        BUFFER_SIZE = 2048
        chunk = conn.recv(BUFFER_SIZE)
        msg = chunk.decode("utf-8")
        if chunk != b"":
            conn.sendall(b"+PONG\r\n")


def main():
    with socket.create_server(("localhost", 6379), reuse_port=True) as server:
        while True:
            sock_connection, _ = server.accept()  # wait for client
            threading.Thread(target=handle_connection, args=(sock_connection,)).start()


if __name__ == "__main__":
    main()