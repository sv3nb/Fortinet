from jinja2 import Environment, FileSystemLoader, Template
import csv
import socket
import yaml

file = open('public_ip_list.txt')
list = []
lines = file.readlines()
for line in lines:
	list.append(line.rstrip())
# we now have an array of IP addresses called 'list'

address_list = []
for ip in list:
	mydict = {}
	mydict["FQDN"] = socket.gethostbyaddr(ip)[0]
	mydict["ip"] = socket.gethostbyaddr(ip)[2][0]
	address_list.append(mydict)
# we now have a list with nested dictionaries each containing {FQDN: value, ip: value}
# we feed this dictionary to our Jinja template

ENV = Environment(loader=FileSystemLoader('./'))
template = ENV.get_template("FW_public_address_template.j2")
print(template.render(address_list=address_list))

file.close()
