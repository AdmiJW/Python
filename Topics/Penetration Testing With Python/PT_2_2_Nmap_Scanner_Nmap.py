# Install package 'python-nmap' for this
import nmap
import PT_2_0_Utilities as inpututil


##############################################################################################################
# Function which displays user menu and prompts IP address and scan option. Returns the responses in tuple of
# (ip_address, min_port, max_port, scanType)
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
    print("               Nmap Scanner (Nmap Software ver.)")
    print('===============================================================')

    # Read IP address and port range
    ip = inpututil.read_ip_address()
    port_ranges = inpututil.read_port_range()

    # Prompt to obtain the scan type
    choice = ""
    while True:
        choice = input("Please select the type of scan to be conducted: \n"
                       "1. SYN ACK Scan\n"
                       "2. UDP Scan\n"
                       "3. Comprehensive Scan\n"
                       "Enter your choice: ")
        if not (choice.isdecimal() and 1 <= int(choice) <= 3):
            print("Invalid Choice. It must be 1,2 or 3!")
        else:
            break

    return ip, port_ranges[0], port_ranges[1], int(choice)


# Main function
if __name__ == '__main__':
    # Create an scanner object
    scanner = nmap.PortScanner()

    ip_address, min_port, max_port, scan_type = user_menu()
    print('\n')

    # SYN ACK Scan
    if scan_type == 1:
        scanner.scan(ip_address, f'{min_port}-{max_port}', '-v -sS')
    elif scan_type == 2:
        scanner.scan(ip_address, f'{min_port}-{max_port}', '-v -sU')
    else:
        scanner.scan(ip_address, f'{min_port}-{max_port}', '-v -sS -sU -sV -sC -A -O')

    print('Nmap Version: ', scanner.nmap_version() )
    print('Scan Info: ', scanner.scaninfo() )

    print('Host address: ', ip_address)
    # If only comprehensive scan is selected
    if 'osmatch' in scanner[ip_address].keys():
        print('Possible Host OS: ')
        for os in scanner[ip_address]['osmatch']:
            print(f'\t{os["name"]}  ({os["accuracy"]}%)')
    print('\nHost name: ', scanner[ip_address].hostname() )
    print('Host status: ', scanner[ip_address].state() )
    print('Host protocols: ', scanner[ip_address].all_protocols() )

    # For each of the available protocol (tcp, udp)
    for protocol in scanner[ip_address].all_protocols():
        print('Open port of protocol', protocol, ':', scanner[ip_address][protocol].keys() )

        # Ask user if they want to see detail on each of the open ports
        if input('\nEnter "d" for details on each open port: ') == 'd':
            for port in scanner[ip_address][protocol].keys():
                print(f'[Port {port} of protocol {protocol}]"=======================================================\n'
                      f'{scanner[ip_address][protocol][port]}\n')
