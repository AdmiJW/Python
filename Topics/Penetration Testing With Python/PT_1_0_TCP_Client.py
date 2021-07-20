import socket

# Create client socket
client_socket = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM
)

# Connect the socket with loopback address and port number
client_socket.connect( ('127.0.0.1', 444) )

# Obtain input to send to server
name = input("Please Enter your name: ")
client_socket.send( bytes(name, 'utf-8') )

# Retrieve the server response. Maximum buffer size is 1024 bytes. Since response is in binary format, decode it
response = client_socket.recv(1024).decode('utf-8')
print(response)

# Close connection
client_socket.close()