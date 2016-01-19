#!/usr/bin/env python
# vim: set ts=2 sw=2 ai et:
import nmapTools
import dnsTools
import csv
import getopt
import os
import sys
import ad_server

# Read a file of networks in the format
# net_block(n),n.n.n.n/n
# example: net_block1,192.168.1.0/24
# Store in networks.txt (local directory)
# Use the file to create a dictionary of desired networks to scan

try:
    opts, args = getopt.getopt(sys.argv[1:], "b:n:c:", ["block=", "netfile=", "csvfile="])
except getopt.GetoptError as err:
    print(str(err))
    print("Usage: python asset_collect.py [-n netfile] [-c csvfile]")
    sys.exit(2)
block = None
csvfilename = None
netfile = 'networks.txt'
for o, a in opts:
    if o in ("-c", "--csvfile"):
        csvfilename = a
    elif o in ("-n", "--netfile"):
        netfile = a
    elif o in ("-b", "--block"):
        block = a
    else:
        assert False, "unhandled option"

net_dict = {}
if block:
  net_dict['cmd_line_netblock'] = block
else:
  with open(netfile) as f:
      for line in f:
          network = line.rstrip('\n').split(',')
          net_dict[network[0]] = (network[1])
# logging (test)

# iterate through each K,V in net_dict then scan
# append each scan result to results list
results = []
for k, v in net_dict.iteritems():
    results.append(nmapTools.ping_sweep(v))
# logging (test)

# iterate through each ip in each result dict in results list
# if the ip has not been looked up, look it up and add it to lookups list
dns_list = []
lookups = []

ad_test1 = ad_server.AD_Server('TC-AD01')
ad_test2 = ad_server.AD_Server('TC-AD02')
ad_prod1 = ad_server.AD_Server('TD-AD01')
ad_prod2 = ad_server.AD_Server('TC-AD02')
ad_servers = [ad_test1, ad_test2, ad_prod1, ad_prod2]

output = {}

for result in results:
    ips = result['scan'].keys()
    for ip in ips:
        output[ip] = {}
        print ip
        dns_rec = dnsTools.lookup(ip)
        if dns_rec[2] is not None:
            output[ip]['dns'] = dns_rec[0]
            ad_results = []
            for server in ad_servers:
                ad_host = server._find_host(output[ip]['dns'].split('.')[0])
                ad_results.append(ad_host)
            if [] not in ad_results:
                output[ip]['result_code'] = 0  # all good
            elif ad_results.count([]) < len(ad_servers):
                output[ip]['result_code'] = 2
            else:
                assert len(ad_servers) == ad_results.count([])
                output[ip]['result_code'] = 3
        else:
            output[ip]['result_code'] = 1  # 2 peice missing

print output

"""
for result in results:
            lookups.append(ip)
            dns_rec = dnsTools.lookup(ip)
            if dns_rec[2] is not None:
                print "found " + ip + " with dns: "
                dns_dict = {
                    'ip': dns_rec[2][0],
                    'fqdn': dns_rec[0],
                    'alias': dns_rec[1]
       

if csvfilename:
    with open(csvfilename, 'w') as csvfile:
        fieldnames = ['ip', 'result_code']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow(dict(zip(writer.fieldnames, writer.fieldnames)))
        for ip in output.keys():
            writer.writerow({
                'ip': ip,
                'result_code': output[ip]['result_code']
            })
