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

def Get_Service(host,api_key):

    http_header = {'content-type':'application/json', 'Accept': 'application/json'}
    url = 'https://' + host + '/api/v2/cmdb/firewall.service/custom/?access_token=' + api_key
    payload = {}
    response = requests.get(url, data=json.dumps(payload), headers=http_header, verify=False)
    service_dict = json.loads(response.text)

    # we contruct a list with only the name of the service objects
    service_list = []
    for service in service_dict['results']:
        service_list.append(service['name'])
    return service_list

def Create_Service(host,api_key):

    service_list = Get_Service(host,api_key) # retrieve a list of existing service objects
    http_header = {'content-type':'application/json', 'Accept': 'application/json'}
    url = 'https://'+ host +'/api/v2/cmdb/firewall.service/custom/?access_token=' + api_key
    f = open('services.csv')
    reader = csv.DictReader(f, delimiter=';')
    headers = reader.fieldnames
    services = []
    for row in reader:
    	services.append(row)
    for service in services:
        if service["name"] in json.dumps(service_list):  # convert dict to formatted text so we can validate if the string is present
            print('service exists')
        else:
            payload = {
                "name": service["name"],
                "protocol": service["protocol"],
                "tcp-portrange": service["tcp-portrange"],
                "udp-portrange": service['udp-portrange'],
                "comment": service["comment"],
                "color": service["color"],
                }
            response = requests.post(url, data=json.dumps(payload), headers=http_header, verify=False)
            print(response.text)

if __name__ == "__main__":
    Create_Service(host,api_key)
