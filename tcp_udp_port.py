import re


#ACTUAL REGEX 
tcp_regex_and_port  = re.compile (r'(\d+.\d+.\d+.\d+:(\d+))+')
tcp_regex = re.compile (r'(\d+.\d+.\d+.\d+:\d+)+')
port_regex = re.compile (r':(\d+)+')
service_regex = re.compile(r'\d+/(\w+)')
port_and_service_regex = re.compile(r'((:(\d+)+)(.+?)(\d+/(\w+)))')

#CONSTANTS
EPHEMERAL_LOW = 1024
EPHEMERAL_HIGH = 65550

#SAMPLE
portsOpen='''

Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 192.168.122.1:53        0.0.0.0:*               LISTEN      2644/dnsmasq        
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1932/sshd           
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      1926/cupsd          
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      2419/master         
tcp6       0      0 :::22                   :::*                    LISTEN      1932/sshd           
tcp6       0      0 ::1:631                 :::*                    LISTEN      1926/cupsd          
tcp6       0      0 ::1:25                  :::*                    LISTEN      2419/master         
udp        0      0 0.0.0.0:36740           0.0.0.0:*                           891/avahi-daemon: r 
udp        0      0 192.168.122.1:53        0.0.0.0:*                           2644/dnsmasq        
udp        0      0 0.0.0.0:67              0.0.0.0:*                           2644/dnsmasq        
udp        0      0 0.0.0.0:68              0.0.0.0:*                           1723/dhclient       
udp        0      0 0.0.0.0:5353            0.0.0.0:*                           891/avahi-daemon: r 
udp        0      0 0.0.0.0:28988           0.0.0.0:*                           1723/dhclient       
udp        0      0 127.0.0.1:323           0.0.0.0:*                           903/chronyd         
udp6       0      0 :::23178                :::*                                1723/dhclient       
udp6       0      0 ::1:323                 :::*                                903/chronyd     

'''


def get_TCP(file):
    #TCP REGEX
    port_and_service_regex2 = re.compile(r'(tcp(.+)?(:(\d+)+) (.+)?(\d+/(\w+)))')
    m3 = port_and_service_regex2.findall(portsOpen)
    for i in m3:
        #CHECK TYPE
        if int(i[3]) > EPHEMERAL_LOW:
            var1 = 'EPHEMERAL'
        else:
            var1 = 'RESERVED'
        print('protocol:' + i[0][:4],'tcp_port: ' + i[3], 'service: '+ i[6], 'type: ' + var1)


def get_UDP(file):
    #UDP REGEX
    port_and_service_regex3 = re.compile(r'(udp(.+)?(:(\d+)+) (.+)?(\d+/(\w+)))')
    m4 = port_and_service_regex3.findall(portsOpen)
    for i in m4:
        if int(i[3]) > EPHEMERAL_LOW:
            var1 = 'EPHEMERAL'
        else:
            var1 = 'RESERVED'
        print('protocol:' + i[0][:4],'tcp_port: ' + i[3], 'service: '+ i[6], 'type: ' + var1)


get_TCP(portsOpen)
get_UDP(portsOpen)