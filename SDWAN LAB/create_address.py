import json
import requests
import csv
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()
import sys

# provide the IP or FQDN as argument when running the script
host = sys.argv[1]
# use the URL to match the right api_key
with open('api-key.json') as g:
    json_dict = json.load(g)
    api_key = json_dict[host]

def Get_Address(host,api_key):

    http_header = {'content-type':'application/json', 'Accept': 'application/json'}
    url = 'https://'+ host + '/api/v2/cmdb/firewall/address/?access_token=' + api_key
    payload = {}
    response = requests.get(url, data=json.dumps(payload), headers=http_header, verify=False)
    address_dict = json.loads(response.text)
    address_list = address_dict['results']
    return address_list

def Create_Address(host,api_key):

    address_list = Get_Address(host,api_key)
    f = open('subnets.csv')
    reader = csv.DictReader(f, delimiter=';')
    headers = reader.fieldnames
    subnets = []
    for row in reader:
    	subnets.append(row)
    http_header = {'content-type':'application/json', 'Accept': 'application/json'}
    url = 'https://' + host + '/api/v2/cmdb/firewall/address/?access_token=' + api_key

    for subnet in subnets:
        name = str("n-" + subnet['IP range'] + subnet['Subnet mask'])
        cidr = str(subnet['IP range'] + subnet['Subnet mask'])
        if name in json.dumps(address_list):
                print(f"address already exists, skipping {name}")
        else:
            payload = {
                "name": name,
                "type": "ipmask",
                "subnet": cidr,
                "comment": subnet['Comment'],
                "color": 19
                }
            response = requests.post(url, data=json.dumps(payload), headers=http_header, verify=False)
            print(response.text)

if __name__ == "__main__":
    Create_Address(host,api_key)
