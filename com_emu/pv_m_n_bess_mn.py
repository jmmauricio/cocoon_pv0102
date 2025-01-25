'''
Two isolated networks three hosts are connected to both.
One host is only connected to the netwoek with domain 192.168.X.X

sudo fuser -k 6653/tcp
sudo mn -c
sudo python3 pv_mn_bess_mn.py

h00001 python3 emulator.py &

LV0101 curl http://192.168.2.1:8000/measures

h0003 python3 edge.py POI -cfg_dev config_devices.json &
LV0101 python3 edge.py LV0101 -cfg_dev config_devices.json &
LV0102 python3 edge.py LV0102 -cfg_dev config_devices.json &


h0001 python3 ./modbus/modbus_client.py

sudo mnexec -a 1443 bash
sudo mnexec -a 1433 bash

sudo mnexec -a 1437 bash
sudo mnexec -a 1439 bash
sudo mnexec -a 8184 bash

h1 tc qdisc change dev h1-eth0 root netem delay 50ms
s0102 tc qdisc change dev s0102-eth2 root netem delay 100ms
s0103 tc qdisc change dev s0103-eth2 root netem delay 150ms

'''



#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
import time 
import json
import argparse


def interSecureModelNetwork(M=1, N=2, sEEMU_if = 'enp0s8', sEXT_if = 'enp0s9'):

    net = Mininet( topo=None,
                   build=False,
                   ipBase='1.0.0.0/8')
    
    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=OVSController,
                      protocol='tcp',
                      port=6633)

    switchType = OVSKernelSwitch; 

    ## Real network emulation ########################################################################################

    info( '*** Starting real networking devices\n')
    dpid = 1
    sPOI =  net.addSwitch( 'sPOI', cls=switchType, dpid=f'{dpid}',failMode='standalone')   

    for i_m in range(1,M+1):
        for i_n in range(1,N+1):
            dpid += 1
            name = f"{i_m}".zfill(2) + f"{i_n}".zfill(2)
            net.addSwitch(f's{name}', cls=switchType, dpid=f'{dpid}',failMode='standalone')    

    info( '*** Adding hosts \n')

    POI   = net.addHost(  'POI', cls=Host, ip='10.10.0.3/16', defaultRoute='10.10.0.1',mac='00:00:00:00:00:03')  # POI 
    PPC   = net.addHost(  'PPC', cls=Host, ip='10.10.0.4/16', defaultRoute='10.10.0.1',mac='00:00:00:00:00:04')  # PPC
    Probe = net.addHost('Probe', cls=Host, ip='10.10.0.5/16', defaultRoute='10.10.0.1',mac='00:00:00:00:00:05')  # Probe    

    for i_m in range(1,M+1):
        for i_n in range(1,N+1):
            dpid += 1
            m_str,n_str =  f"{i_m}".zfill(2),f"{i_n}".zfill(2)
            name = m_str + n_str 
            net.addHost(f'LV{name}', cls=Host, ip=f'10.10.{i_m}.{i_n}/8', defaultRoute='10.10.0.1',mac=f'00:00:00:00:{m_str}:{n_str}')   

    info( '*** Adding real network links\n')

    net.addLink(  POI, sPOI)
    net.addLink(  PPC, sPOI)
    net.addLink(Probe, sPOI)

    for i_m in range(1,M+1):
        name_j = "sPOI"
        for i_n in range(1,N+1):
            name = f"{i_m}".zfill(2) + f"{i_n}".zfill(2)
            name_k = 's' + name

            net.addLink(name_j, name_k)
            net.addLink(f"LV{name}", name_k, cls=TCLink, delay='20ms')
            name_j = name_k
    
    ## Emulation network  ########################################################################################

    info( '*** Starting external connection\n')  
    dpid += 1
    sEXT =  net.addSwitch( 'sEXT', cls=switchType, dpid=f'{dpid}',failMode='standalone')     
    dpid += 1 
    sEEMU = net.addSwitch('sEEMU', cls=switchType, dpid=f'{dpid}',failMode='standalone')  # switch for the electrical emulator
    Intf(  sEEMU_if, node=sEEMU )  # EDIT the interface name here! 
    #Intf(  'eth1', node=sEEMU )  # EDIT the interface name here! 

    Intf(  sEXT_if, node=sEXT )  # EDIT the interface name here! 
    #Intf( 'enp0s10', node=sPOI )  # EDIT the interface name here! 



    info( '*** Setting link parameters\n')
    #WAN1 = {'bw':1000,'delay':'20ms','loss':1,'jitter':'10ms'} 
    #GBPS = {'delay':'18ms'} 
    #MBPS = {'bw':10} 

    net.addLink(  POI, sEEMU)
    net.addLink(  PPC, sEXT)

    for i_m in range(1,M+1):
        for i_n in range(1,N+1):
            name = f"{i_m}".zfill(2) + f"{i_n}".zfill(2)
            net.addLink(f"LV{name}", sEEMU)

    #net.addLink(WANR1, DSS1GW, cls=TCLink , **MBPS)
    info( '\n')

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting networking devices \n')
    net.get( 'sPOI').start([])

    for i_m in range(1,M+1):
        for i_n in range(1,N+1):
            dpid += 1
            m_str,n_str =  f"{i_m}".zfill(2),f"{i_n}".zfill(2)
            name = m_str + n_str 
            net.get(f's{name}').start([])

    net.get('sEEMU').start([])
    net.get('sEXT').start([])

    info( '\n')

    info( '*** Preparing custom sgsim scripts \n')
    #CLI.do_webserver = webserver    
    net.get(  'POI').cmd('ifconfig POI-eth1 10.20.0.3 netmask 255.255.0.0')
    net.get(  'PPC').cmd('ifconfig PPC-eth1 172.20.0.4 netmask 255.255.0.0')
    net.get('Probe').cmd('ifconfig Probe-eth1 10.10.0.5 netmask 255.255.0.0')


    for i_m in range(1,M+1):
        for i_n in range(1,N+1):
            dpid += 1
            m_str,n_str =  f"{i_m}".zfill(2),f"{i_n}".zfill(2)
            name = m_str + n_str 
            net.get(f's{name}').start([])

            net.get(f'LV{name}').cmd(f'ifconfig LV{name}-eth1 10.20.{m_str}.{n_str} netmask 255.255.0.0')

    hosts_dict = {}
    for item in ['POI']:
        #pid = net.get(item).cmd(f"pgrep -f '{item}'| head -n 1")
        pid_raw = net.get(item).cmd(f"pgrep -f '{item}'")
        pid_raws = pid_raw.split('\r\n')
        print(pid_raws)
        hosts_dict.update({item:{'pid':int(pid_raws[-2])}})

    for i_m in range(1,M+1):
        for i_n in range(1,N+1):
            m_str,n_str =  f"{i_m}".zfill(2),f"{i_n}".zfill(2)
            name = m_str + n_str 
            #pid = net.get(item).cmd(f"pgrep -f '{item}'| head -n 1")
            pid_raw = net.get(f'LV{name}').cmd(f"pgrep -f 'LV{name}'")
            pid_raws = pid_raw.split('\r\n')
            print('LV',pid_raws)
            hosts_dict.update({f'LV{name}':{'pid':int(pid_raws[-2])}})

    print(hosts_dict)
    # Convert dictionary to JSON
    hosts_json = json.dumps(hosts_dict, indent=4)

    # Write JSON data to a file
    with open("hosts.json", "w") as json_file:
        json_file.write(hosts_json)


    info( '*** Model Started *** \n' )
    CLI(net)
    net.stop()

# def webserver(self, line):
#     "Starts Python Simple HTTP Server on LV0101" 
#     net = self.mn   
#     info('Starting the webserver... \n')        
#     net.get('LV0101').cmdPrint('xterm -geometry 90x30+10+10 -fa "Monospace" -fs 12 -T "Webserver" -e "python3 -m http.server 8080;bash"&') 
#     time.sleep(0.5)
   
if __name__ == '__main__':
    setLogLevel( 'info' )


    parser = argparse.ArgumentParser()
    parser.add_argument("-m", help="number of feeders")
    parser.add_argument("-n", help="number of generators per feeder")
    parser.add_argument("-sEEMU_if", help="Emulator interface")
    parser.add_argument("-sEXT_if", help="PPC External interface")

    args = parser.parse_args()
    print(args)
    m = int(args.m)
    n = int(args.n)
    sEEMU_if = args.sEEMU_if
    sEXT_if = args.sEXT_if

    if sEEMU_if == None: sEEMU_if = 'enp0s8' 
    if sEXT_if == None: sEXT_if = 'enp0s9' 
        
    interSecureModelNetwork(m,n,sEEMU_if,sEXT_if)