#Topology Substation 13-10-11
#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Node, Controller, RemoteController, OVSSwitch, OVSKernelSwitch, Host
from mininet.cli import CLI
from mininet.link import Intf, TCLink
from mininet.log import setLogLevel, info
from mininet.node import Node, CPULimitedHost
from mininet.util import irange,dumpNodeConnections
import time
import os



class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."

    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()

def emptyNet():

    NODE2_IP='192.168.56.1'
    CONTROLLER_IP='127.0.0.1'

    net = Mininet( topo=None,
                   build=False)

    #c0 = net.addController( 'c0',controller=RemoteController,ip=CONTROLLER_IP,port=6633)
    net.addController('c0', port=6633)

    r0 = net.addHost('r0', cls=LinuxRouter, ip='100.0.0.1/16')
    r1 = net.addHost('r1', cls=LinuxRouter, ip='100.1.0.1/16')
    r2 = net.addHost('r2', cls=LinuxRouter, ip='100.2.0.1/16')
    r12 = net.addHost('r12', cls=LinuxRouter, ip='100.12.0.1/16')
    r20 = net.addHost('r20', cls=LinuxRouter, ip='100.20.0.1/16')


    #Switch External Gateway
    s777 = net.addSwitch( 's777' )

    #Switch on Control Center
    s999 = net.addSwitch( 's999' )

    #Switch on Substation
    s11 = net.addSwitch( 's11' )
    s12 = net.addSwitch( 's12' )
    s13 = net.addSwitch( 's13' )
    s21 = net.addSwitch( 's21' )
    s22 = net.addSwitch( 's22' )
    s23 = net.addSwitch( 's23' )
    s121 = net.addSwitch( 's121' )
    s122 = net.addSwitch( 's122' )
    s123 = net.addSwitch( 's123' )
    s201 = net.addSwitch( 's201' )
    s202 = net.addSwitch( 's202' )
    s203 = net.addSwitch( 's203' )

    # Add host-switch links in the same subnet
    net.addLink(s999, r0, intfName2='r0-eth1', params2={'ip': '100.0.0.1/16'})
    net.addLink(s11, r1, intfName2='r1-eth1', params2={'ip': '100.1.0.1/16'})
    net.addLink(s21, r2, intfName2='r2-eth1', params2={'ip': '100.2.0.1/16'})
    net.addLink(s121, r12, intfName2='r12-eth1', params2={'ip': '100.12.0.1/16'})
    net.addLink(s201, r20, intfName2='r20-eth1', params2={'ip': '100.20.0.1/16'})

     # Add router-router link in a new subnet for the router-router connection
    net.addLink(r0, r1, intfName1='r0-eth2', intfName2='r1-eth2', params1={'ip': '200.1.0.1/24'}, params2={'ip': '200.1.0.2/24'})
    net.addLink(r0, r2, intfName1='r0-eth3', intfName2='r2-eth2', params1={'ip': '200.2.0.1/24'}, params2={'ip': '200.2.0.2/24'})
    net.addLink(r0, r12, intfName1='r0-eth4', intfName2='r12-eth2', params1={'ip': '200.12.0.1/24'}, params2={'ip': '200.12.0.2/24'})
    net.addLink(r0, r20, intfName1='r0-eth5', intfName2='r20-eth2', params1={'ip': '200.20.0.1/24'}, params2={'ip': '200.20.0.2/24'})

    #Add Host on Control Center
    ccdb = net.addHost('ccdb', ip='100.0.0.11')
    cctl = net.addHost('cctl', ip='100.0.0.12')

    #Add Hosts on Substation 1
    s01m1 = net.addHost('s01m1', ip='100.1.0.11', cls=CPULimitedHost, cpu=.1)
    s01m2 = net.addHost('s01m2', ip='100.1.0.12', cls=CPULimitedHost, cpu=.1)
    s01m3 = net.addHost('s01m3', ip='100.1.0.13', cls=CPULimitedHost, cpu=.1)
    s01m4 = net.addHost('s01m4', ip='100.1.0.14', cls=CPULimitedHost, cpu=.1)
    s01m5 = net.addHost('s01m5', ip='100.1.0.15', cls=CPULimitedHost, cpu=.1)
    s01m6 = net.addHost('s01m6', ip='100.1.0.16', cls=CPULimitedHost, cpu=.1)
    s01cpc = net.addHost('s01cpc', ip='100.1.0.21')
    s01db = net.addHost('s01db', ip='100.1.0.22')
    s01gw = net.addHost('s01gw', ip='100.1.0.23')

    #Add Hosts on Substation 2
    s02m1 = net.addHost('s02m1', ip='100.2.0.11', cls=CPULimitedHost, cpu=.1)
    s02m2 = net.addHost('s02m2', ip='100.2.0.12', cls=CPULimitedHost, cpu=.1)
    s02m3 = net.addHost('s02m3', ip='100.2.0.13', cls=CPULimitedHost, cpu=.1)
    s02m4 = net.addHost('s02m4', ip='100.2.0.14', cls=CPULimitedHost, cpu=.1)
    s02m5 = net.addHost('s02m5', ip='100.2.0.15', cls=CPULimitedHost, cpu=.1)
    s02m6 = net.addHost('s02m6', ip='100.2.0.16', cls=CPULimitedHost, cpu=.1)
    s02cpc = net.addHost('s02cpc', ip='100.2.0.21')
    s02db = net.addHost('s02db', ip='100.2.0.22')
    s02gw = net.addHost('s02gw', ip='100.2.0.23')

    #Add Hosts on Substation 12
    s12m1 = net.addHost('s12m1', ip='100.12.0.11', cls=CPULimitedHost, cpu=.1)
    s12m2 = net.addHost('s12m2', ip='100.12.0.12', cls=CPULimitedHost, cpu=.1)
    s12m3 = net.addHost('s12m3', ip='100.12.0.13', cls=CPULimitedHost, cpu=.1)
    s12m4 = net.addHost('s12m4', ip='100.12.0.14', cls=CPULimitedHost, cpu=.1)
    s12m5 = net.addHost('s12m5', ip='100.12.0.15', cls=CPULimitedHost, cpu=.1)
    s12m6 = net.addHost('s12m6', ip='100.12.0.16', cls=CPULimitedHost, cpu=.1)
    s12cpc = net.addHost('s12cpc', ip='100.12.0.21')
    s12db = net.addHost('s12db', ip='100.12.0.22')
    s12gw = net.addHost('s12gw', ip='100.12.0.23')

    #Add Hosts on Substation 20
    s20m1 = net.addHost('s20m1', ip='100.20.0.11', cls=CPULimitedHost, cpu=.1)
    s20m2 = net.addHost('s20m2', ip='100.20.0.12', cls=CPULimitedHost, cpu=.1)
    s20m3 = net.addHost('s20m3', ip='100.20.0.13', cls=CPULimitedHost, cpu=.1)
    s20m4 = net.addHost('s20m4', ip='100.20.0.14', cls=CPULimitedHost, cpu=.1)
    s20m5 = net.addHost('s20m5', ip='100.20.0.15', cls=CPULimitedHost, cpu=.1)
    s20m6 = net.addHost('s20m6', ip='100.20.0.16', cls=CPULimitedHost, cpu=.1)
    s20cpc = net.addHost('s20cpc', ip='100.20.0.21')
    s20db = net.addHost('s20db', ip='100.20.0.22')
    s20gw = net.addHost('s20gw', ip='100.20.0.23')


    # Link siwtch to switch
    net.addLink(s11,s12)
    net.addLink(s13,s12)
    net.addLink(s21,s22)
    net.addLink(s23,s22)
    net.addLink(s121,s122)
    net.addLink(s123,s122)
    net.addLink(s201,s202)
    net.addLink(s203,s202)

    # Link Control Center to Switch
    net.addLink(ccdb,s999, intfName1='ccdb-eth1', params1={'ip':'100.0.0.11/24'})
    net.addLink(cctl,s999, intfName1='cctl-eth1', params1={'ip':'100.0.0.12/24'})

    # Link Substation 1 Merging unit to Switch
    net.addLink(s01m1,s13, intfName1='s01m1-eth1', params1={'ip':'100.1.0.11/24'})
    net.addLink(s01m2,s13, intfName1='s01m2-eth1', params1={'ip':'100.1.0.12/24'})
    net.addLink(s01m3,s13, intfName1='s01m3-eth1', params1={'ip':'100.1.0.13/24'})
    net.addLink(s01m4,s13, intfName1='s01m4-eth1', params1={'ip':'100.1.0.14/24'})
    net.addLink(s01m5,s13, intfName1='s01m5-eth1', params1={'ip':'100.1.0.15/24'})
    net.addLink(s01m6,s13, intfName1='s01m6-eth1', params1={'ip':'100.1.0.16/24'}) 
    net.addLink(s01cpc,s12)
    net.addLink(s01db,s12)
    net.addLink(s01gw,s11, intfName1='s01gw-eth1', params1={'ip':'100.1.0.23/24'})

    # Link Substation 2 Merging unit to Switch
    net.addLink(s02m1,s23, intfName1='s02m1-eth1', params1={'ip':'100.2.0.11/24'})
    net.addLink(s02m2,s23, intfName1='s02m2-eth1', params1={'ip':'100.2.0.12/24'})
    net.addLink(s02m3,s23, intfName1='s02m3-eth1', params1={'ip':'100.2.0.13/24'})
    net.addLink(s02m4,s23, intfName1='s02m4-eth1', params1={'ip':'100.2.0.14/24'})
    net.addLink(s02m5,s23, intfName1='s02m5-eth1', params1={'ip':'100.2.0.15/24'})
    net.addLink(s02m6,s23, intfName1='s02m6-eth1', params1={'ip':'100.2.0.16/24'}) 
    net.addLink(s02cpc,s22)
    net.addLink(s02db,s22)
    net.addLink(s02gw,s21, intfName1='s02gw-eth1', params1={'ip':'100.2.0.23/24'})

    # Link Substation 12 Merging unit to Switch
    net.addLink(s12m1,s123, intfName1='s12m1-eth1', params1={'ip':'100.12.0.11/24'})
    net.addLink(s12m2,s123, intfName1='s12m2-eth1', params1={'ip':'100.12.0.12/24'})
    net.addLink(s12m3,s123, intfName1='s12m3-eth1', params1={'ip':'100.12.0.13/24'})
    net.addLink(s12m4,s123, intfName1='s12m4-eth1', params1={'ip':'100.12.0.14/24'})
    net.addLink(s12m5,s123, intfName1='s12m5-eth1', params1={'ip':'100.12.0.15/24'})
    net.addLink(s12m6,s123, intfName1='s12m6-eth1', params1={'ip':'100.12.0.16/24'}) 
    net.addLink(s12cpc,s122)
    net.addLink(s12db,s122)
    net.addLink(s12gw,s121, intfName1='s12gw-eth1', params1={'ip':'100.12.0.23/24'})

    # Link Substation 2 Merging unit to Switch
    net.addLink(s20m1,s203, intfName1='s20m1-eth1', params1={'ip':'100.20.0.11/24'})
    net.addLink(s20m2,s203, intfName1='s20m2-eth1', params1={'ip':'100.20.0.12/24'})
    net.addLink(s20m3,s203, intfName1='s20m3-eth1', params1={'ip':'100.20.0.13/24'})
    net.addLink(s20m4,s203, intfName1='s20m4-eth1', params1={'ip':'100.20.0.14/24'})
    net.addLink(s20m5,s203, intfName1='s20m5-eth1', params1={'ip':'100.20.0.15/24'})
    net.addLink(s20m6,s203, intfName1='s20m6-eth1', params1={'ip':'100.20.0.16/24'}) 
    net.addLink(s20cpc,s202)
    net.addLink(s20db,s202)
    net.addLink(s20gw,s201, intfName1='s20gw-eth1', params1={'ip':'100.20.0.23/24'})

    # Link Host Control Center to External gateway
    net.addLink(ccdb,s777, intfName1='ccdb-eth0', params1={'ip':'10.0.0.11/16'})
    net.addLink(cctl,s777, intfName1='cctl-eth0', params1={'ip':'10.0.0.12/16'})

    # Link Host Substation 1 to switch to external gateway
    net.addLink(s01m1,s777, intfName1='s01m1-eth0', params1={'ip':'10.0.1.11/16'})
    net.addLink(s01m2,s777, intfName1='s01m2-eth0', params1={'ip':'10.0.1.12/16'})
    net.addLink(s01m3,s777, intfName1='s01m3-eth0', params1={'ip':'10.0.1.13/16'})
    net.addLink(s01m4,s777, intfName1='s01m4-eth0', params1={'ip':'10.0.1.14/16'})
    net.addLink(s01m5,s777, intfName1='s01m5-eth0', params1={'ip':'10.0.1.15/16'})
    net.addLink(s01m6,s777, intfName1='s01m6-eth0', params1={'ip':'10.0.1.16/16'})
    net.addLink(s01gw,s777, intfName1='s01gw-eth0', params1={'ip':'10.0.1.23/16'})

    # Link Host Substation 2 to switch to external gateway
    net.addLink(s02m1,s777, intfName1='s02m1-eth0', params1={'ip':'10.0.2.11/16'})
    net.addLink(s02m2,s777, intfName1='s02m2-eth0', params1={'ip':'10.0.2.12/16'})
    net.addLink(s02m3,s777, intfName1='s02m3-eth0', params1={'ip':'10.0.2.13/16'})
    net.addLink(s02m4,s777, intfName1='s02m4-eth0', params1={'ip':'10.0.2.14/16'})
    net.addLink(s02m5,s777, intfName1='s02m5-eth0', params1={'ip':'10.0.2.15/16'})
    net.addLink(s02m6,s777, intfName1='s02m6-eth0', params1={'ip':'10.0.2.16/16'})
    net.addLink(s02gw,s777, intfName1='s02gw-eth0', params1={'ip':'10.0.2.23/16'})

    # Link Host Substation 12 to switch to external gateway
    net.addLink(s12m1,s777, intfName1='s12m1-eth0', params1={'ip':'10.0.12.11/16'})
    net.addLink(s12m2,s777, intfName1='s12m2-eth0', params1={'ip':'10.0.12.12/16'})
    net.addLink(s12m3,s777, intfName1='s12m3-eth0', params1={'ip':'10.0.12.13/16'})
    net.addLink(s12m4,s777, intfName1='s12m4-eth0', params1={'ip':'10.0.12.14/16'})
    net.addLink(s12m5,s777, intfName1='s12m5-eth0', params1={'ip':'10.0.12.15/16'})
    net.addLink(s12m6,s777, intfName1='s12m6-eth0', params1={'ip':'10.0.12.16/16'})
    net.addLink(s12gw,s777, intfName1='s12gw-eth0', params1={'ip':'10.0.12.23/16'})

    # Link Host Substation 20 to switch to external gateway
    net.addLink(s20m1,s777, intfName1='s20m1-eth0', params1={'ip':'10.0.20.11/16'})
    net.addLink(s20m2,s777, intfName1='s20m2-eth0', params1={'ip':'10.0.20.12/16'})
    net.addLink(s20m3,s777, intfName1='s20m3-eth0', params1={'ip':'10.0.20.13/16'})
    net.addLink(s20m4,s777, intfName1='s20m4-eth0', params1={'ip':'10.0.20.14/16'})
    net.addLink(s20m5,s777, intfName1='s20m5-eth0', params1={'ip':'10.0.20.15/16'})
    net.addLink(s20m6,s777, intfName1='s20m6-eth0', params1={'ip':'10.0.20.16/16'})
    net.addLink(s20gw,s777, intfName1='s20gw-eth0', params1={'ip':'10.0.20.23/16'})

    #Build and start Network ============================================================================
    net.build()
    net.addNAT(ip='10.0.0.250').configDefault()
    net.start()

    #Configure GRE Tunnel
    #s777.cmdPrint('ovs-vsctl add-port s777 s777-gre1 -- set interface s777-gre1 type=gre ofport_request=5 options:remote_ip='+NODE2_IP)
    #s777.cmdPrint('ovs-vsctl show')
    nat = net.get('nat0')
    nat.cmdPrint('ip link set mtu 1454 dev nat0-eth0')

    # Add routing for reaching networks that aren't directly connected
    info( net[ 'r0' ].cmd( 'ip route add 100.1.0.0/24 via 200.1.0.2 dev r0-eth2' ) )
    info( net[ 'r1' ].cmd( 'ip route add 100.0.0.0/24 via 200.1.0.1 dev r1-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.2.0.0/24 via 200.2.0.2 dev r0-eth3' ) )
    info( net[ 'r2' ].cmd( 'ip route add 100.0.0.0/24 via 200.2.0.1 dev r2-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.12.0.0/24 via 200.12.0.2 dev r0-eth4' ) )
    info( net[ 'r12' ].cmd( 'ip route add 100.0.0.0/24 via 200.12.0.1 dev r12-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.20.0.0/24 via 200.20.0.2 dev r0-eth5' ) )
    info( net[ 'r20' ].cmd( 'ip route add 100.0.0.0/24 via 200.20.0.1 dev r20-eth2' ) )

    info( net[ 's01m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.1.0.1 dev s01m1-eth1' ) )
    info( net[ 's01m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.1.0.1 dev s01m2-eth1' ) )
    info( net[ 's01m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.1.0.1 dev s01m3-eth1' ) )
    info( net[ 's01m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.1.0.1 dev s01m4-eth1' ) )
    info( net[ 's01m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.1.0.1 dev s01m5-eth1' ) )
    info( net[ 's01m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.1.0.1 dev s01m6-eth1' ) )

    info( net[ 's02m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.2.0.1 dev s02m1-eth1' ) )
    info( net[ 's02m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.2.0.1 dev s02m2-eth1' ) )
    info( net[ 's02m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.2.0.1 dev s02m3-eth1' ) )
    info( net[ 's02m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.2.0.1 dev s02m4-eth1' ) )
    info( net[ 's02m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.2.0.1 dev s02m5-eth1' ) )
    info( net[ 's02m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.2.0.1 dev s02m6-eth1' ) )

    info( net[ 's12m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.12.0.1 dev s12m1-eth1' ) )
    info( net[ 's12m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.12.0.1 dev s12m2-eth1' ) )
    info( net[ 's12m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.12.0.1 dev s12m3-eth1' ) )
    info( net[ 's12m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.12.0.1 dev s12m4-eth1' ) )
    info( net[ 's12m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.12.0.1 dev s12m5-eth1' ) )
    info( net[ 's12m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.12.0.1 dev s12m6-eth1' ) )

    info( net[ 's20m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.20.0.1 dev s20m1-eth1' ) )
    info( net[ 's20m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.20.0.1 dev s20m2-eth1' ) )
    info( net[ 's20m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.20.0.1 dev s20m3-eth1' ) )
    info( net[ 's20m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.20.0.1 dev s20m4-eth1' ) )
    info( net[ 's20m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.20.0.1 dev s20m5-eth1' ) )
    info( net[ 's20m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.20.0.1 dev s20m6-eth1' ) )
    
    info( net[ 'ccdb' ].cmd( 'ip route add 100.1.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.2.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.12.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.20.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )

    info( net[ 'cctl' ].cmd( 'ip route add 100.1.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.2.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.12.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.20.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    
    info(os.system('ip addr add 100.0.0.99/24 dev s999'))
    info(os.system('ip link set s999 up'))

    #time.sleep(5)

    #info( net[ 's06db' ].cmd( 'python3 ascdb.py &amp' ) )


    CLI( net )
    net.stop()



if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()