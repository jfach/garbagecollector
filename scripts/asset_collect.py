#!/usr/bin/env python
import nmapTools
import dnsTools
import csv
import getopt
import os
import sys
import time
import ad_server
import gc_asset
import issue_handler

# Read a file of networks in the format
# net_block(n),n.n.n.n/n
# example: net_block1,192.168.1.0/24
# Store in networks.txt (local directory)
# Use the file to create a dictionary of desired networks to scan

try:
    opts, args = getopt.getopt(
                               sys.argv[1:],
                               "a:b:n:c:",
                               ["adseed=", "block=", "netseed=", "csvfile="]
                               )
except getopt.GetoptError as err:
    print(str(err))
    print("Usage: python asset_collect.py [-n netseed] [-b block] [-c csvfile]")
    sys.exit(2)
block = None
csvfilename = None
netfile = 'seeds/net_seed.txt'
ad_seed = 'seeds/ad_seed.txt'
for o, a in opts:
    if o in ("-c", "--csvfile"):
        csvfilename = a
    elif o in ("-n", "--netseed"):
        netfile = a
    elif o in ("-b", "--block"):
        block = a
    elif o in ("-a", "--adseed"):
	ad_seed = a
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
ad_servers = []
with open(ad_seed) as f:
    for line in f:
      ad = line.rstrip('\n').split(',')
      ad_servers.append(ad_server.AD_Server(ad[1]))

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

output = {}

print "Starting scan..."

assets = []
for result in results:
    ips = result['scan'].keys()
    for ip in ips:
        output[ip] = {}
        dns_rec = dnsTools.lookup(ip)
        print dns_rec[0]
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
                this_asset = gc_asset.Asset(ip,
					    ad_servers,
					    ad_results,
					    2,
					    dns_rec[0])
                assets.append(this_asset)
            else:
                assert len(ad_servers) == ad_results.count([])
                output[ip]['result_code'] = 3
                this_asset = gc_asset.Asset(ip,
					    ad_servers,
					    ad_results,
					    3,
					    dns_rec[0])
                assets.append(this_asset)
        else:
            output[ip]['result_code'] = 1  # 2 peice missing
            this_asset = gc_asset.Asset(ip,
				        ad_servers,
			                ad_results,
					1)
            assets.append(this_asset)

print "Scan complete"
print "Creating issues for asset objects..."
for asset in assets:
    issue_handler.gen_issue(asset)

if csvfilename:
    print "Writing output to csv..."
    with open(csvfilename, 'w') as csvfile:
        fieldnames = ['ip', 'result_code']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow(dict(zip(writer.fieldnames, writer.fieldnames)))
        for ip in output.keys():
            writer.writerow({
                'ip': ip,
                'result_code': output[ip]['result_code']

            })
    print "Wrote output to " + csvfilename

print "Done"
