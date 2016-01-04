#!/usr/bin/env python
# vim: set ts=2 sw=2 ai et:
import socket


def lookup(addr):
    """
    Get DNS records of ip/host and make
    sure to catch errors if no records exist
    Arguments: addr = ip address or hostname(string)
    Returns: (hostname(string), aliaslist(list), ipaddrlist(list))
    """
    try:
        return socket.gethostbyaddr(addr)
    except (socket.herror, socket.gaierror) as e:
        return None, None, None
