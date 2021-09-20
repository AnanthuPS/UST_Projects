import os


def interface_menu():
    print("\t_____Choose an interface_____")
    print("\t1. wlp4s0")
    print("\t2. enp2s0")
    print("\t3. virbr0")
    print("\t4. docker0")
    print("\t5. lo")
    print("\t--------------")

def assign_ip():
    interface_menu()
    ch = int(input("\t Choose your interface : "))

    if ch == 1:
        ip = input("\t\t Enter the IP address for wlp4s0 : ")
        cmd =f"sudo ip address add {ip} dev wlp4s0"
        ip_assign = os.popen(cmd).read()
        print(os.popen("ip -4 a show wlp4s0").read())

    elif ch == 2:
        ip = input("\t\t Enter the IP address for enp2s0 : ")
        cmd =f"sudo ip address add {ip} dev enp2s0"
        ip_assign = os.popen(cmd).read()
        print(os.popen("ip -4 a show enp2s0").read())

    elif ch == 3:
        ip = input("\t\t Enter the IP address for virbr0 : ")
        cmd =f"sudo ip address add {ip} dev virbr0"
        ip_assign = os.popen(cmd).read()
        print(os.popen("ip -4 a show virbr0").read())

    elif ch == 4:
        ip = input("\t\t Enter the IP address for docker0 : ")
        cmd =f"sudo ip address add {ip} dev docker0"
        ip_assign = os.popen(cmd).read()
        print(os.popen("ip -4 a show docker0").read())

    elif ch == 5:
        ip = input("\t\t Enter the IP address for lo : ")
        cmd =f"sudo ip address add {ip} dev lo"
        ip_assign = os.popen(cmd).read()
        print(os.popen("ip -4 a show lo").read())               

def del_ip():
    interface_menu()
    ch = int(input("\t Choose your interface : "))

    if ch == 1:
        ip = input("\t\t Enter the IP address for deletion (wlp4s0) : ")
        cmd =f"sudo ip address del {ip} dev wlp4s0"
        ip_del = os.popen(cmd).read()
        print(os.popen("ip -4 a show wlp4s0").read())

    elif ch == 2:
        ip = input("\t\t Enter the IP address for for deletion (enp2s0) : ")
        cmd =f"sudo ip address del {ip} dev enp2s0"
        ip_del = os.popen(cmd).read()
        print(os.popen("ip -4 a show enp2s0").read())

    elif ch == 3:
        ip = input("\t\t Enter the IP address for for deletion (virbr0) : ")
        cmd =f"sudo ip address del {ip} dev virbr0"
        ip_del = os.popen(cmd).read()
        print(os.popen("ip -4 a show virbr0").read())

    elif ch == 4:
        ip = input("\t\t Enter the IP address for for deletion (docker0) : ")
        cmd =f"sudo ip address del {ip} dev docker0"
        ip_del = os.popen(cmd).read()
        print(os.popen("ip -4 a show docker0").read())

    elif ch == 5:
        ip = input("\t\t Enter the IP address for for deletion (lo) : ")
        cmd =f"sudo ip address del {ip} dev lo"
        ip_del = os.popen(cmd).read()
        print(os.popen("ip -4 a show lo").read())
    

def display_ip():
    cmd = f"ip -c -br address"
    print(os.popen(cmd).read())

def display_all_interface():
    cmd = f"ifconfig"
    print(os.popen(cmd).read())

def conf_routing():
    netw_addr = input("Enter the Network address with mask : ")
    gate_ip = input("Enter the Gateway IP : ")
    cmd = f"ip r add {netw_addr} via {gate_ip}"
    print(os.popen(cmd).read())

def turn_interface_onoroff():
    print("_____Choose an option_____")
    print("1. Turn off an interface")
    print("2. Turn on an interface")
    ch = int(input("Enter your option : "))
    if ch == 1:
        interface_menu()
        ch = int(input("\tChoose an interface : "))
        if ch == 1:
            print(os.popen('sudo ip link set dev wlp4s0 down').read())
        elif ch == 2:
            print(os.popen('sudo ip link set dev enp2s0 down').read())
        elif ch == 3:
            print(os.popen('sudo ip link set dev virbr0 down').read())
        elif ch == 4:
            print(os.popen('sudo ip link set dev docker0 down').read())
        elif ch == 5:
            print(os.popen('sudo ip link set dev lo down').read())

    elif ch == 2:
        interface_menu()
        ch = int(input("\tChoose an interface : "))
        if ch == 1:
            print(os.popen('sudo ip link set dev wlp4s0 up').read())
        elif ch == 2:
            print(os.popen('sudo ip link set dev enp2s0 up').read())
        elif ch == 3:
            print(os.popen('sudo ip link set dev virbr0 up').read())
        elif ch == 4:
            print(os.popen('sudo ip link set dev docker0 up').read())
        elif ch == 5:
            print(os.popen('sudo ip link set dev lo up').read())

    else:
        print("Choose a valid option")                          


def add_arp_entry():
    ip = input("Enter an IP address : ")
    cmd = f"sudo ip n add {ip} lladdr 24:94:93:1e:be:14 dev wlp4s0 nud permanent"
    arp = os.popen(cmd).read()
    print(os.popen("ip n show").read())

def delete_arp_entry():
    ip = input("Enter an IP address : ")
    cmd = f"sudo ip n del {ip} dev wlp4s0"
    arp = os.popen(cmd).read()
    print(os.popen("ip n show").read())

def restart_network():
    cmd = f"sudo systemctl restart networking"
    os.popen(cmd).read()
    print("Network restarted!")
    print(os.popen("sudo systemctl status networking").read())

def change_hostname():
    host_name = input("Enter new host name :")
    cmd = f'hostnamectl set-hostname {host_name}'
    os.popen(cmd).read()
    print(f"new host name {host_name} set successfully")


def add_dns_server_entry():
    cmd = 'sudo cat  >> /etc/resolv.conf'
    print(os.popen(cmd).read())
    print('Nameserver added successfully')
