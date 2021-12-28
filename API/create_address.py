import json
import requests
import csv
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

def Get_Address(url, key):
    url = url
    key = key
    headers = {'content-type':'application/json', 'Accept': 'application/json'}
    url = 'https://192.168.108.100/api/v2/cmdb/firewall/address/?access_token=8bNyng9Nm0t8550cr03ypf57HsjdnG&format=name|comment'
    payload = {}
    response = requests.get(url, data=json.dumps(payload), headers=headers, verify=False)
    address_dict = json.loads(response.text)
    address_list = address_dict['results']
    return address_list

def Create_Address(url, key):
    url = url
    key = key
    f = open('subnets.csv')
    reader = csv.DictReader(f, delimiter=';')
    headers = reader.fieldnames
    subnets = []
    for row in reader:
    	subnets.append(row)

    address_list = Get_Address()
    headers = {'content-type':'application/json', 'Accept': 'application/json'}
    url = 'https://192.168.108.100/api/v2/cmdb/firewall/address/?access_token=8bNyng9Nm0t8550cr03ypf57HsjdnG'

    for subnet in subnets:
        name = str("n-" + subnet['IP range'] + subnet['Subnet mask'])
        cidr = str(subnet['IP range'] + subnet['Subnet mask'])
        for address in address_list:
            if name in address['name']:
                pass
            else:
                payload =
                {
                    "name": name,
                    "type": "ipmask",
                    "subnet": cidr,
                    "comment": subnet['Comment'],
                    "color": 19
                }
        response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
        print(response.text)

if __name__ == "__main__":
    Create_Address()
