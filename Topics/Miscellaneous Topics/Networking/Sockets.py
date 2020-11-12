#   ####################################### TCP, SOCKET, PORT NUMBERS ########################################
#
#   TCP (Transmission Control Protocol) is a protocol which is built on top of IP, which allows for retransmission of
#   data if any of it is lost. It is kind of a reliable pipe for data

#   A Socket is an end point of a bidirectional inter-process, like a socket we see in daily life. We don't care
#   how power are transmitted, we just know that power will come out of it

#   Port Numbers for TCP allows for multiple network application to exist on the same server. Different applications
#   on the same machine will use different port numbers, so when data arrived at TCP, it knows which data packet
#   belongs to which application. Here are common port numbers for specific services:
#       HTTP                                    - 80
#       HTTPS                                   - 443
#       DNS                                     - 53
#       SMTP (Simple mail Transfer Protocol)    - 25
#       FTP  (File transfer Protocol)           - 21
#   By default the browser will hide the port number which is using common port numbers like 443 or 80. If different
#   port number is used, it will display right after the domain name part! 'Like www.lasi-asia.org:8080/wp'
#
#   When using web browser, we often use Ephemeral port, which means 'short-lived' port. We get assigned a random
#   port number, visited the website's which uses 80 or 443 port number, and get the request back, and the port closes
#
#   ################################################################################################################

#   ####################################### PYTHON SOCKET MODULE ########################################
#
#   In Python we can use the socket module to make requests to the internet.
#

import socket

myIP = socket.gethostbyname( socket.gethostname() )
print(myIP)

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
#   Can take in a Tuple of (Host, Port)
mySocket.connect( ('data.pr4e.org', 80) )
#   Make up the HTTP GET command to send to the host. Make sure to encode it so no character other than ASCII
myCommand = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

print(myCommand)

mySocket.send(myCommand)

while True:
    data = mySocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
    
#   Remember to close the connection to prevent memory leaks
mySocket.close()
