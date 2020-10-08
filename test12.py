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

     # Add Minndle Routers 
    r0 = net.addHost('r0', cls=LinuxRouter, ip='150.0.0.1/24')

    #Switch on Control Center
    s999 = net.addSwitch( 's999' )

    #Switch on Substation
    s11 = net.addSwitch( 's11' )
    s12 = net.addSwitch( 's12' )
    s13 = net.addSwitch( 's13' )

    s21 = net.addSwitch( 's21' )
    s22 = net.addSwitch( 's22' )
    s23 = net.addSwitch( 's23' )


    #Add Host on Control Center
    ccctrl = net.addHost('ccctrl', ip='150.0.0.11')
    ccdb = net.addHost('ccdb', ip='150.0.0.12')

    #Add Host on Substation
    s01m1 = net.addHost('s01m1', ip='100.1.0.11')
    s02m1 = net.addHost('s02m1', ip='100.2.0.11')



    # Link Switch To Router
    net.addLink(s999, r0, intfName2='r0-eth0', params2={'ip': '150.0.0.1/24'})
    net.addLink(s11, r0, intfName2='r0-eth1', params2={'ip': '100.1.0.1/24'})
    net.addLink(s21, r0, intfName2='r0-eth2', params2={'ip': '100.2.0.1/24'})
    
    # Link siwtch to switch
    net.addLink(s11,s12)
    net.addLink(s13,s12)
    net.addLink(s21,s22)
    net.addLink(s23,s22)


    # Link Host to switch Control Center
    net.addLink(ccctrl,s999, intfName1='ccctrl-eth1', params1={'ip':'150.0.0.11/24'})
    net.addLink(ccdb,s999, intfName1='ccdb-eth1', params1={'ip':'150.0.0.12/24'})

    # Link Host to switch Subsatation
    net.addLink(s01m1,s13, intfName1='s01m1-eth1', params1={'ip':'100.1.0.11/24'})
    net.addLink(s02m1,s23, intfName1='s02m1-eth1', params1={'ip':'100.2.0.11/24'})


    #Build and start Network ============================================================================
    net.build()
    net.start()

    #r0.cmdPrint('ip route flush table main')

    #Route Config Control Center to 27 Substation Flow
    r0.cmdPrint('ip route add 150.0.0.0/24 dev r0-eth0')
    r0.cmdPrint('ip route add 100.1.0.0/24 dev r0-eth1')
    r0.cmdPrint('ip route add 100.2.0.0/24 dev r0-eth2')


    #Gateway Config
    ccctrl.cmdPrint('ip route add 100.0.0.0/8 via 150.0.0.1 dev ccctrl-eth1')
    ccdb.cmdPrint('ip route add 100.0.0.0/8 via 150.0.0.1 dev ccdb-eth1')

    s01m1.cmdPrint('ip route add 150.0.0.0/8 via 100.1.0.1 dev s01m1-eth1')
    s02m1.cmdPrint('ip route add 150.0.0.0/8 via 100.2.0.1 dev s02m1-eth1')


    CLI( net )
    net.stop()



if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()