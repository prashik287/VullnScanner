import requests
import json

class Reconnaissance:

    @staticmethod
    def whoislookup(target):
        whoisd = {}
        wisapi=requests.get(f"https://api.domaintools.com/v1/domaintools.com/whois/{target}")
        data = json.loads(wisapi.text)
        formatted = data.get('response', {})
        if isinstance(formatted, dict):
            for key, value in formatted.items():
                whoisd[f'{key}'] =f"{value}"
            return whoisd
        else:
            print("Response is not a dictionary")
    @staticmethod
    def reverse_dns(target):
        rdnsapi = f"https://api.hackertarget.com/reversedns/?q={target}"
        response = requests.get(rdnsapi)
        return response.text

    @staticmethod
    def dnslookup(target):
        dnsapi = f"https://api.hackertarget.com/dnslookup/?q={target}"
        response = requests.get(dnsapi)
        return response.text

    @staticmethod
    def hostsearch(target):
        hostsearchapi = f"https://api.hackertarget.com/hostsearch/?q={target}"
        response = requests.get(hostsearchapi)
        return response.text

    @staticmethod
    def zonetransfer(target):
        zonetransferapi = f"https://api.hackertarget.com/zonetransfer/?q={target}"
        response = requests.get(zonetransferapi)
        return response.text

    @staticmethod
    def reverselookupip(target):
        reverseipapi = f"https://api.hackertarget.com/reverseiplookup/?q={target}"
        response = requests.get(reverseipapi)
        return response.text

    @staticmethod
    def get_ip(domain):
        try:
            dns_response = requests.get(f"https://api.hackertarget.com/dnslookup/?q={domain}").text
            for line in dns_response.split('\n'):
                if 'A' in line:
                    return line.split(',')[1].strip()
            raise Exception("IP address not found")
        except Exception as e:
            raise Exception("Failed to get IP from domain")

    # whoislookup("dmce.ac.in")