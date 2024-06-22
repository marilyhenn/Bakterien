import socket
import time

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
main_socket.bind(("localhost", 8080))
main_socket.setblocking(False)
main_socket.listen(5)
print("The server is working")
players = []
while True:
    try:
        new_socket, addr = main_socket.accept()
        print("Connected", addr)
        new_socket.setblocking(False)
        players.append(new_socket)
    except BlockingIOError:
        pass
    for i in players:
        try:
            data = i.recv(1024).decode()
            print("You got", data)
        except:
            pass
    time.sleep(1)
