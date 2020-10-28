#!/usr/bin/python

"""
linuxrouter.py: Example network with Linux IP router

This example converts a Node into a router using IP forwarding
already built into Linux.

The example topology creates a router and three IP subnets:

    - 192.168.1.0/24 (r0-eth1, IP: 192.168.1.1)
    - 172.16.0.0/12 (r0-eth2, IP: 172.16.0.1)
    - 10.0.0.0/8 (r0-eth3, IP: 10.0.0.1)

Each subnet consists of a single host connected to
a single switch:

    r0-eth1 - s1-eth1 - h1-eth0 (IP: 192.168.1.100)
    r0-eth2 - s2-eth1 - h2-eth0 (IP: 172.16.0.100)
    r0-eth3 - s3-eth1 - h3-eth0 (IP: 10.0.0.100)

The example relies on default routing entries that are
automatically created for each router interface, as well
as 'defaultRoute' parameters for the host interfaces.

Additional routes may be added to the router or hosts by
executing 'ip route' or 'route' commands on the router or hosts.
"""


from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node, CPULimitedHost
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.util import irange,dumpNodeConnections
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


class NetworkTopo( Topo ):
    "A LinuxRouter connecting three IP subnets"

    def build( self, **_opts ):

        # Add 2 routers in two different subnets
        r1 = self.addHost('r1', cls=LinuxRouter, ip='10.0.0.1/24')
        r2 = self.addHost('r2', cls=LinuxRouter, ip='10.1.0.1/24')

        # Add 2 switches
        #s1, s2, s3, scc = [self.addSwitch(s) for s in ('s1', 's2', 's3', 'scc')]
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )

        # Add host-switch links in the same subnet
        self.addLink(s4, r1, intfName2='r1-eth1',
                    params2={'ip': '10.0.0.1/24'})

        self.addLink(s3, r2, intfName2='r2-eth1',
                    params2={'ip': '10.1.0.1/24'})

        # Add router-router link in a new subnet for the router-router connection
        self.addLink(r1, r2, intfName1='r1-eth2', intfName2='r2-eth2',
                  params1={'ip': '10.100.0.1/24'}, params2={'ip': '10.100.0.2/24'})

        self.addLink( s2, s3 )
        self.addLink( s1, s2 )

        # Adding hosts specifying the default route
        cc = self.addHost(name='cc', ip='10.0.0.11/24', defaultRoute='via 10.0.0.1')
        dbc = self.addHost(name='dbc', ip='10.0.0.12/24', defaultRoute='via 10.0.0.1')

        m1 = self.addHost(name='m1', ip='10.1.0.11/24', defaultRoute='via 10.1.0.1', cls=CPULimitedHost, cpu=.1)
        m2 = self.addHost(name='m2', ip='10.1.0.12/24', defaultRoute='via 10.1.0.1', cls=CPULimitedHost, cpu=.1)
        m3 = self.addHost(name='m3', ip='10.1.0.13/24', defaultRoute='via 10.1.0.1', cls=CPULimitedHost, cpu=.1)
        m4 = self.addHost(name='m4', ip='10.1.0.14/24', defaultRoute='via 10.1.0.1', cls=CPULimitedHost, cpu=.1)
        m5 = self.addHost(name='m5', ip='10.1.0.15/24', defaultRoute='via 10.1.0.1', cls=CPULimitedHost, cpu=.1)
        m6 = self.addHost(name='m6', ip='10.1.0.16/24', defaultRoute='via 10.1.0.1', cls=CPULimitedHost, cpu=.1)
        sc1 = self.addHost(name='sc1', ip='10.1.0.21/24', defaultRoute='via 10.1.0.1')
        db1 = self.addHost(name='db1', ip='10.1.0.22/24', defaultRoute='via 10.1.0.1')
        gw1 = self.addHost(name='gw1', ip='10.1.0.31/24', defaultRoute='via 10.1.0.1')

        # Add host-switch links
        #for d, s in [(d1, s1), (d2, s2), (d3, s3)]:
        #    self.addLink(d, s)

        self.addLink( m1, s1, cls=TCLink, bw=0.1 )
        self.addLink( m2, s1, cls=TCLink, bw=0.1 )
        self.addLink( m3, s1, cls=TCLink, bw=0.1 )
        self.addLink( m4, s1, cls=TCLink, bw=0.1 )
        self.addLink( m5, s1, cls=TCLink, bw=0.1 )
        self.addLink( m6, s1, cls=TCLink, bw=0.1 )
        self.addLink( sc1, s2 )
        self.addLink( db1, s2 )
        self.addLink( gw1, s3 )

        self.addLink( cc, s4 )
        self.addLink( dbc, s4 )


def run():
    "Test linux router"
    topo = NetworkTopo()
    net = Mininet( topo=topo )  # controller is used by s1-s3
    net.start()
    info( '*** Routing Table on Router:\n' )
    # Add routing for reaching networks that aren't directly connected
    info( net[ 'r1' ].cmd( 'ip route add 10.1.0.0/24 via 10.100.0.2 dev r1-eth2' ) )
    info( net[ 'r2' ].cmd( 'ip route add 10.0.0.0/24 via 10.100.0.1 dev r2-eth2' ) )
    #r1.cmd("ip route add 10.1.0.0/24 via 10.100.0.2 dev r1-eth2")
    #r2.cmd("ip route add 10.0.0.0/24 via 10.100.0.1 dev r2-eth2")
    info( net[ 'r1' ].cmd( 'route' ) )
    info( net[ 'r2' ].cmd( 'route' ) )

    info(os.system('date'))
    info(os.system('ip addr add 10.1.0.99/24 dev s1'))
    info(os.system('ip link set s1 up'))
    
    #info( net[ 'm1' ].cmd( 'python3 mu1.py &amp' ) )
    #info( net[ 'm2' ].cmd( 'python3 mu2.py &amp' ) )
    #info( net[ 'm3' ].cmd( 'python3 hello.py' ) )
    
    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    run()
