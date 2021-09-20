#Program for finding the system health

import os

def main_menu():
    print("__________System Health Finder__________")
    print("1. Display available RAM")
    print("2. Display Load avearge")
    print("3. Display Hostname details")
    print("4. Display All process count")
    print("5. Display uptime")
    print("6. Quit")

def available_ram():
    cmd = 'free -m | tr -s " " | cut -d " " -f7 | head -n 2'
    print(os.popen(cmd).read())

def load_avg():
    cmd = 'cat /proc/loadavg'
    print(os.popen(cmd).read())

def host_name():
    cmd = 'hostnamectl status'
    print(os.popen(cmd).read())

def process_count():
    cmd = 'ps -a | wc -l'
    print(os.popen(cmd).read())

def uptime():
    print(os.popen('uptime').read())


while True:
    main_menu()
    ch = int(input("Enter your choice : "))

    if ch == 1:
        available_ram()

    elif ch == 2:
        load_avg()

    elif ch == 3:
        host_name()

    elif ch == 4:
        process_count()

    elif ch == 5:
        uptime()

    elif ch == 6:
        break

    else:
        print("Enter a valid choice !")
