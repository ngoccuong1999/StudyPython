import requests
import json
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

url = 'https://127.0.0.1:8443/api/v1/firewall/rule'
urltest = 'https://api.abuseipdb.com/api/v2/check'

payload = {
    "client-id": "admin",
    "client-token": "h4;+GTA5pgFEL^'#",
    "type": "block",
    "interface": "wan",
    "ipprotocol": "inet",
    "protocol": "tcp",
    "src": "172.16.209.138",
    "srcport": "any",
    "dst": "vtnet0",
    "dstport": 443,
    "descr": "This is a test rule added via API",
    "top": True
}
response = requests.post(url, verify=False, json=payload)
print(response.content)
#reference
#https://stackoverflow.com/questions/15445981/how-do-i-disable-the-security-certificate-check-in-python-requests
