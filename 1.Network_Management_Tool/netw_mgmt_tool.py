#Network Management Tool(Menu driven)

import os
from netw_mgmt_fun import *

def main_menu():
    print("__________Network Management Tool __________")
    print("Enter your choice : ")
    print("1. Assign IP address")
    print("2. Delete IP address")
    print("3. Display IP address")
    print("4. Display all interfaces")
    print("5. Configure routing")
    print("6. Turn On/Off interface")
    print("7. Add ARP entry")
    print("8. Delete ARP Entry")
    print("9. Restart Network")
    print("10. Change hostname")
    print("11. Add DNS server entry")
    print("12. Quit")
    print("---------------------------------------------")




while True:
    main_menu()
    ch = int(input("Enter your choice : "))

    if ch == 1:
        assign_ip()

    elif ch == 2:
        del_ip()

    elif ch == 3:
        display_ip()

    elif ch == 4:
        display_all_interface()

    elif ch == 5:
        conf_routing()

    elif ch == 6:
        turn_interface_onoroff()

    elif ch == 7:
        add_arp_entry()

    elif ch == 8:
        delete_arp_entry()

    elif ch == 9:
        restart_network()

    elif ch == 10:
        change_hostname()

    elif ch == 11:
        add_dns_server_entry()  

    elif ch == 12:
        break                                 

  