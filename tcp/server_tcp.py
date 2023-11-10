import socket
import threading

def worker(connection, client_address):
    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(30)
            if data:
                #print('received {!r}'.format(data.decod>
                connection.sendall(data)
            else:
                break

    finally:
        # Clean up the connection
        connection.close()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    # Wait for other connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    threading.Thread(target=worker, args=(connection, client_address)).start()

# Bind the socket to the port
server_address = ('192.168.100.134', 8081)
print('starting up on {} port {}'.format(*server_address>
sock.bind(server_address)
