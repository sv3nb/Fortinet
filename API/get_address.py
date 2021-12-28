import json
import requests
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

if __name__ == "__main__":


# RESTAPI request retrieves firewall address name and comment fields
        headers = {'content-type':'application/json', 'Accept': 'application/json'}
        url = 'https://13.49.223.59/api/v2/cmdb/firewall/address/?access_token=x5mH9kQct1Qn8gkbw8zy5rbGkkqN0g&format=name|comment'
        payload = {}


response = requests.get(url, data=json.dumps(payload), headers=headers, verify=False)
address_dict = json.loads(response.text)
address_list = address_dict['results']

for address in address_list:
        if "google" in address['name']:
                print("google address present!")
        else:
                pass
