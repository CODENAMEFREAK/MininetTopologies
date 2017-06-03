#!/usr/bin/python


from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.node import OVSSwitch
from mininet.topolib import TreeNet


# Extend Topo to build your own topology
class MyCustomTopo(Topo):
    # Override build to make your own topology
    def build(self):


        tor_switch_1 = self.addSwitch('TOR_S_1', switch=OVSSwitch,controller=RemoteController, ip='192.168.1.4', port=6633)

        r_1_s_1 = self.addHost('R_1_S_1')
        r_1_s_2 = self.addHost('R_1_S_2')
        r_1_s_3 = self.addHost('R_1_S_3')
        r_1_s_4 = self.addHost('R_1_S_4')
        r_1_s_5 = self.addHost('R_1_S_5')






        self.addLink(r_1_s_1, tor_switch_1)
        self.addLink(r_1_s_2, tor_switch_1)
        self.addLink(r_1_s_3, tor_switch_1)
        self.addLink(r_1_s_4, tor_switch_1)
        self.addLink(r_1_s_5, tor_switch_1)









if __name__ == "__main__":
    setLogLevel("info")

    topology = MyCustomTopo()

    net = Mininet(topo=topology)

    #net.addController("FreakCustomController", controller=RemoteController, ip='192.168.1.4', port=6633)


    net.start()
    CLI(net)
    net.stop()
    #setLogLevel('info')
    #network = TreeNet(depth=2, fanout=3, switch=OVSSwitch,controller=RemoteController, ip='192.168.1.4', port=6633)
	#network.addController("FreakCustomController", controller=RemoteController, ip='192.168.1.4', port=6633)
    #network.run(CLI, network)
