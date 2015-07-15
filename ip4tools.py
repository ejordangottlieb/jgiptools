#!/usr/bin/env python

from random import randint
from IPv4Iana import AddressAssignments as current
from time import sleep

class IPv4Random(object):

    def __init__(self,**rangeoptions):
        self.placeholder = False

    def _get_range_entry(self, ipv4_range):
        ranges_length = len(ipv4_range)
        random_range = randint(0,ranges_length - 1)
        return random_range
    
    def get_random(self):
        random_range = self._get_range_entry(current.ipv4_ranges)
        
        if ( current.ipv4_ranges[random_range]['start'] == 0x64000000 ):
            random_range = self._get_range_entry(current.ipv4_100)
            random_ipv4 = randint(current.ipv4_100[random_range]['start'],
                                  current.ipv4_100[random_range]['end'])
        elif ( current.ipv4_ranges[random_range]['start'] == 0xa9000000 ):
            ipv4 = current()
            ipv4_169 = ipv4.get_169()
            random_range = self._get_range_entry(ipv4_169)
            random_ipv4 = randint(ipv4_169[random_range]['start'],
                                  ipv4_169[random_range]['end'])

        elif ( current.ipv4_ranges[random_range]['start'] == 0xac000000 ):
            random_range = self._get_range_entry(current.ipv4_172)
            random_ipv4 = randint(current.ipv4_172[random_range]['start'],
                                  current.ipv4_172[random_range]['end'])

        elif ( current.ipv4_ranges[random_range]['start'] == 0xc0000000 ):
            ipv4 = current()
            ipv4_192 = ipv4.ipv4_192
            random_range = self._get_range_entry(ipv4_192)
            ip_192 = ipv4.get_192(ipv4_192[random_range]['start'])
            random_range = self._get_range_entry(ip_192)
            random_ipv4 = randint(ip_192[random_range]['start'],
                                  ip_192[random_range]['end'])

        else:
            random_ipv4 = randint(current.ipv4_ranges[random_range]['start'],
                                  current.ipv4_ranges[random_range]['end'])

        quad_ipv4 ="{}.{}.{}.{}".format( ((random_ipv4 & 0xff000000) >>24),
                                         ((random_ipv4 & 0xff0000) >>16),
                                         ((random_ipv4 & 0xff00)) >>8,
                                         (random_ipv4 & 0xff)
                                       )
        return quad_ipv4

if __name__ == "__main__":
    m = IPv4Random()
    count = 0
    while (True):
        test = m.get_random() 
        #if (True):
        if ( test[0:8] == '192.0.3.' ):
            print(test)
            print(count)
            #sleep(1)
            count = 0

        else:
            #print(test)
            count += 1
