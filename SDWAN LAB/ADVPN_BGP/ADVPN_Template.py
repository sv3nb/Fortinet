from jinja2 import Environment, FileSystemLoader, Template
import csv
import yaml

# load in CSV file and create a list of dictionaries to feed into the template
gateways = open('gateways.csv')
reader = csv.DictReader(gateways, delimiter=';')
fortigates = []
for row in reader:
	fortigates.append(row)

# string consisting of multiple items separated by a comma is converted to list
for fortigate in fortigates:
	fortigate['protected subnets'] = fortigate['protected subnets'].split(',')
# Generate Jinja Template with variables
	ENV = Environment(loader=FileSystemLoader('./'))
	template = ENV.get_template("ADVPN_BGP_Template.j2")
	output_template = template.render(hostname = fortigate['hostname'], \
	subnets = fortigate['protected subnets'], \
	role = fortigate['role'].lower(), \
	tunnel_IP = fortigate['tunnel IP'], \
	ASN = fortigate['ASN'], \
	WAN_interface = fortigate['WAN interface'], \
	remote_gateway = fortigate['remote gateway'], \
	ADVPN = fortigate['ADVPN'], \
	summarize = fortigate['summarize'], \
	loopback_IP = fortigate['loopback IP'],
	overlay_subnet = '172.31.100.0/24'
	)
	with open(f'{fortigate["hostname"]}.cfg', "w") as config_file:
		config_file.write(output_template)
