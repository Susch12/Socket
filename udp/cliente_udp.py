import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.98.137', 8081)
print('Escribe el mensaje: ')
message = input('').encode()

try:

    # Send data
    print('sending {!r}'.format(message.decode('utf-8')))
    sent = sock.sendto(message, server_address)

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data.decode('utf-8')))

finally:
    print('closing socket')
    sock.close()
