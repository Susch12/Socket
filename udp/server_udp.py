import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.98.137', 8081)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)


while True:
    #print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    #print('received {} bytes from {}'.format(
    #len((data), address)
    #print(data.decode('utf-8'))

    if data:
        sent = sock.sendto(data, address)
        print('sent {} bytes back to {}'.format(
            sent, address))
