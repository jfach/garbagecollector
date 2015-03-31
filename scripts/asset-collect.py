
#!/usr/bin/env python
# vim: set ts=2 sw=2 ai et:
# 
# http://stackoverflow.com/questions/10373247/how-do-i-write-a-python-dictionary-to-a-csv-file

import nmapTools
import dnsTools
import csv
import os

results = nmapTools.ping_sweep('6.3.3.0/24')

for x in results:
  for y in results[x]:
    dns_rec = dnsTools.lookup(y)
    # uncomment to test
    #print (y,dns_rec[0],dns_rec[1],dns_rec[2])
    if dns_rec[2] is not None:
        # uncomment to test
        # print (dns_rec[2])
        dns_dict = {'ip':dns_rec[2], 'fqdn': dns_rec[0], 'alias': dns_rec[1]}
        # uncomment to test
	# print dns_dict


with open('test.csv', 'wb') as f:
  w = csv.DictWriter(f,dns_dict.keys())
  for data in dns_dict:
    w.writerow(dns_dict)
    f.close()

