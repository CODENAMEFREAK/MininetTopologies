#!/usr/bin/python


from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.node import OVSSwitch


# Extend Topo to build your own topology
class MyCustomTopo(Topo):
    # Override build to make your own topology
    def build(self):
        # Write your topology here
        core_switch_1 = self.addSwitch('C_S_1', switch=OVSSwitch)

        aggr_switch_1 = self.addSwitch('A_S_1', switch=OVSSwitch)
        aggr_switch_2 = self.addSwitch('A_S_2', switch=OVSSwitch)

        tor_switch_1 = self.addSwitch('TOR_S_1', switch=OVSSwitch)
        tor_switch_2 = self.addSwitch('TOR_S_2', switch=OVSSwitch)
        tor_switch_3 = self.addSwitch('TOR_S_3', switch=OVSSwitch)
        tor_switch_4 = self.addSwitch('TOR_S_4', switch=OVSSwitch)

        r_1_s_1 = self.addHost('R_1_S_1')
        r_1_s_2 = self.addHost('R_1_S_2')
        r_1_s_3 = self.addHost('R_1_S_3')
        r_1_s_4 = self.addHost('R_1_S_4')
        r_1_s_5 = self.addHost('R_1_S_5')

        r_2_s_1 = self.addHost('R_2_S_1')
        r_2_s_2 = self.addHost('R_2_S_2')
        r_2_s_3 = self.addHost('R_2_S_3')
        r_2_s_4 = self.addHost('R_2_S_4')
        r_2_s_5 = self.addHost('R_2_S_5')

        r_3_s_1 = self.addHost('R_3_S_1')
        r_3_s_2 = self.addHost('R_3_S_2')
        r_3_s_3 = self.addHost('R_3_S_3')
        r_3_s_4 = self.addHost('R_3_S_4')
        r_3_s_5 = self.addHost('R_3_S_5')

        r_4_s_1 = self.addHost('R_4_S_1')
        r_4_s_2 = self.addHost('R_4_S_2')
        r_4_s_3 = self.addHost('R_4_S_3')
        r_4_s_4 = self.addHost('R_4_S_4')
        r_4_s_5 = self.addHost('R_4_S_5')

        self.addLink(r_1_s_1, tor_switch_1)
        self.addLink(r_1_s_2, tor_switch_1)
        self.addLink(r_1_s_3, tor_switch_1)
        self.addLink(r_1_s_4, tor_switch_1)
        self.addLink(r_1_s_5, tor_switch_1)

        self.addLink(r_2_s_1, tor_switch_2)
        self.addLink(r_2_s_2, tor_switch_2)
        self.addLink(r_2_s_3, tor_switch_2)
        self.addLink(r_2_s_4, tor_switch_2)
        self.addLink(r_2_s_5, tor_switch_2)

        self.addLink(r_3_s_1, tor_switch_3)
        self.addLink(r_3_s_2, tor_switch_3)
        self.addLink(r_3_s_3, tor_switch_3)
        self.addLink(r_3_s_4, tor_switch_3)
        self.addLink(r_3_s_5, tor_switch_3)

        self.addLink(r_4_s_1, tor_switch_4)
        self.addLink(r_4_s_2, tor_switch_4)
        self.addLink(r_4_s_3, tor_switch_4)
        self.addLink(r_4_s_4, tor_switch_4)
        self.addLink(r_4_s_5, tor_switch_4)

        self.addLink(aggr_switch_1, tor_switch_1)
        self.addLink(aggr_switch_1, tor_switch_2)

        self.addLink(aggr_switch_2, tor_switch_3)
        self.addLink(aggr_switch_2, tor_switch_4)

        self.addLink(core_switch_1, aggr_switch_1)
        self.addLink(core_switch_1, aggr_switch_2)


if __name__ == "__main__":
    setLogLevel("info")

    topology = MyCustomTopo()

    net = Mininet(topo=topology)

    net.addController("FreakCustomController", controller=RemoteController, ip='192.168.1.4', port=6633)

    # net.addController("FreakCustomController")

    net.start()
    CLI(net)
    net.stop()
