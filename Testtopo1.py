#!/usr/bin/python


from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.node import OVSSwitch
from mininet.node import OVSController


# Extend Topo to build your own topology
class MyCustomTopo(Topo):
    # Override build to make your own topology
    def build(self):
        # Write your topology here
        ovs_switch = self.addSwitch('s1', switch=OVSSwitch)

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        self.addLink(h1, ovs_switch)
        self.addLink(h2, ovs_switch)
        self.addLink(h3, ovs_switch)
        self.addLink(h4, ovs_switch)


if __name__ == "__main__":
    setLogLevel("info")
    topology = MyCustomTopo()
    net = Mininet(topo=topology)
    net.addController("MyController", controller=RemoteController, ip='10.112.19.131', port=6633)

    net.start()
    CLI(net)
    net.stop()
