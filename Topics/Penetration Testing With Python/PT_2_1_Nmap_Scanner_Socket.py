import socket
import PT_2_0_Utilities as inpututil

# Nmap is a free and open-source network scanner created by Gordon Lyon. Nmap is used to discover hosts and services
# on a computer network by sending packets and analyzing the responses
# Basically, provided IP address and port range to scan, Nmap will send packets to the port at given IP address
# and see if there is a service associated with the port or not, whether it is opened, filtered or closed.


##############################################################################################################
# Function which displays user menu and prompts IP address and scan option. Returns the responses in tuple of
# (ip_address, minPort, maxPort)
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
    print("                    Nmap Scanner (Sockets ver.)")
    print('===============================================================')
    ip = inpututil.read_ip_address()
    port_ranges = inpututil.read_port_range()

    return ip, port_ranges[0], port_ranges[1]


if __name__ == '__main__':
    ip_address, min_port, max_port = user_menu()

    print("\nRunning scan on the following IP and port: ",
          f"IP Address: {ip_address}",
          f"Port: [{min_port}-{max_port}]\n", sep='\n')

    for port in range(min_port, max_port+1):
        if port % 100 == 0:
            print("Scanning port starting from", port, "...")
        try:
            with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect( (ip_address, port) )

                print(f'Port {port} is open')
        except:
            pass


