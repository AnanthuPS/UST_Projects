import os
import json


def main_menu():
    print('_____Manage Docker_____')
    print('1.Status of containers')
    print('2.Download new Image')
    print('3.Run container')
    print('4.Delete Container')
    print('5.Network details of container')
    print('6.Modify Network details of contaniner')
    print('7.Quit')


while True:
    main_menu()
    ch = int(input("Enter your choice : "))

    if ch == 1:
        # checking docker container status
        cmd = 'docker container stats'
        os.system(cmd)
    
    elif ch == 2:
        # download images from docker repo
        img_name = input("Enter image_name : ")
        cmd = f'docker pull {img_name}'
        print(os.popen(cmd).read())
            
    elif ch == 3:
        # run container
        img_name = input("Enter image_name : ")
        container_name = input('Enter container name : ')
        cmd = f'docker run --name {container_name} {img_name}'
        os.system(cmd)
        print(os.popen('docker ps -a |head -n 2').read())

    elif ch == 4:
        # delete container
        container_name = input('Enter container name : ')
        cmd = f'docker rm {container_name}'
        res = os.popen(cmd).read()
        print(f'{res} container deleted successfully')
    
    elif ch == 5:
        # network details of a container
        cmd = 'docker network inspect bridge'
        print(os.popen(cmd).read())
    
    elif ch == 6:
        print("-------Network details--------")
        print(os.popen("docker network ls").read())
        network_name = input("Enter the network name : ")
        container_image = input("Enter the container name to disconnect from network :")
        print(f"Disconnecting {container_image} from {network_name}")
        cmd =f"docker network disconnect {network_name} {container_image}"
        print(os.popen(cmd).read())
        print("Disconnected network",style="bold blue")
        print(f"Connecting {container_image} to  {network_name}")
        cmd1 = f"docker network connect {network_name} {container_image}"
        print(os.popen(cmd1).read())
        print("Connected to network")

    elif ch == 7:
        break

    else:
        print('Invalid option')