#!/usr/bin/python


from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.node import OVSSwitch

customcontroller = RemoteController("FreakCustomController", ip='192.168.1.4', port=6633)


class CustomSwitch(OVSSwitch):
    def start(self, controllers):
        return OVSSwitch.start(self, customcontroller)


# Extend Topo to build your own topology
class MyCustomTopo(Topo):
    # Override build to make your own topology
    def build(self):
        # Write your topology here
        # core_switch_1 = self.addSwitch('core1', switch=OVSSwitch)

        aggr_switch_1 = self.addSwitch('agrsw1', switch=CustomSwitch)
        aggr_switch_2 = self.addSwitch('agrsw2', switch=CustomSwitch)

        tor_switch_1 = self.addSwitch('tors1', switch=CustomSwitch)
        tor_switch_2 = self.addSwitch('tors2', switch=CustomSwitch)
        tor_switch_3 = self.addSwitch('tors3', switch=CustomSwitch)
        tor_switch_4 = self.addSwitch('tors4', switch=CustomSwitch)

        r_1_s_1 = self.addHost('r1s1')
        r_1_s_2 = self.addHost('r1s2')

        r_2_s_1 = self.addHost('r2s1')
        r_2_s_2 = self.addHost('r2s2')

        r_3_s_1 = self.addHost('r3s1')
        r_3_s_2 = self.addHost('r3s2')

        r_4_s_1 = self.addHost('r4s1')
        r_4_s_2 = self.addHost('r4s2')

        self.addLink(r_1_s_1, tor_switch_1)
        self.addLink(r_1_s_2, tor_switch_1)

        self.addLink(r_2_s_1, tor_switch_2)
        self.addLink(r_2_s_2, tor_switch_2)

        self.addLink(r_3_s_1, tor_switch_3)
        self.addLink(r_3_s_2, tor_switch_3)

        self.addLink(r_4_s_1, tor_switch_4)
        self.addLink(r_4_s_2, tor_switch_4)

        self.addLink(aggr_switch_1, tor_switch_1)
        self.addLink(aggr_switch_1, tor_switch_2)

        self.addLink(aggr_switch_2, tor_switch_3)
        self.addLink(aggr_switch_2, tor_switch_4)

        # self.addLink(core_switch_1, aggr_switch_1)
        # self.addLink(core_switch_1, aggr_switch_2)


if __name__ == "__main__":
    setLogLevel("info")

    topology = MyCustomTopo()

    net = Mininet(topo=topology)

    # net.addController("FreakCustomController", controller=RemoteController, ip='192.168.1.4', port=6633)

    # net.addController("FreakCustomController")

    net.start()
    CLI(net)
    net.stop()
