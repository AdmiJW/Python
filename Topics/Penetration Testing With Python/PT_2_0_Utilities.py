import re


########################################################################################
# Reads an IP address from the user. Ensured it is in x.x.x.x format where 0 <= x <= 255
def read_ip_address():
    ip_regex = re.compile('^(?:\d{1,3}\.){3}\d{1,3}$')
    ip_address = input("Please Enter the IP address you want to be scanned (Eg: 192.168.0.1): ")

    while True:
        # Failed Regex test
        if not ip_regex.fullmatch(ip_address):
            print("Invalid IP Address format")
            ip_address = input("Please Enter the IP address you want to be scanned (Eg: 192.168.0.1): ")
            continue

        # [0,255] Range test
        ip_groups = map(lambda g: int(g), ip_address.split('.'))
        is_all_in_range = all(map(lambda x: 0 <= x <= 255, ip_groups))

        if not is_all_in_range:
            print("Invalid IP Address. Groups must be in range [0,255].")
            ip_address = input("Please Enter the IP address you want to be scanned (Eg: 192.168.0.1): ")
            continue

        return ip_address


###############################################################################################
# Reads a range of port number from the user. Ensured it is in x-x format where 0 <= x <= 65535
# Returns a tuple of (smallerPort, largerPort)
def read_port_range():
    port_regex = re.compile('^\d{1,5}-\d{1,5}$')

    while True:
        port_range = input("Please Enter a range of port numbers (Eg: 0-65535): ")

        # Failed Regex Test
        if not port_regex.fullmatch(port_range):
            print("Invalid Port Range format. It must be in format 'X-X'")
            continue

        # [0,65535] Range test
        ip_groups = tuple( map(lambda g: int(g), port_range.split('-')) )
        is_all_in_range = all(map(lambda x: 0 <= x <= 65535, ip_groups))

        if not is_all_in_range:
            print("Invalid Port Range. Groups must be in range [0,65535].")
            continue

        return min(ip_groups), max(ip_groups)