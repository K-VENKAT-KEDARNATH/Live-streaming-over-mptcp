from mininet.net import Mininet
from mininet.link import TCLink
from mininet import cli
from mininet.log import info,setLogLevel
import os

net = Mininet()
max_queue_size = 100
def createTopo():
    global net
    h1 = net.addHost('h1', ip='10.0.1.1')
    h2 = net.addHost('h2', ip='10.0.2.1')

    s3 = net.addSwitch('s3')

    net.addController("c0")


    net.addLink(h1, s3, cls=TCLink, bw=5, delay='50ms', max_queue_size=max_queue_size)
    net.addLink(h1, s3, cls=TCLink, bw=10, delay='1ms', max_queue_size=max_queue_size)
    net.addLink(h2, s3, cls=TCLink, bw=50, delay='1ms', max_queue_size=max_queue_size)
    net.addLink(h2, s3, cls=TCLink, bw=50, delay='1ms', max_queue_size=max_queue_size)
    net.addLink(h2, s3, cls=TCLink, bw=50, delay='1ms', max_queue_size=max_queue_size)


    h1.setIP('10.0.1.1', intf='h1-eth0')
    h1.setIP('10.0.1.2', intf='h1-eth1')

    h2.setIP('10.0.2.1', intf='h2-eth0')
    h2.setIP('10.0.2.2', intf='h2-eth1')
    h2.setIP('10.0.2.3', intf='h2-eth2')

    net.addNAT().configDefault()


def start():
    net.start()
    net.pingAll()
    cli.CLI(net)

def stop():
    if net is not None:
        net.stop()




if __name__ =="__main__":
    createTopo()
    setLogLevel('info')
    start()
