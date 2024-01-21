import re


def validate_ip_regex(ip_address):
    pattern = re.match(r"'\d'{1,3}\.'\d'{1,3}\.'\d'{1,3}\.'\d'{1,3}", ip_address)

    address = ip_address.split(".")

    for ip_byte in address:
        if int(ip_byte) < 0 or int(ip_byte) > 255:
            print(f"The IP address '{ip_address}' is not valid")
            return False

    print(f"The IP address '{ip_address}' is valid")
    return True


def validate_ipv6_regex(ipv6):
    a = re.match(
        r"([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|"
        r"([0-9a-fA-F]{1,4}:){1,7}:|"
        r"([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|"
        r"([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|"
        r"([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|"
        r"([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|"
        r"([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|"
        r"[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|"
        r":((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-fA-F]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|"
        r"([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])",
        ipv6)

    if a:
        print(f"The IPv6 '{ipv6}' is valid")
    else:
        print(f"The IPv6 '{ipv6}' is not valid")


a = input("Enter the IPv4: ")
b = input("Enter the IPv6: ")
validate_ip_regex(a)
validate_ipv6_regex(b)

