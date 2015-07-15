class AddressAssignments(object):
    ipv4_ranges = [ { 'start':0x1000100, 'end':0x1ffffff },        # APNIC
                    { 'start':0x2000000, 'end':0x2ffffff },        # RIPE
                    { 'start':0x3000000, 'end':0x3ffffff },        # GE 
                    { 'start':0x4000000, 'end':0x4ffffff },        # Level3
                    { 'start':0x5000000, 'end':0x5ffffff },        # RIPE
# Army Info Sys CTR { 'start':0x6000000, 'end':0x6ffffff },
                    { 'start':0x7000000, 'end':0x7ffffff },        # ARIN
                    { 'start':0x8000000, 'end':0x8ffffff },        # Level3
                    { 'start':0x9000000, 'end':0x9ffffff },        # IBM
# IANA Private      { 'start':0xa000000, 'end':0xaffffff },
# DOD Intel Info    { 'start':0xb000000, 'end':0xbffffff },
                    { 'start':0xc000000, 'end':0xcffffff },        # ATT
                    { 'start':0xd000000, 'end':0xdffffff },        # Xerox
                    { 'start':0xe000000, 'end':0xeffffff },        # APNIC
                    { 'start':0xf000000, 'end':0xfffffff },        # HP
                    { 'start':0x10000000, 'end':0x10ffffff },      # DEC
                    { 'start':0x11000000, 'end':0x11ffffff },      # Apple
                    { 'start':0x12000000, 'end':0x12ffffff },      # MIT
                    { 'start':0x13000000, 'end':0x13ffffff },      # Ford ?
                    { 'start':0x14000000, 'end':0x14ffffff },      # CSC ?
# DDR-RVN           { 'start':0x15000000, 'end':0x16ffffff },
# Def Inf Sys Agncy { 'start':0x16000000, 'end':0x17ffffff },
                    { 'start':0x17000000, 'end':0x17ffffff },      # ARIN
                    { 'start':0x18000000, 'end':0x18ffffff },      # ARIN
# UK Min of Defence { 'start':0x19000000, 'end':0x19ffffff },
                    { 'start':0x20000000, 'end':0x20ffffff },      # ATT
# DLA SysAutmtn Ctr { 'start':0x21000000, 'end':0x21ffffff },
                    { 'start':0x22000000, 'end':0x22ffffff },      # HBurton
                    { 'start':0x23000000, 'end':0x23ffffff },      # Merit
                    { 'start':0x24000000, 'end':0x24ffffff },      # Apnic
                    { 'start':0x25000000, 'end':0x25ffffff },      # Ripe NCC
                    { 'start':0x26000000, 'end':0x26ffffff },      # Cogent
                    { 'start':0x27000000, 'end':0x27ffffff },      # Apnic 
                    { 'start':0x28000000, 'end':0x28ffffff },      # ELilly
                    { 'start':0x29000000, 'end':0x29ffffff },      # AFRINIC
                    { 'start':0x2a000000, 'end':0x2affffff },      # APNIC
                    { 'start':0x2b000000, 'end':0x2bffffff },      # APNIC ?
                    { 'start':0x2c000000, 'end':0x2cffffff },      # Mult Reg ?
                    { 'start':0x2d000000, 'end':0x2dffffff },      # Ripe
                    { 'start':0x2f000000, 'end':0x2fffffff },      # BellNorth  
                    { 'start':0x30000000, 'end':0x30ffffff },      # Prudent
                    { 'start':0x31000000, 'end':0x31ffffff },      # APNIC
                    { 'start':0x32000000, 'end':0x32ffffff },      # ARIN
                    { 'start':0x33000000, 'end':0x33ffffff },      # UK Gov ?
                    { 'start':0x34000000, 'end':0x34ffffff },      # ARIN  
                    { 'start':0x35000000, 'end':0x35ffffff },      # Daimler
                    { 'start':0x36000000, 'end':0x36ffffff },      # AMZN & Merck
# DoD Net Info Ctr  { 'start':0x37000000, 'end':0x37ffffff },
# USPS              { 'start':0x38000000, 'end':0x38ffffff },
                    { 'start':0x39000000, 'end':0x39ffffff },      # SITA
                    { 'start':0x3a000000, 'end':0x3affffff },      # APNIC
                    { 'start':0x3b000000, 'end':0x3bffffff },      # APNIC
                    { 'start':0x3c000000, 'end':0x3cffffff },      # APNIC
                    { 'start':0x3d000000, 'end':0x3dffffff },      # APNIC
                    { 'start':0x3e000000, 'end':0x3effffff },      # RIPE NCC
                    { 'start':0x3f000000, 'end':0x3fffffff },      # ARIN
                    { 'start':0x40000000, 'end':0x40ffffff },      # ARIN
                    { 'start':0x41000000, 'end':0x41ffffff },      # ARIN
                    { 'start':0x42000000, 'end':0x42ffffff },      # ARIN
                    { 'start':0x43000000, 'end':0x43ffffff },      # ARIN
                    { 'start':0x44000000, 'end':0x44ffffff },      # ARIN
                    { 'start':0x45000000, 'end':0x45ffffff },      # ARIN
                    { 'start':0x46000000, 'end':0x46ffffff },      # ARIN
                    { 'start':0x47000000, 'end':0x47ffffff },      # ARIN
                    { 'start':0x48000000, 'end':0x48ffffff },      # ARIN
                    { 'start':0x49000000, 'end':0x49ffffff },      # ARIN
                    { 'start':0x4a000000, 'end':0x4affffff },      # ARIN
                    { 'start':0x4b000000, 'end':0x4bffffff },      # ARIN
                    { 'start':0x4c000000, 'end':0x4cffffff },      # ARIN
                    { 'start':0x4d000000, 'end':0x4dffffff },      # RIPE NCC
                    { 'start':0x4e000000, 'end':0x4effffff },      # RIPE NCC
                    { 'start':0x4f000000, 'end':0x4fffffff },      # RIPE NCC
                    { 'start':0x50000000, 'end':0x50ffffff },      # RIPE NCC
                    { 'start':0x51000000, 'end':0x51ffffff },      # RIPE NCC
                    { 'start':0x52000000, 'end':0x52ffffff },      # RIPE NCC
                    { 'start':0x53000000, 'end':0x53ffffff },      # RIPE NCC
                    { 'start':0x54000000, 'end':0x54ffffff },      # RIPE NCC
                    { 'start':0x55000000, 'end':0x55ffffff },      # RIPE NCC
                    { 'start':0x56000000, 'end':0x56ffffff },      # RIPE NCC
                    { 'start':0x57000000, 'end':0x57ffffff },      # RIPE NCC
                    { 'start':0x58000000, 'end':0x58ffffff },      # RIPE NCC
                    { 'start':0x59000000, 'end':0x59ffffff },      # RIPE NCC
                    { 'start':0x5a000000, 'end':0x5affffff },      # RIPE NCC
                    { 'start':0x5b000000, 'end':0x5bffffff },      # RIPE NCC
                    { 'start':0x5c000000, 'end':0x5cffffff },      # RIPE NCC
                    { 'start':0x5d000000, 'end':0x5dffffff },      # RIPE NCC
                    { 'start':0x5e000000, 'end':0x5effffff },      # RIPE NCC
                    { 'start':0x5f000000, 'end':0x5fffffff },      # RIPE NCC
                    { 'start':0x60000000, 'end':0x60ffffff },      # ARIN
                    { 'start':0x61000000, 'end':0x61ffffff },      # ARIN
                    { 'start':0x62000000, 'end':0x62ffffff },      # ARIN
                    { 'start':0x63000000, 'end':0x63ffffff },      # ARIN
                    { 'start':0x64000000, 'end':0x64ffffff },      # ARIN
                    { 'start':0x65000000, 'end':0x65ffffff },      # APNIC
                    { 'start':0x66000000, 'end':0x66ffffff },      # AFRINIC norts
                    { 'start':0x67000000, 'end':0x67ffffff },      # APNIC
                    { 'start':0x68000000, 'end':0x68ffffff },      # ARIN
                    { 'start':0x69000000, 'end':0x69ffffff },      # AFRINIC 
                    { 'start':0x6a000000, 'end':0x6affffff },      # APNIC 
                    { 'start':0x6b000000, 'end':0x6bffffff },      # ARIN 
                    { 'start':0x6c000000, 'end':0x6cffffff },      # ARIN 
                    { 'start':0x6d000000, 'end':0x6dffffff },      # RIPE NCC 
                    { 'start':0x6e000000, 'end':0x6effffff },      # APNIC 
                    { 'start':0x6f000000, 'end':0x6fffffff },      # APNIC 
                    { 'start':0x70000000, 'end':0x70ffffff },      # APNIC 
                    { 'start':0x71000000, 'end':0x71ffffff },      # APNIC 
                    { 'start':0x72000000, 'end':0x72ffffff },      # APNIC 
                    { 'start':0x73000000, 'end':0x73ffffff },      # APNIC 
                    { 'start':0x74000000, 'end':0x74ffffff },      # APNIC 
                    { 'start':0x75000000, 'end':0x75ffffff },      # APNIC 
                    { 'start':0x76000000, 'end':0x76ffffff },      # APNIC 
                    { 'start':0x77000000, 'end':0x77ffffff },      # APNIC 
                    { 'start':0x78000000, 'end':0x78ffffff },      # APNIC 
                    { 'start':0x79000000, 'end':0x79ffffff },      # APNIC 
                    { 'start':0x7a000000, 'end':0x7affffff },      # APNIC 
                    { 'start':0x7b000000, 'end':0x7bffffff },      # APNIC 
                    { 'start':0x7c000000, 'end':0x7cffffff },      # APNIC 
                    { 'start':0x7d000000, 'end':0x7dffffff },      # APNIC 
                    { 'start':0x7e000000, 'end':0x7effffff },      # APNIC 
# Loopbacks         { 'start':0x7f000000, 'end':0x7fffffff },
                    { 'start':0x80000000, 'end':0x80ffffff },      # ARIN 
                    { 'start':0x81000000, 'end':0x81ffffff },      # ARIN 
                    { 'start':0x82000000, 'end':0x82ffffff },      # ARIN 
                    { 'start':0x83000000, 'end':0x83ffffff },      # ARIN 
                    { 'start':0x84000000, 'end':0x84ffffff },      # ARIN 
                    { 'start':0x85000000, 'end':0x85ffffff },      # APNIC 
                    { 'start':0x86000000, 'end':0x86ffffff },      # ARIN 
                    { 'start':0x87000000, 'end':0x87ffffff },      # ARIN 
                    { 'start':0x88000000, 'end':0x88ffffff },      # ARIN 
                    { 'start':0x89000000, 'end':0x89ffffff },      # ARIN 
                    { 'start':0x8a000000, 'end':0x8affffff },      # ARIN 
                    { 'start':0x8b000000, 'end':0x8bffffff },      # ARIN 
                    { 'start':0x8c000000, 'end':0x8cffffff },      # ARIN 
                    { 'start':0x8d000000, 'end':0x8dffffff },      # RIPE NCC 
                    { 'start':0x8e000000, 'end':0x8effffff },      # ARIN 
                    { 'start':0x8f000000, 'end':0x8fffffff },      # ARIN 
                    { 'start':0x90000000, 'end':0x90ffffff },      # ARIN 
                    { 'start':0x91000000, 'end':0x91ffffff },      # RIPE NCC 
                    { 'start':0x92000000, 'end':0x92ffffff },      # ARIN 
                    { 'start':0x93000000, 'end':0x93ffffff },      # ARIN 
                    { 'start':0x94000000, 'end':0x94ffffff },      # ARIN 
                    { 'start':0x95000000, 'end':0x95ffffff },      # ARIN 
                    { 'start':0x96000000, 'end':0x96ffffff },      # APNIC 
                    { 'start':0x97000000, 'end':0x97ffffff },      # RIPE NCC 
                    { 'start':0x98000000, 'end':0x98ffffff },      # ARIN 
                    { 'start':0x99000000, 'end':0x99ffffff },      # APNIC 
                    { 'start':0x9a000000, 'end':0x9affffff },      # AFRINIC 
                    { 'start':0x9b000000, 'end':0x9bffffff },      # ARIN 
                    { 'start':0x9c000000, 'end':0x9cffffff },      # ARIN 
                    { 'start':0x9d000000, 'end':0x9dffffff },      # ARIN 
                    { 'start':0x9e000000, 'end':0x9effffff },      # ARIN 
                    { 'start':0x9f000000, 'end':0x9fffffff },      # ARIN 
                    { 'start':0xa0000000, 'end':0xa0ffffff },      # ARIN 
                    { 'start':0xa1000000, 'end':0xa1ffffff },      # ARIN 
                    { 'start':0xa2000000, 'end':0xa2ffffff },      # ARIN 
                    { 'start':0xa3000000, 'end':0xa3ffffff },      # APNIC 
                    { 'start':0xa4000000, 'end':0xa4ffffff },      # ARIN 
                    { 'start':0xa5000000, 'end':0xa5ffffff },      # ARIN 
                    { 'start':0xa6000000, 'end':0xa6ffffff },      # ARIN 
                    { 'start':0xa7000000, 'end':0xa7ffffff },      # ARIN 
                    { 'start':0xa8000000, 'end':0xa8ffffff },      # ARIN 
                    { 'start':0xa9000000, 'end':0xa9ffffff },      # ARIN 
                    { 'start':0xaa000000, 'end':0xaaffffff },      # ARIN 
                    { 'start':0xab000000, 'end':0xabffffff },      # APNIC 
                    { 'start':0xac000000, 'end':0xacffffff },      # ARIN 
                    { 'start':0xad000000, 'end':0xadffffff },      # ARIN 
                    { 'start':0xae000000, 'end':0xaeffffff },      # ARIN 
                    { 'start':0xaf000000, 'end':0xafffffff },      # APNIC 
                    { 'start':0xb0000000, 'end':0xb0ffffff },      # RIPE NCC 
                    { 'start':0xb1000000, 'end':0xb1ffffff },      # LACNIC 
                    { 'start':0xb2000000, 'end':0xb2ffffff },      # RIPE NCC 
                    { 'start':0xb3000000, 'end':0xb3ffffff },      # LACNIC 
                    { 'start':0xb4000000, 'end':0xb4ffffff },      # APNIC 
                    { 'start':0xb5000000, 'end':0xb5ffffff },      # LACNIC 
                    { 'start':0xb6000000, 'end':0xb6ffffff },      # APNIC 
                    { 'start':0xb7000000, 'end':0xb7ffffff },      # APNIC 
                    { 'start':0xb8000000, 'end':0xb8ffffff },      # ARIN
                    { 'start':0xb9000000, 'end':0xb9ffffff },      # RIPE NCC 
                    { 'start':0xba000000, 'end':0xbaffffff },      # LACNIC 
                    { 'start':0xbb000000, 'end':0xbbffffff },      # LACNIC 
                    { 'start':0xbc000000, 'end':0xbcffffff },      # Admin RIPE NCC 
                    { 'start':0xbd000000, 'end':0xbdffffff },      # LACNIC 
                    { 'start':0xbe000000, 'end':0xbeffffff },      # LACNIC 
                    { 'start':0xbf000000, 'end':0xbfffffff },      # Admin LACNIC 
                    { 'start':0xc0000000, 'end':0xc0ffffff },      # Admin ARIN 
                    { 'start':0xc1000000, 'end':0xc1ffffff },      # RIPE NCC 
                    { 'start':0xc2000000, 'end':0xc2ffffff },      # RIPE NCC
                    { 'start':0xc3000000, 'end':0xc3ffffff },      # RIPE NCC
                    { 'start':0xc4000000, 'end':0xc4ffffff },      # Admin AFRINIC
                    { 'start':0xc5000000, 'end':0xc5ffffff },      # AFRINIC
                    { 'start':0xc6000000, 'end':0xc6ffffff },      # Admin ARIN
                    { 'start':0xc7000000, 'end':0xc7ffffff },      # ARIN
                    { 'start':0xc8000000, 'end':0xc8ffffff },      # LACNIC
                    { 'start':0xc9000000, 'end':0xc9ffffff },      # LACNIC
                    { 'start':0xca000000, 'end':0xcaffffff },      # APNIC
                    { 'start':0xcb000000, 'end':0xcbffffff },      # APNIC
                    { 'start':0xcc000000, 'end':0xccffffff },      # ARIN
                    { 'start':0xcd000000, 'end':0xcdffffff },      # ARIN
                    { 'start':0xce000000, 'end':0xceffffff },      # ARIN
                    { 'start':0xcf000000, 'end':0xcfffffff },      # ARIN
                    { 'start':0xd0000000, 'end':0xd0ffffff },      # ARIN
                    { 'start':0xd1000000, 'end':0xd1ffffff },      # ARIN
                    { 'start':0xd2000000, 'end':0xd2ffffff },      # APNIC
                    { 'start':0xd3000000, 'end':0xd3ffffff },      # APNIC
                    { 'start':0xd4000000, 'end':0xd4ffffff },      # RIPE NCC
                    { 'start':0xd5000000, 'end':0xd5ffffff },      # RIPE NCC
                    { 'start':0xd6000000, 'end':0xd6ffffff },      # US-DOD
                    { 'start':0xd7000000, 'end':0xd7ffffff },      # US-DOD
                    { 'start':0xd8000000, 'end':0xd8ffffff },      # ARIN
                    { 'start':0xd9000000, 'end':0xd9ffffff },      # RIPE NCC
                    { 'start':0xda000000, 'end':0xdaffffff },      # APNIC
                    { 'start':0xdb000000, 'end':0xdbffffff },      # APNIC
                    { 'start':0xdc000000, 'end':0xdcffffff },      # APNIC
                    { 'start':0xdd000000, 'end':0xddffffff },      # APNIC
                    { 'start':0xde000000, 'end':0xdeffffff },      # APNIC
                    { 'start':0xdf000000, 'end':0xdfffffff },      # APNIC

                  ]

    ipv4_100 =    [ { 'start':0x64000000, 'end':0x643fffff },      # no RFC6598
                    { 'start':0x64800000, 'end':0x64bfffff },      # no RFC6598
                    { 'start':0x64c00000, 'end':0x64ffffff },      # no RFC6598
                  ]

    ipv4_172 =    [ { 'start':0xac000000, 'end':0xac0fffff },      # no RFC1918
                    { 'start':0xac200000, 'end':0xac2fffff },      # no RFC1918
                    { 'start':0xac300000, 'end':0xac3fffff },      # no RFC1918
                    { 'start':0xac400000, 'end':0xac4fffff },      # no RFC1918
                    { 'start':0xac500000, 'end':0xac5fffff },      # no RFC1918
                    { 'start':0xac600000, 'end':0xac6fffff },      # no RFC1918
                    { 'start':0xac700000, 'end':0xac7fffff },      # no RFC1918
                    { 'start':0xac800000, 'end':0xac8fffff },      # no RFC1918
                    { 'start':0xac900000, 'end':0xac9fffff },      # no RFC1918
                    { 'start':0xaca00000, 'end':0xacafffff },      # no RFC1918
                    { 'start':0xacb00000, 'end':0xacbfffff },      # no RFC1918
                    { 'start':0xacc00000, 'end':0xaccfffff },      # no RFC1918
                    { 'start':0xacd00000, 'end':0xacdfffff },      # no RFC1918
                    { 'start':0xace00000, 'end':0xacefffff },      # no RFC1918
                    { 'start':0xacf00000, 'end':0xacffffff },      # no RFC1918
                  ]

    ipv4_192 =    [ { 'start':0xc0000000, 'end':0xc07fffff },      # no RFC1918
                    { 'start':0xc0800000, 'end':0xc0ffffff },      # no RFC1918
                  ]

    def get_169(self):
        start = 0xa9000000
        end = 0xa900ffff
        ipv4_169 = [ { 'start':start, 'end':end } ]
        while (True):
           start += 0x10000
           end += 0x10000
           if ( start == 0xa9fe0000 ):
               continue 
           else:
               ipv4_169.append({ 'start':start, 'end':end })
           if ( start == 0xa9ff0000 ):
               break
        return ipv4_169

    def get_192(self,start):
        if (start == 0xc0000000 ):
            start = 0xc0000100
            end = 0xc00001ff
            addr_192 = [ { 'start':start, 'end':end } ]
            while (True):
                start += 0x100
                end += 0x100
                if ( start == 0xc0000200 ):
                    continue
                elif ( start == 0xc0586300):
                    continue
                else:
                    addr_192.append({ 'start':start, 'end':end })
                if ( start == 0xc07fff00 ):
                    break
            return addr_192
        else:
            start = 0xc0800000
            end = 0xc080ffff
            addr_192 = [ { 'start':start, 'end':end } ]
            while (True):
                start += 0x10000
                end += 0x10000
                if ( start == 0xc0a80000):
                    continue
                else:
                    addr_192.append({ 'start':start, 'end':end })
                if ( start == 0xc0ff0000 ):
                    break
            return addr_192

