#!/usr/bin/env python

from random import randint

class IPv4Random(object):

    ipv4_ranges = [ { 'start':0x3000000, 'end':0x3ffffff },        # GE
                    { 'start':0x4000000, 'end':0x4ffffff },        # Level3
                    { 'start':0x7000000, 'end':0x7ffffff },        # ARIN
                    { 'start':0x8000000, 'end':0x8ffffff },        # Level3
                    { 'start':0x9000000, 'end':0x9ffffff },        # IBM
                    { 'start':0xc000000, 'end':0xcffffff },        # ATT
                    { 'start':0xd000000, 'end':0xdffffff },        # Xerox
                    { 'start':0xf000000, 'end':0xfffffff },        # HP
                    { 'start':0x10000000, 'end':0x10ffffff },      # DEC
                    { 'start':0x11000000, 'end':0x11ffffff },      # Apple
                    { 'start':0x12000000, 'end':0x12ffffff },      # MIT
                    { 'start':0x13000000, 'end':0x13ffffff },      # Ford ?
                    { 'start':0x14000000, 'end':0x14ffffff },      # CSC ?
                    { 'start':0x19000000, 'end':0x19ffffff },      # UK ?
                    { 'start':0x20000000, 'end':0x20ffffff },      # ATT
                    { 'start':0x22000000, 'end':0x22ffffff },      # HBurton
                    { 'start':0x23000000, 'end':0x23ffffff },      # Merit
                    { 'start':0x26000000, 'end':0x26ffffff },      # Cogent
                    { 'start':0x28000000, 'end':0x28ffffff },      # ELilly
                    { 'start':0x2c000000, 'end':0x2cffffff },      # AmRadio ?
                    { 'start':0x2f000000, 'end':0x2fffffff },      # BellNorth  
                    { 'start':0x30000000, 'end':0x30ffffff },      # Prudent
                    { 'start':0x33000000, 'end':0x33ffffff },      # UK Gov ?
                    { 'start':0x34000000, 'end':0x34ffffff },      # duPont
                    { 'start':0x35000000, 'end':0x35ffffff },      # Daimler
                    { 'start':0x36000000, 'end':0x36ffffff },      # Merck
                    { 'start':0x38000000, 'end':0x38ffffff },      # USPS ?
                    { 'start':0x39000000, 'end':0x39ffffff },      # SITA
                    { 'start':0x3a000000, 'end':0x3affffff },      # APNIC
                    { 'start':0x3b000000, 'end':0x3bffffff },      # APNIC
                  ]

    def __init__(self,**rangeoptions):
        # Place holder for possible options
        self.placeholder = False

    def get_random(self):
        ranges_length = len(self.ipv4_ranges)
        random_range = randint(0,ranges_length - 1)
        random_ipv4 = randint(self.ipv4_ranges[random_range]['start'],
                              self.ipv4_ranges[random_range]['end'])

        quad_ipv4 ="{}.{}.{}.{}".format( ((random_ipv4 & 0xff000000) >>24),
                                         ((random_ipv4 & 0xff0000) >>16),
                                         ((random_ipv4 & 0xff00)) >>8,
                                         (random_ipv4 & 0xff)
                                       )
        return quad_ipv4

if __name__ == "__main__":
    m = IPv4Random()
    print(m.get_random())
