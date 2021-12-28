from jinja2 import Environment, FileSystemLoader, Template
import csv
import yaml

ENV = Environment(loader=FileSystemLoader('./'))
template = ENV.get_template("FW_address_template.j2")

f = open('subnet_export.csv')
reader = csv.DictReader(f, delimiter=';')
headers = reader.fieldnames
subnets = []
for row in reader:
	subnets.append(row)

print(template.render(subnets=subnets))

f.close()
