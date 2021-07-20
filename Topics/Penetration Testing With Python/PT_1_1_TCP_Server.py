import socket


# Create a server socket. (Convention variable name is to use 's')
# Commonly used:
#   Family - IPv4 -> AF_INET
#            IPv6 -> AF_INET6
#   Type   - TCP  -> SOCK_STREAM
#            UDP  -> SOCK_DGRAM
server_socket = socket.socket(
    family=socket.AF_INET,          # IPv4
    type=socket.SOCK_STREAM         # TCP
)


# Bind the server socket to the hostname and port number
host = '127.0.0.1'                      # LAPTOP-R22GTED8 in my case
port = 444                              # Recall the available range is 0-65535
server_socket.bind( (host, port) )


# Setup a TCP listener. Parameter specify how many connections can it listen to at one time
# If the number of connections exceed at one time, the extra connections will be refused
server_socket.listen(3)


print('Socket established')



# Keep in loop so it will loop listening to the incoming connection and not finish after one connection
while True:
    # accept() is a blocking function, waiting for a connection to be established
    # Once an connection is established, returns tuple of client socket and address
    client_socket, client_address = server_socket.accept()

    # We assume the client will send name. Decode the name.
    name = client_socket.recv(1024).decode('utf-8')
    print(f'Established connection coming from {str(client_address)}\nName: {name}\n')

    # Send a response back to the client, and close the connection
    msg = bytes(f'Thank you for connecting to the server {client_address}\nName: {name}\n', 'utf-8')
    client_socket.send(msg)
    client_socket.close()
