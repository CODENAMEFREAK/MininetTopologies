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
        #mycontroller = RemoteController('FreakController',ip='192.168.1.4',port=6633)
        ovs_switch_1 = self.addSwitch('s1', switch=OVSSwitch)
        ovs_switch_2 = self.addSwitch('s2', switch=OVSSwitch)

        ovs_core_switch = self.addSwitch('cs0', switch=OVSSwitch)

        s_1_h_1 = self.addHost('s1h1')#, ip='10.0.0.1/24')
        s_1_h_2 = self.addHost('s1h2')#, ip='10.0.0.2/24')

        s_2_h_1 = self.addHost('s2h1')#, ip='10.0.0.3/24')
        s_2_h_2 = self.addHost('s2h2')#, ip='10.0.0.4/24')

        self.addLink(s_1_h_1, ovs_switch_1)
        self.addLink(s_1_h_2, ovs_switch_1)
        self.addLink(s_2_h_1, ovs_switch_2)
        self.addLink(s_2_h_2, ovs_switch_2)
        self.addLink(ovs_switch_1, ovs_core_switch)
        self.addLink(ovs_switch_2, ovs_core_switch)
        self.addLink(s_1_h_1, ovs_core_switch)
        self.addLink(s_1_h_2, ovs_core_switch)
        self.addLink(s_2_h_1, ovs_core_switch)
        self.addLink(s_2_h_2, ovs_core_switch)


if __name__ == "__main__":
    setLogLevel("info")

    topology = MyCustomTopo()

    net = Mininet(topo=topology)
    net.addController("FreakCustomController", controller=RemoteController, ip='192.168.1.4', port=6633)

    # net.addController("FreakCustomController")

    net.start()
    CLI(net)
    net.stop()
