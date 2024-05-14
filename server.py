import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
localhost='172.21.26.112'
port=80

server_socket.bind((localhost,port))
server_socket.listen(80)

print("server started")

client_socket,addr=server_socket.accept()

while True:
    msg_received=client_socket.recv(1024)
    msg_received=msg_received.decode()
    print("Client",msg_received)

    msg_send=input("Me")
    client_socket.send(msg_send.encode("ascii"))
    client_socket.close()   
    