#!/usr/bin/env python
# vim: set ts=2 sw=2 ai et:
# 
import nmapTools
import dnsTools
import csv

# replace IP Range with range of your choosing
results = nmapTools.ping_sweep('192.168.1.0/24')

# dnsTools uses your local machines DNS servers to run query
for x in results:
        #print(x)
        for y in results[x]:
                #print (y,':',results[x][y])
                dns_rec = dnsTools.lookup(y)
                if dns_rec[2] is not None:
                        print (dns_rec[2],dns_rec[0],dns_rec[0])
