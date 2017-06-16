# !/usr/bin/python


from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.node import OVSKernelSwitch

#Creating a simple DC Topology without remote controller

class FreakDC(Topo):
    def build( self):
        aggr_switch_1 = self.addSwitch('asw1', switch =OVSKernelSwitch, ip='192.168.10.2/24')
        aggr_switch_2 = self.addSwitch('asw2', switch =OVSKernelSwitch, ip='192.168.20.3/24')

        core_switch_1 = self.addSwitch('csw1',switch =OVSKernelSwitch, ip='192.168.10.1/24')

        sw1h1 = self.addHost('s1h1',ip='192.168.10.4/24')
        sw1h2 = self.addHost('s1h2',ip='192.168.10.5/24')
        sw1h3 = self.addHost('s1h3', ip='192.168.10.6/24')
        sw1h4 = self.addHost('s1h4', ip='192.168.10.7/24')
        sw1h5 = self.addHost('s1h5', ip='192.168.10.8/24')

        sw2h1 = self.addHost('s2h1', ip='192.168.10.9/24')
        sw2h2 = self.addHost('s2h2', ip='192.168.10.10/24')
        sw2h3 = self.addHost('s2h3', ip='192.168.10.11/24')
        sw2h4 = self.addHost('s2h4', ip='192.168.10.12/24')
        sw2h5 = self.addHost('s2h5', ip='192.168.10.13/24')

        self.addLink(node1=core_switch_1,node2=aggr_switch_1,port1=1,port2=1)
        self.addLink(node1=core_switch_1,node2=aggr_switch_2,port1=2,port2=1)

        self.addLink(node1=aggr_switch_1,node2=sw1h1,port1=2,port2=1)
        self.addLink(node1=aggr_switch_1,node2=sw1h2,port1=3,port2=1)
        self.addLink(node1=aggr_switch_1,node2=sw1h3,port1=4,port2=1)
        self.addLink(node1=aggr_switch_1,node2=sw1h4,port1=5,port2=1)
        self.addLink(node1=aggr_switch_1,node2=sw1h5,port1=6,port2=1)

        self.addLink(node1=aggr_switch_2, node2=sw2h1,port1=2,port2=1)
        self.addLink(node1=aggr_switch_2, node2=sw2h2,port1=3,port2=1)
        self.addLink(node1=aggr_switch_2, node2=sw2h3,port1=4,port2=1)
        self.addLink(node1=aggr_switch_2, node2=sw2h4,port1=5,port2=1)
        self.addLink(node1=aggr_switch_2, node2=sw2h5,port1=6,port2=1)


if __name__ == "__main__":
   setLogLevel("info")

    topology = FreakDC()
    controllerIP = '127.0.0.1'
    controllerPort = 6633
    freakController = RemoteController(name='FreakRemoteController', ip=controllerIP, port=controllerPort)
    net = Mininet(topo=topology,controller=freakController)
    net.start()
    CLI(net)
    net.stop()
