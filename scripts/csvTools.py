import csv

def write_dict(filename, dns_dict):
	with open(filename, 'w') as csvfile:
		fieldnames = ['ip', 'fqdn', 'alias']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writerow(dns_dict)

