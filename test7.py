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

    x1 = net.addHost('x1')
    x2 = net.addHost('x2')

    y1 = net.addHost( 'y1', ip='100.0.0.11' )
    y2 = net.addHost( 'y2', ip='100.0.0.12' )

    s1 = net.addSwitch( 's1' )

    s11 = net.addSwitch( 's11' )
    s12 = net.addSwitch( 's12' )
    s13 = net.addSwitch( 's13' )
    s14 = net.addSwitch( 's14' )


    net.addLink( s11,s12 )
    net.addLink( s12,s13 )
    net.addLink( s13,s14 )

    net.addLink( y1, s12)
    net.addLink( y2, s13)

    net.addLink(s1, x1, intfName2='x1-eth1', params2={'ip': '10.0.0.3/24'})
    net.addLink(s1, x2, intfName2='x2-eth1', params2={'ip': '10.0.0.4/24'})

    net.addLink(s11, x1, intfName2='x1-eth2', params2={'ip': '100.0.0.1/24'})
    net.addLink(s14, x2, intfName2='x2-eth2', params2={'ip': '100.0.0.2/24'})



    net.build()
    net.addNAT(ip='10.0.0.250').configDefault()
    net.start()
    #net.addNAT().configDefault()
    #s1.start([c0])
    #s1.cmdPrint('ovs-vsctl set bridge s1 protocols=OpenFlow13')
    # Configure the GRE tunnel
    s1.cmdPrint('ovs-vsctl add-port s1 s1-gre1 -- set interface s1-gre1 type=gre ofport_request=5 options:remote_ip='+NODE2_IP)
    s1.cmdPrint('ovs-vsctl show')
    #s1.cmdPrint('ovs-vsctl set bridge s1 protocols=OpenFlow13')
    #os.system('ovs-ofctl add-flow s1 eth_type=2048,ip_dst=10.0.1.3,action=output:5')
    #os.system('ovs-ofctl add-flow s1 eth_type=2048,ip_dst=10.0.1.4,action=output:5')
    #os.system('ovs-ofctl add-flow s1 eth_type=2054,ip_dst=10.0.1.3,action=output:5')
    #os.system('ovs-ofctl add-flow s1 eth_type=2054,ip_dst=10.0.1.4,action=output:5')

    x1.cmdPrint('ip link set mtu 1454 dev x1-eth1')
    x2.cmdPrint('ip link set mtu 1454 dev x2-eth1')

    nat = net.get('nat0')
    nat.cmdPrint('ip link set mtu 1454 dev nat0-eth0')
    #net.addNAT().configDefault()
    CLI( net )
    net.stop()



if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()