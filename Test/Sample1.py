# !/usr/bin/python


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
        core_switch = self.addSwitch('cr1', switch=OVSSwitch)
        aggr_switch_1 = self.addSwitch('as1', switch=OVSSwitch)
        aggr_switch_2 = self.addSwitch('as2', switch=OVSSwitch)

        h1 = self.addHost('s1h1')
        h2 = self.addHost('s1h2')
        h3 = self.addHost('s2h1')
        h4 = self.addHost('s2h2')

        self.addLink(aggr_switch_1, core_switch)
        self.addLink(core_switch, aggr_switch_2)
        self.addLink(h1, aggr_switch_1)
        self.addLink(h2, aggr_switch_1)
        self.addLink(h3, aggr_switch_2)
        self.addLink(h4, aggr_switch_2)




if __name__ == "__main__":
    setLogLevel("info")

    topology = MyCustomTopo()
    controllerIP = '127.0.0.1'
    controllerPort = 6633
    freakController = RemoteController(name ='FreakCustomController',ip=controllerIP, port=controllerPort)
    net = Mininet(topo=topology)
    net.start()
    CLI(net)
    net.stop()
