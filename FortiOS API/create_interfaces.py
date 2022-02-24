import csv
import requests
import re
import json
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()
import sys

# provide the IP or FQDN as argument when running the script
host = sys.argv[1]
# use the URL to match the right api_key
with open('api-key.json') as g:
    json_dict = json.load(g)
    api_key = json_dict[host]

def Create_Interface(host,api_key):
    '''
    This function will create VLAN interfaces on a Fortigate based on a CSV source file.
    It uses the FortiOS RESTAPI (tested on 6.4.8)
    The minimum required fields are ip, interface, vdom, vlanid and name
    '''
    f = open('vlans.csv')
    reader = csv.DictReader(f, delimiter=';')
    headers = reader.fieldnames
    vlans = []
    for row in reader:
    	vlans.append(row)
    http_header = {'content-type':'application/json', 'Accept': 'application/json'}
    url = 'https://' + host + '/api/v2/cmdb/system/interface/?access_token=' + api_key

    for vlan in vlans:
        prefix = re.search('(?P<suffix>\/\d\d)',vlan['Subnet']) # extract the suffix of the CIDR
        ip = str(vlan['Default Gateway'] + prefix.group('suffix')) # construct the ip composed of the gateway address + suffix
        payload = {
            "name": vlan['Name'],
            "type": "vlan",
            "ip": ip,
            "mode": 'static',
            "interface": "port2",
            "vlanid": vlan['VLAN'],
            "vdom": "root"
            }
        global response
        response = requests.post(url, data=json.dumps(payload), headers=http_header, verify=False)
        if response.status_code == 200:
            print(response.text)
        else:
            print(response.status_code)

if __name__ == "__main__":
    Create_Interface(host,api_key)
