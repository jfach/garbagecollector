#!/usr/bin/env python
# vim: set ts=2 sw=2 ai et:

import nmap


def ping_sweep(ip_block):
    """
    Really unintrusive nmap discovery ping scan
    Arguments: ip_block = subnet(string)
    Returns: Scan Results(dictionary)
    """
    nm = nmap.PortScanner()
    results = nm.scan(hosts=ip_block,  arguments='-n -sP -PE')
    return results
