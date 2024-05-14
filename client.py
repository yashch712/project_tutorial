import socket
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
localhost='172.21.26.112'
port=80

s.connect((localhost,port))
print("new client created")

while True:
    client_message = input("Me")
    s.send(client_message.encode())

    msg_received = s.recv(1024)
    msg_received = msg_received.decode()
    print('Server:',msg_received)

    if msg_received == 'exit':
        break;

s.close()
