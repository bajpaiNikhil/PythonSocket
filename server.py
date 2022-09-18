import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
# print(SERVER, socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(connection, address):
    print(f"[New Connection] {address} connected .")
    connected = True
    while connected:
        msg = connection.recv(2048).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(f"[connected] , {msg}")
        connection.send(f"[Received]".encode(FORMAT))
        # msg_length = connection.recv(HEADER).decode(FORMAT)
        # if msg_length:
        #     msg_length = int(msg_length)
        #     msg = connection.recv(msg_length).decode(FORMAT)
        #     if msg == DISCONNECT_MESSAGE:
        #         connected = False
        #     print(f"[{address}] {msg}")
    connection.close()


def start():
    server.listen()
    print(f"[LISTENING] SERVER is listening on {SERVER}")
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"[Active Connections] {threading.active_count() - 1}")


print("{Starting} server is starting ....")
start()
