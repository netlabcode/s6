#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Node, Controller, RemoteController, OVSSwitch, OVSKernelSwitch, Host
from mininet.cli import CLI
from mininet.link import Intf, TCLink
from mininet.log import setLogLevel, info


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

    # Add 2 routers in two different subnets
    r0 = net.addHost('r0', cls=LinuxRouter, ip='150.0.0.1/24')
    r1 = net.addHost('r1', cls=LinuxRouter, ip='100.1.0.1/24')
    r2 = net.addHost('r2', cls=LinuxRouter, ip='100.2.0.1/24')

    x1 = net.addHost('x1')
    x2 = net.addHost('x2')
    x3 = net.addHost('x3')

    y1 = net.addHost( 'y1', ip='100.1.0.11' )
    y2 = net.addHost( 'y2', ip='150.0.0.12' )
    y3 = net.addHost( 'y3', ip='100.2.0.11' )

    s1 = net.addSwitch( 's1' )

    s11 = net.addSwitch( 's11' )
    s12 = net.addSwitch( 's12' )
    s13 = net.addSwitch( 's13' )
    s14 = net.addSwitch( 's14' )

    s21 = net.addSwitch( 's21' )


    # Add host-switch links in the same subnet
    net.addLink(s14, r0, intfName2='r0-eth1', params2={'ip': '150.0.0.1/24'})

    net.addLink(s13, r1, intfName2='r1-eth1', params2={'ip': '100.1.0.1/24'})

    net.addLink(s21, r2, intfName2='r2-eth1', params2={'ip': '100.2.0.1/24'})

    # Add router-router link in a new subnet for the router-router connection
    net.addLink(r0, r1, intfName1='r0-eth2', intfName2='r1-eth2', params1={'ip': '200.0.0.1/24'}, params2={'ip': '200.0.0.2/24'})

    net.addLink(r0, r2, intfName1='r0-eth3', intfName2='r2-eth2', params1={'ip': '200.2.0.1/24'}, params2={'ip': '200.2.0.2/24'})


    net.addLink( s11,s12 )
    net.addLink( s12,s13 )
    #net.addLink( s13,s14 )

    net.addLink( y1, s12)
    net.addLink( y2, s14)

    net.addLink( y3, s21)

    net.addLink(s1, x1, intfName2='x1-eth1', params2={'ip': '10.0.0.3/24'})
    net.addLink(s1, x2, intfName2='x2-eth1', params2={'ip': '10.0.0.4/24'})
    net.addLink(s1, x3, intfName2='x3-eth1', params2={'ip': '10.0.0.5/24'})

    net.addLink(s11, x1, intfName2='x1-eth2', params2={'ip': '100.1.0.2/24'})
    net.addLink(s14, x2, intfName2='x2-eth2', params2={'ip': '150.0.0.2/24'})
    net.addLink(s21, x3, intfName2='x3-eth2', params2={'ip': '100.2.0.2/24'})




    net.build()
    net.addNAT(ip='10.0.0.250').configDefault()
    net.start()

    # Configure the GRE tunnel
    s1.cmdPrint('ovs-vsctl add-port s1 s1-gre1 -- set interface s1-gre1 type=gre ofport_request=5 options:remote_ip='+NODE2_IP)
    s1.cmdPrint('ovs-vsctl show')

    x1.cmdPrint('ip link set mtu 1454 dev x1-eth1')
    x2.cmdPrint('ip link set mtu 1454 dev x2-eth1')
    x3.cmdPrint('ip link set mtu 1454 dev x3-eth1')

    nat = net.get('nat0')
    nat.cmdPrint('ip link set mtu 1454 dev nat0-eth0')

    r0.cmdPrint('ip route add 100.1.0.0/24 via 200.0.0.2 dev r0-eth2')
    r0.cmdPrint('ip route add 100.2.0.0/24 via 200.2.0.2 dev r0-eth3')
    r1.cmdPrint('ip route add 150.0.0.0/24 via 200.0.0.1 dev r1-eth2')
    r2.cmdPrint('ip route add 150.0.0.0/24 via 200.2.0.1 dev r2-eth2')

    y1.cmdPrint('ip route add 150.0.0.0/24 via 100.1.0.1 dev y1-eth0')
    y2.cmdPrint('ip route add 100.1.0.0/24 via 150.0.0.1 dev y2-eth0')
    y2.cmdPrint('ip route add 100.2.0.0/24 via 150.0.0.1 dev y2-eth0')
    y3.cmdPrint('ip route add 150.0.0.0/24 via 100.2.0.1 dev y3-eth0')

    x1.cmdPrint('ip route add 150.0.0.0/24 via 100.1.0.1 dev x1-eth2')
    x2.cmdPrint('ip route add 100.1.0.0/24 via 150.0.0.1 dev x2-eth2')
    x2.cmdPrint('ip route add 100.2.0.0/24 via 150.0.0.1 dev x2-eth2')
    x3.cmdPrint('ip route add 150.0.0.0/24 via 100.2.0.1 dev x3-eth2')
    


    CLI( net )
    net.stop()



if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()