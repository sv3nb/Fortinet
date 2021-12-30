import json
import requests
import csv
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

def Get_Address():

    http_header = {'content-type':'application/json', 'Accept': 'application/json'}
    url = 'https://16.170.227.201/api/v2/cmdb/firewall/address/?access_token=wfnG5Nfmdy933gfnsN735q68nhGcqw&format=name'
    payload = {}
    response = requests.get(url, data=json.dumps(payload), headers=http_header, verify=False)
    address_dict = json.loads(response.text)
    address_list = address_dict['results']
    return address_list

def Create_Address():

    address_list = Get_Address()
    f = open('subnets.csv')
    reader = csv.DictReader(f, delimiter=';')
    headers = reader.fieldnames
    subnets = []
    for row in reader:
    	subnets.append(row)
    http_header = {'content-type':'application/json', 'Accept': 'application/json'}
    url = 'https://16.170.227.201/api/v2/cmdb/firewall/address/?access_token=wfnG5Nfmdy933gfnsN735q68nhGcqw'

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
    Create_Address()
