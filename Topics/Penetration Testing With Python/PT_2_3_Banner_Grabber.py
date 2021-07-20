import socket
import PT_2_0_Utilities as inpututil

# Once we know which ports are available on a machine, we can try to retrieve some information from it.
# A banner is usually a small piece of information which is associated with the response data from the server.
# It could be a welcome message, or information on the service itself. An example would be the header part
# in a HTTP response.
#
# This information may or may not be useful. If it reveals information on the version of database, hackers may choose
# to visit https://www.exploit-db.com/ and search for vulnerabilities on your machine to attack.



##############################################################################################################
# Function which displays user menu and prompts IP address and port range to retrieve banner
# Returns tuple of (ip_address, min_port, max_port)
def user_menu():
    print(r"  /$$$$$$        /$$               /$$    /$$$$$ /$$      /$$",
          r" /$$__  $$      | $$              |__/   |__  $$| $$  /$ | $$",
          r"| $$  \ $$  /$$$$$$$ /$$$$$$/$$$$  /$$      | $$| $$ /$$$| $$",
          r"| $$$$$$$$ /$$__  $$| $$_  $$_  $$| $$      | $$| $$/$$ $$ $$",
          r"| $$__  $$| $$  | $$| $$ \ $$ \ $$| $$ /$$  | $$| $$$$_  $$$$",
          r"| $$  | $$| $$  | $$| $$ | $$ | $$| $$| $$  | $$| $$$/ \  $$$",
          r"| $$  | $$|  $$$$$$$| $$ | $$ | $$| $$|  $$$$$$/| $$/   \  $$",
          r"|__/  |__/ \_______/|__/ |__/ |__/|__/ \______/ |__/     \__/", sep='\n')
    print('===============================================================')
    print("                         Banner Grabber")
    print('===============================================================')

    # Read IP address and port range
    ip = inpututil.read_ip_address()
    port_ranges = inpututil.read_port_range()

    return ip, port_ranges[0], port_ranges[1]


###############################################################################
# Main function
if __name__ == '__main__':
    ip_address, min_port, max_port = user_menu()

    for port in range(min_port, max_port+1):
        try:
            c = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

            # 1 second per port. If the port range is large, will take a long time
            c.settimeout(1)
            c.connect( (ip_address, port) )
            c.send(b'test\r\n')
            response = c.recv(1 * 1024 * 1024).decode('utf-8')
            c.close()

            if input(f'Response on port {port}. Enter "s" to show: ') == 's':
                print(response, end='\n\n')
        except:
            pass


