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

    NODE2_IP='131.180.165.16'
    CONTROLLER_IP='127.0.0.1'

    net = Mininet( topo=None,
                   build=False)

    #c0 = net.addController( 'c0',controller=RemoteController,ip=CONTROLLER_IP,port=6633)
    net.addController('c0', port=6633)

     # Add Minndle Routers 
    r0 = net.addHost('r0', cls=LinuxRouter, ip='150.0.0.1/24')

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

    s61 = net.addSwitch( 's61' )
    s62 = net.addSwitch( 's62' )
    s63 = net.addSwitch( 's63' )


    #Add Host on Control Center
    ccctrl = net.addHost('ccctrl', ip='150.0.0.11')
    ccdb = net.addHost('ccdb', ip='150.0.0.12')

    #Add Host on Substation
    s01m1 = net.addHost('s01m1', ip='100.1.0.11')
    s01cpc = net.addHost('s01cpc', ip='100.1.0.21')

    s02m1 = net.addHost('s02m1', ip='100.2.0.11')
    s02cpc = net.addHost('s02cpc', ip='100.2.0.21')

    s06m1 = net.addHost('s06m1', ip='100.6.0.11')
    s06m2 = net.addHost('s06m2', ip='100.6.0.12')
    s06m3 = net.addHost('s06m3', ip='100.6.0.13')
    s06m4 = net.addHost('s06m4', ip='100.6.0.14')
    s06m5 = net.addHost('s06m5', ip='100.6.0.15')
    s06m6 = net.addHost('s06m6', ip='100.6.0.16')
    s06cpc = net.addHost('s06cpc', ip='100.6.0.21')



    # Link Switch To Router
    net.addLink(s999, r0, intfName2='r0-eth0', params2={'ip': '150.0.0.1/24'})
    net.addLink(s11, r0, intfName2='r0-eth1', params2={'ip': '100.1.0.1/24'})
    net.addLink(s21, r0, intfName2='r0-eth2', params2={'ip': '100.2.0.1/24'})
    net.addLink(s61, r0, intfName2='r0-eth6', params2={'ip': '100.6.0.1/24'})
    
    # Link siwtch to switch
    net.addLink(s11,s12)
    net.addLink(s13,s12)
    net.addLink(s21,s22)
    net.addLink(s23,s22)

    net.addLink(s61,s62)
    net.addLink(s63,s62)


    # Link Host to switch Control Center
    net.addLink(ccctrl,s999, intfName1='ccctrl-eth1', params1={'ip':'150.0.0.11/24'})
    net.addLink(ccdb,s999, intfName1='ccdb-eth1', params1={'ip':'150.0.0.12/24'})

    # Link Host to switch Subsatation
    net.addLink(s01m1,s13, intfName1='s01m1-eth1', params1={'ip':'100.1.0.11/24'})
    net.addLink(s02m1,s23, intfName1='s02m1-eth1', params1={'ip':'100.2.0.11/24'})

    net.addLink(s06m1,s63, intfName1='s06m1-eth1', params1={'ip':'100.6.0.11/24'})
    net.addLink(s06m2,s63, intfName1='s06m2-eth1', params1={'ip':'100.6.0.12/24'})
    net.addLink(s06m3,s63, intfName1='s06m3-eth1', params1={'ip':'100.6.0.13/24'})
    net.addLink(s06m4,s63, intfName1='s06m4-eth1', params1={'ip':'100.6.0.14/24'})
    net.addLink(s06m5,s63, intfName1='s06m5-eth1', params1={'ip':'100.6.0.15/24'})
    net.addLink(s06m6,s63, intfName1='s06m6-eth1', params1={'ip':'100.6.0.16/24'})    

    net.addLink(s01cpc,s12)
    net.addLink(s02cpc,s22)
    net.addLink(s06cpc,s62)


    # Link Host to switch to external gateway
    net.addLink(ccctrl,s777, intfName1='ccctrl-eth0', params1={'ip':'10.0.0.241/24'})
    net.addLink(ccdb,s777, intfName1='ccdb-eth0', params1={'ip':'10.0.0.242/24'})

    net.addLink(s01m1,s777, intfName1='s01m1-eth0', params1={'ip':'10.0.0.11/24'})
    net.addLink(s02m1,s777, intfName1='s02m1-eth0', params1={'ip':'10.0.0.21/24'})

    net.addLink(s06m1,s777, intfName1='s06m1-eth0', params1={'ip':'10.0.0.11/24'})
    net.addLink(s06m2,s777, intfName1='s06m2-eth0', params1={'ip':'10.0.0.12/24'})
    net.addLink(s06m3,s777, intfName1='s06m3-eth0', params1={'ip':'10.0.0.13/24'})
    net.addLink(s06m4,s777, intfName1='s06m4-eth0', params1={'ip':'10.0.0.14/24'})
    net.addLink(s06m5,s777, intfName1='s06m5-eth0', params1={'ip':'10.0.0.15/24'})
    net.addLink(s06m6,s777, intfName1='s06m6-eth0', params1={'ip':'10.0.0.16/24'})


    #Build and start Network ============================================================================
    net.build()
    net.addNAT(ip='10.0.0.250').configDefault()
    net.start()

    #Configure GRE Tunnel
    s777.cmdPrint('ovs-vsctl add-port s777 s777-gre1 -- set interface s777-gre1 type=gre ofport_request=5 options:remote_ip='+NODE2_IP)
    s777.cmdPrint('ovs-vsctl show')
    nat = net.get('nat0')
    nat.cmdPrint('ip link set mtu 1454 dev nat0-eth0')

    #Route Config Control Center to 27 Substation Flow
    r0.cmdPrint('ip route add 150.0.0.0/24 dev r0-eth0')
    r0.cmdPrint('ip route add 100.1.0.0/24 dev r0-eth1')
    r0.cmdPrint('ip route add 100.2.0.0/24 dev r0-eth2')

    r0.cmdPrint('ip route add 100.6.0.0/24 dev r0-eth6')


    #Gateway Config
    ccctrl.cmdPrint('ip route add 100.0.0.0/8 via 150.0.0.1 dev ccctrl-eth1')
    ccdb.cmdPrint('ip route add 100.0.0.0/8 via 150.0.0.1 dev ccdb-eth1')

    s01m1.cmdPrint('ip route add 150.0.0.0/8 via 100.1.0.1 dev s01m1-eth1')
    s02m1.cmdPrint('ip route add 150.0.0.0/8 via 100.2.0.1 dev s02m1-eth1')

    s06m1.cmdPrint('ip route add 150.0.0.0/8 via 100.6.0.1 dev s06m1-eth1')
    s06m2.cmdPrint('ip route add 150.0.0.0/8 via 100.6.0.1 dev s06m2-eth1')
    s06m3.cmdPrint('ip route add 150.0.0.0/8 via 100.6.0.1 dev s06m3-eth1')
    s06m4.cmdPrint('ip route add 150.0.0.0/8 via 100.6.0.1 dev s06m4-eth1')
    s06m5.cmdPrint('ip route add 150.0.0.0/8 via 100.6.0.1 dev s06m5-eth1')
    s06m6.cmdPrint('ip route add 150.0.0.0/8 via 100.6.0.1 dev s06m6-eth1')

    s01cpc.cmdPrint('ip route add 150.0.0.0/8 via 100.1.0.1 dev s01cpc-eth0')
    s02cpc.cmdPrint('ip route add 150.0.0.0/8 via 100.2.0.1 dev s02cpc-eth0')

    s06cpc.cmdPrint('ip route add 150.0.0.0/8 via 100.6.0.1 dev s06cpc-eth0')


    CLI( net )
    net.stop()



if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
