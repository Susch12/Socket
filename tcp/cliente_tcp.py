import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.98.137', 8081)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    print('Escribe el mensaje: ')
    message = input('').encode()
    print('sending {!r}'.format(message.decode('utf-8')))
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data.decode('utf-8')))

finally:
    print('closing socket')
    sock.close()
