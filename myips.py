# -*- coding: utf-8 -*-

import socket
import psutil  # install

''' Get ipv4 addresses on this environment.
Returns:
    list: ipv4 addresses
e.g.
    [{'lo0': '127.0.0.1'}, {'en0': '192.168.3.5'}]
'''


def getIpv4():
    result = list()
    for interface, snics in psutil.net_if_addrs().items():
        for snic in snics:
            if snic.family == socket.AF_INET:
                ipv4 = {
                    interface: snic.address
                }
                result.append(ipv4)
    return result
