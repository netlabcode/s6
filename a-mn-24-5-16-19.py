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
    r5 = net.addHost('r5', cls=LinuxRouter, ip='100.5.0.1/16')
    r16 = net.addHost('r16', cls=LinuxRouter, ip='100.16.0.1/16')
    r19 = net.addHost('r19', cls=LinuxRouter, ip='100.19.0.1/16')
    r24 = net.addHost('r24', cls=LinuxRouter, ip='100.24.0.1/16')


    #Switch External Gateway
    s777 = net.addSwitch( 's777' )

    #Switch on Control Center
    s999 = net.addSwitch( 's999' )

    #Switch on Substation
    s51 = net.addSwitch( 's51' )
    s52 = net.addSwitch( 's52' )
    s53 = net.addSwitch( 's53' )
    s161 = net.addSwitch( 's161' )
    s162 = net.addSwitch( 's162' )
    s163 = net.addSwitch( 's163' )
    s191 = net.addSwitch( 's191' )
    s192 = net.addSwitch( 's192' )
    s193 = net.addSwitch( 's193' )
    s241 = net.addSwitch( 's241' )
    s242 = net.addSwitch( 's242' )
    s243 = net.addSwitch( 's243' )

    # Add host-switch links in the same subnet
    net.addLink(s999, r0, intfName2='r0-eth1', params2={'ip': '100.0.0.1/16'})
    net.addLink(s51, r5, intfName2='r5-eth1', params2={'ip': '100.5.0.1/16'})
    net.addLink(s161, r16, intfName2='r16-eth1', params2={'ip': '100.16.0.1/16'})
    net.addLink(s191, r19, intfName2='r19-eth1', params2={'ip': '100.19.0.1/16'})
    net.addLink(s241, r24, intfName2='r24-eth1', params2={'ip': '100.24.0.1/16'})

     # Add router-router link in a new subnet for the router-router connection
    net.addLink(r0, r5, intfName1='r0-eth2', intfName2='r5-eth2', params1={'ip': '200.5.0.1/24'}, params2={'ip': '200.5.0.2/24'})
    net.addLink(r0, r16, intfName1='r0-eth3', intfName2='r16-eth2', params1={'ip': '200.16.0.1/24'}, params2={'ip': '200.16.0.2/24'})
    net.addLink(r0, r19, intfName1='r0-eth4', intfName2='r19-eth2', params1={'ip': '200.19.0.1/24'}, params2={'ip': '200.19.0.2/24'})
    net.addLink(r0, r24, intfName1='r0-eth5', intfName2='r24-eth2', params1={'ip': '200.24.0.1/24'}, params2={'ip': '200.24.0.2/24'})

    #Add Host on Control Center
    ccdb = net.addHost('ccdb', ip='100.0.0.11')
    cctl = net.addHost('cctl', ip='100.0.0.12')

    #Add Hosts on Substation 5
    s05m1 = net.addHost('s05m1', ip='100.5.0.11', cls=CPULimitedHost, cpu=.1)
    s05m2 = net.addHost('s05m2', ip='100.5.0.12', cls=CPULimitedHost, cpu=.1)
    s05m3 = net.addHost('s05m3', ip='100.5.0.13', cls=CPULimitedHost, cpu=.1)
    s05m4 = net.addHost('s05m4', ip='100.5.0.14', cls=CPULimitedHost, cpu=.1)
    s05m5 = net.addHost('s05m5', ip='100.5.0.15', cls=CPULimitedHost, cpu=.1)
    s05m6 = net.addHost('s05m6', ip='100.5.0.16', cls=CPULimitedHost, cpu=.1)
    s05cpc = net.addHost('s05cpc', ip='100.5.0.21')
    s05db = net.addHost('s05db', ip='100.5.0.22')
    s05gw = net.addHost('s05gw', ip='100.5.0.23')

    #Add Hosts on Substation 16
    s16m1 = net.addHost('s16m1', ip='100.16.0.11', cls=CPULimitedHost, cpu=.1)
    s16m2 = net.addHost('s16m2', ip='100.16.0.12', cls=CPULimitedHost, cpu=.1)
    s16m3 = net.addHost('s16m3', ip='100.16.0.13', cls=CPULimitedHost, cpu=.1)
    s16m4 = net.addHost('s16m4', ip='100.16.0.14', cls=CPULimitedHost, cpu=.1)
    s16m5 = net.addHost('s16m5', ip='100.16.0.15', cls=CPULimitedHost, cpu=.1)
    s16m6 = net.addHost('s16m6', ip='100.16.0.16', cls=CPULimitedHost, cpu=.1)
    s16cpc = net.addHost('s16cpc', ip='100.16.0.21')
    s16db = net.addHost('s16db', ip='100.16.0.22')
    s16gw = net.addHost('s16gw', ip='100.16.0.23')

    #Add Hosts on Substation 19
    s19m1 = net.addHost('s19m1', ip='100.19.0.11', cls=CPULimitedHost, cpu=.1)
    s19m2 = net.addHost('s19m2', ip='100.19.0.12', cls=CPULimitedHost, cpu=.1)
    s19m3 = net.addHost('s19m3', ip='100.19.0.13', cls=CPULimitedHost, cpu=.1)
    s19m4 = net.addHost('s19m4', ip='100.19.0.14', cls=CPULimitedHost, cpu=.1)
    s19m5 = net.addHost('s19m5', ip='100.19.0.15', cls=CPULimitedHost, cpu=.1)
    s19m6 = net.addHost('s19m6', ip='100.19.0.16', cls=CPULimitedHost, cpu=.1)
    s19cpc = net.addHost('s19cpc', ip='100.19.0.21')
    s19db = net.addHost('s19db', ip='100.19.0.22')
    s19gw = net.addHost('s19gw', ip='100.19.0.23')

    #Add Hosts on Substation 24
    s24m1 = net.addHost('s24m1', ip='100.24.0.11', cls=CPULimitedHost, cpu=.1)
    s24m2 = net.addHost('s24m2', ip='100.24.0.12', cls=CPULimitedHost, cpu=.1)
    s24m3 = net.addHost('s24m3', ip='100.24.0.13', cls=CPULimitedHost, cpu=.1)
    s24m4 = net.addHost('s24m4', ip='100.24.0.14', cls=CPULimitedHost, cpu=.1)
    s24m5 = net.addHost('s24m5', ip='100.24.0.15', cls=CPULimitedHost, cpu=.1)
    s24m6 = net.addHost('s24m6', ip='100.24.0.16', cls=CPULimitedHost, cpu=.1)
    s24cpc = net.addHost('s24cpc', ip='100.24.0.21')
    s24db = net.addHost('s24db', ip='100.24.0.22')
    s24gw = net.addHost('s24gw', ip='100.24.0.23')


    # Link siwtch to switch
    net.addLink(s51,s52)
    net.addLink(s53,s52)
    net.addLink(s161,s162)
    net.addLink(s163,s162)
    net.addLink(s191,s192)
    net.addLink(s193,s192)
    net.addLink(s241,s242)
    net.addLink(s243,s242)

    # Link Control Center to Switch
    net.addLink(ccdb,s999, intfName1='ccdb-eth1', params1={'ip':'100.0.0.11/24'})
    net.addLink(cctl,s999, intfName1='cctl-eth1', params1={'ip':'100.0.0.12/24'})

    # Link Substation 5 Merging unit to Switch
    net.addLink(s05m1,s53, intfName1='s05m1-eth1', params1={'ip':'100.5.0.11/24'})
    net.addLink(s05m2,s53, intfName1='s05m2-eth1', params1={'ip':'100.5.0.12/24'})
    net.addLink(s05m3,s53, intfName1='s05m3-eth1', params1={'ip':'100.5.0.13/24'})
    net.addLink(s05m4,s53, intfName1='s05m4-eth1', params1={'ip':'100.5.0.14/24'})
    net.addLink(s05m5,s53, intfName1='s05m5-eth1', params1={'ip':'100.5.0.15/24'})
    net.addLink(s05m6,s53, intfName1='s05m6-eth1', params1={'ip':'100.5.0.16/24'}) 
    net.addLink(s05cpc,s52)
    net.addLink(s05db,s52)
    net.addLink(s05gw,s51, intfName1='s05gw-eth1', params1={'ip':'100.5.0.23/24'})

    # Link Substation 16 Merging unit to Switch
    net.addLink(s16m1,s163, intfName1='s16m1-eth1', params1={'ip':'100.16.0.11/24'})
    net.addLink(s16m2,s163, intfName1='s16m2-eth1', params1={'ip':'100.16.0.12/24'})
    net.addLink(s16m3,s163, intfName1='s16m3-eth1', params1={'ip':'100.16.0.13/24'})
    net.addLink(s16m4,s163, intfName1='s16m4-eth1', params1={'ip':'100.16.0.14/24'})
    net.addLink(s16m5,s163, intfName1='s16m5-eth1', params1={'ip':'100.16.0.15/24'})
    net.addLink(s16m6,s163, intfName1='s16m6-eth1', params1={'ip':'100.16.0.16/24'}) 
    net.addLink(s16cpc,s162)
    net.addLink(s16db,s162)
    net.addLink(s16gw,s161, intfName1='s16gw-eth1', params1={'ip':'100.16.0.23/24'})

    # Link Substation 19 Merging unit to Switch
    net.addLink(s19m1,s193, intfName1='s19m1-eth1', params1={'ip':'100.19.0.11/24'})
    net.addLink(s19m2,s193, intfName1='s19m2-eth1', params1={'ip':'100.19.0.12/24'})
    net.addLink(s19m3,s193, intfName1='s19m3-eth1', params1={'ip':'100.19.0.13/24'})
    net.addLink(s19m4,s193, intfName1='s19m4-eth1', params1={'ip':'100.19.0.14/24'})
    net.addLink(s19m5,s193, intfName1='s19m5-eth1', params1={'ip':'100.19.0.15/24'})
    net.addLink(s19m6,s193, intfName1='s19m6-eth1', params1={'ip':'100.19.0.16/24'}) 
    net.addLink(s19cpc,s192)
    net.addLink(s19db,s192)
    net.addLink(s19gw,s191, intfName1='s19gw-eth1', params1={'ip':'100.19.0.23/24'})

    # Link Substation 2 Merging unit to Switch
    net.addLink(s24m1,s243, intfName1='s24m1-eth1', params1={'ip':'100.24.0.11/24'})
    net.addLink(s24m2,s243, intfName1='s24m2-eth1', params1={'ip':'100.24.0.12/24'})
    net.addLink(s24m3,s243, intfName1='s24m3-eth1', params1={'ip':'100.24.0.13/24'})
    net.addLink(s24m4,s243, intfName1='s24m4-eth1', params1={'ip':'100.24.0.14/24'})
    net.addLink(s24m5,s243, intfName1='s24m5-eth1', params1={'ip':'100.24.0.15/24'})
    net.addLink(s24m6,s243, intfName1='s24m6-eth1', params1={'ip':'100.24.0.16/24'}) 
    net.addLink(s24cpc,s242)
    net.addLink(s24db,s242)
    net.addLink(s24gw,s241, intfName1='s24gw-eth1', params1={'ip':'100.24.0.23/24'})

    # Link Host Control Center to External gateway
    net.addLink(ccdb,s777, intfName1='ccdb-eth0', params1={'ip':'10.0.0.11/16'})
    net.addLink(cctl,s777, intfName1='cctl-eth0', params1={'ip':'10.0.0.12/16'})

    # Link Host Substation 1 to switch to external gateway
    net.addLink(s05m1,s777, intfName1='s05m1-eth0', params1={'ip':'10.0.5.11/16'})
    net.addLink(s05m2,s777, intfName1='s05m2-eth0', params1={'ip':'10.0.5.12/16'})
    net.addLink(s05m3,s777, intfName1='s05m3-eth0', params1={'ip':'10.0.5.13/16'})
    net.addLink(s05m4,s777, intfName1='s05m4-eth0', params1={'ip':'10.0.5.14/16'})
    net.addLink(s05m5,s777, intfName1='s05m5-eth0', params1={'ip':'10.0.5.15/16'})
    net.addLink(s05m6,s777, intfName1='s05m6-eth0', params1={'ip':'10.0.5.16/16'})
    net.addLink(s05gw,s777, intfName1='s05gw-eth0', params1={'ip':'10.0.5.23/16'})

    # Link Host Substation 2 to switch to external gateway
    net.addLink(s16m1,s777, intfName1='s16m1-eth0', params1={'ip':'10.0.16.11/16'})
    net.addLink(s16m2,s777, intfName1='s16m2-eth0', params1={'ip':'10.0.16.12/16'})
    net.addLink(s16m3,s777, intfName1='s16m3-eth0', params1={'ip':'10.0.16.13/16'})
    net.addLink(s16m4,s777, intfName1='s16m4-eth0', params1={'ip':'10.0.16.14/16'})
    net.addLink(s16m5,s777, intfName1='s16m5-eth0', params1={'ip':'10.0.16.15/16'})
    net.addLink(s16m6,s777, intfName1='s16m6-eth0', params1={'ip':'10.0.16.16/16'})
    net.addLink(s16gw,s777, intfName1='s16gw-eth0', params1={'ip':'10.0.16.23/16'})

    # Link Host Substation 12 to switch to external gateway
    net.addLink(s19m1,s777, intfName1='s19m1-eth0', params1={'ip':'10.0.19.11/16'})
    net.addLink(s19m2,s777, intfName1='s19m2-eth0', params1={'ip':'10.0.19.12/16'})
    net.addLink(s19m3,s777, intfName1='s19m3-eth0', params1={'ip':'10.0.19.13/16'})
    net.addLink(s19m4,s777, intfName1='s19m4-eth0', params1={'ip':'10.0.19.14/16'})
    net.addLink(s19m5,s777, intfName1='s19m5-eth0', params1={'ip':'10.0.19.15/16'})
    net.addLink(s19m6,s777, intfName1='s19m6-eth0', params1={'ip':'10.0.19.16/16'})
    net.addLink(s19gw,s777, intfName1='s19gw-eth0', params1={'ip':'10.0.19.23/16'})

    # Link Host Substation 20 to switch to external gateway
    net.addLink(s24m1,s777, intfName1='s24m1-eth0', params1={'ip':'10.0.24.11/16'})
    net.addLink(s24m2,s777, intfName1='s24m2-eth0', params1={'ip':'10.0.24.12/16'})
    net.addLink(s24m3,s777, intfName1='s24m3-eth0', params1={'ip':'10.0.24.13/16'})
    net.addLink(s24m4,s777, intfName1='s24m4-eth0', params1={'ip':'10.0.24.14/16'})
    net.addLink(s24m5,s777, intfName1='s24m5-eth0', params1={'ip':'10.0.24.15/16'})
    net.addLink(s24m6,s777, intfName1='s24m6-eth0', params1={'ip':'10.0.24.16/16'})
    net.addLink(s24gw,s777, intfName1='s24gw-eth0', params1={'ip':'10.0.24.23/16'})

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
    info( net[ 'r0' ].cmd( 'ip route add 100.5.0.0/24 via 200.5.0.2 dev r0-eth2' ) )
    info( net[ 'r5' ].cmd( 'ip route add 100.0.0.0/24 via 200.5.0.1 dev r5-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.16.0.0/24 via 200.16.0.2 dev r0-eth3' ) )
    info( net[ 'r16' ].cmd( 'ip route add 100.0.0.0/24 via 200.16.0.1 dev r16-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.19.0.0/24 via 200.19.0.2 dev r0-eth4' ) )
    info( net[ 'r19' ].cmd( 'ip route add 100.0.0.0/24 via 200.19.0.1 dev r19-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.24.0.0/24 via 200.24.0.2 dev r0-eth5' ) )
    info( net[ 'r24' ].cmd( 'ip route add 100.0.0.0/24 via 200.24.0.1 dev r24-eth2' ) )

    info( net[ 's05m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.5.0.1 dev s05m1-eth1' ) )
    info( net[ 's05m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.5.0.1 dev s05m2-eth1' ) )
    info( net[ 's05m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.5.0.1 dev s05m3-eth1' ) )
    info( net[ 's05m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.5.0.1 dev s05m4-eth1' ) )
    info( net[ 's05m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.5.0.1 dev s05m5-eth1' ) )
    info( net[ 's05m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.5.0.1 dev s05m6-eth1' ) )

    info( net[ 's16m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.16.0.1 dev s16m1-eth1' ) )
    info( net[ 's16m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.16.0.1 dev s16m2-eth1' ) )
    info( net[ 's16m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.16.0.1 dev s16m3-eth1' ) )
    info( net[ 's16m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.16.0.1 dev s16m4-eth1' ) )
    info( net[ 's16m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.16.0.1 dev s16m5-eth1' ) )
    info( net[ 's16m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.16.0.1 dev s16m6-eth1' ) )

    info( net[ 's19m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.19.0.1 dev s19m1-eth1' ) )
    info( net[ 's19m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.19.0.1 dev s19m2-eth1' ) )
    info( net[ 's19m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.19.0.1 dev s19m3-eth1' ) )
    info( net[ 's19m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.19.0.1 dev s19m4-eth1' ) )
    info( net[ 's19m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.19.0.1 dev s19m5-eth1' ) )
    info( net[ 's19m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.19.0.1 dev s19m6-eth1' ) )

    info( net[ 's24m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.24.0.1 dev s24m1-eth1' ) )
    info( net[ 's24m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.24.0.1 dev s24m2-eth1' ) )
    info( net[ 's24m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.24.0.1 dev s24m3-eth1' ) )
    info( net[ 's24m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.24.0.1 dev s24m4-eth1' ) )
    info( net[ 's24m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.24.0.1 dev s24m5-eth1' ) )
    info( net[ 's24m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.24.0.1 dev s24m6-eth1' ) )
    
    info( net[ 'ccdb' ].cmd( 'ip route add 100.5.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.16.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.19.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.24.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )

    info( net[ 'cctl' ].cmd( 'ip route add 100.5.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.16.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.19.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.24.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    
    info(os.system('ip addr add 100.0.0.99/24 dev s999'))
    info(os.system('ip link set s999 up'))

    #time.sleep(5)

    #info( net[ 's06db' ].cmd( 'python3 ascdb.py &amp' ) )


    CLI( net )
    net.stop()



if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()