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

        self.addLink(core_switch_1,aggr_switch_1)
        self.addLink(core_switch_1,aggr_switch_2)

        self.addLink(aggr_switch_1,sw1h1)
        self.addLink(aggr_switch_1, sw1h2)
        self.addLink(aggr_switch_1, sw1h3)
        self.addLink(aggr_switch_1, sw1h4)
        self.addLink(aggr_switch_1, sw1h5)

        self.addLink(aggr_switch_2, sw2h1)
        self.addLink(aggr_switch_2, sw2h2)
        self.addLink(aggr_switch_2, sw2h3)
        self.addLink(aggr_switch_2, sw2h4)
        self.addLink(aggr_switch_2, sw2h5)


if __name__ == "__main__":
    setLogLevel("info")

    topology = FreakDC()

    net = Mininet(topo=topology)

    net.addController("FreakCustomController", controller=RemoteController, ip='192.168.1.4', port=6633)


    net.start()
    CLI(net)
    net.stop()
