import ipaddress
import re
import  whois
from tld import get_tld




def is_ip_address(input_string):
    try:
        ipaddress.ip_address(input_string)
        return True
    except ValueError:
        return False

def is_domain_name(input_string):
    domain_regex = re.compile(
        r'^(?:[a-zA-Z0-9]' # First character of the domain
        r'(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)' # Sub domain + hostname
        r'+[a-zA-Z]{2,6}$' # First level TLD
    )
    return re.match(domain_regex, input_string) is not None





# Example usage
# user_input = input("Enter a domain name or an IP address: ")
# result = check_input(user_input)
# print(f"The input is a {result}.")
#
# check_whois("dmce.ac.in")
