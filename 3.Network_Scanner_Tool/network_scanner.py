
#Menu driven network scanning tool:
import nmap

def main_menu():
	print("Network Scanner Tool")
	print("--------------------")
	print("1 -> Scan single host")
	print("2 -> Scan range")
	print("3 -> Scan network")
	print("4 -> Agressive scan")
	print("5 -> Scan ARP packet")
	print("6 -> Scan All port only")
	print("7 -> Scan in verbose mode")
	print("8 -> Exit")

def scan_single_host():
	nm = nmap.PortScanner()
	ip_address = input("\tEnter the IP address : ")
	print("Wait.......................")
	try:
		scan = nm.scan(hosts=ip_address,ports="1-100",arguments = "-v -sS -O -Pn")
		print("@@@",scan)
		for host in scan["scan"][ip_address]['tcp'].items():
			print("Tcp Port => ",host[0])
			print("State => ",host[1]['state'])
			print("Reason => ",host[1]['reason'])
			print("Name => ",host[1]['name'])
	except:
		print("Use sudo ")
		
def scan_range():
	nm = nmap.PortScanner()
	ip_address = input("\tEnter the IP address : ")
	print("Wait........................")
	try:
		scan = nm.scan(hosts=ip_address,arguments = "-sS -O -Pn")
		print("@@@",scan)
		for port in scan["scan"][ip_address]['tcp'].items():
			print(f"TCP port : {port[0]}, {port[1]['state']} , {port[1]['name']}")
	except:
		print("Use sudo")
	
	
def scan_network():
	nm = nmap.PortScanner()
	ip_address = input("\tEnter the IP address : ")
	print("Wait........................")
	try:
		scan = nm.scan(hosts=ip_address,arguments = "-sS -O -Pn")
		for i in scan["scan"][ip_address]['osmatch']:
			print(f"Name => {i['name']}")
			print(f"Accuracy => {i['accuracy']}")
			print(f"OSClass => {i['osclass']}\n")
		
	except:
		print("Use sudo")
	

def agg_scan():
	nm = nmap.PortScanner()
	ip_address = input("\tEnter the IP address : ")
	print("Wait........................")
	try:
		scan = nm.scan(hosts=ip_address,arguments = "-sS -O -Pn -T4")
		for i in scan["scan"][ip_address]['osmatch']:
			print(f"Name => {i['name']}")
			print(f"Accuracy => {i['accuracy']}")
			print(f"OSClass => {i['osclass']}\n")
		
	except:
		print("Use sudo")
	

def arp_packets():
	nm = nmap.PortScanner()
	ip_address = input("\tEnter the IP address : ")
	print("Wait........................")
	try:
		scan = nm.scan(hosts=ip_address,arguments = "-sS -O -PR")
		for i in scan["scan"][ip_address]['osmatch']:
			for j in i['osclass']:
				print(f"cpe : {j['cpe']}")
				print(f"osfamily : {j['osfamily']}")
	except:
		print("Use sudo")
		

def scan_all_ports():
	nm = nmap.PortScanner()
	ip_address = input("\tEnter the IP address : ")
	print("Wait........................")
	try:
		scan = nm.scan(hosts = ip_address,ports = "1-3",arguments = "-sS -O -Pn")
		for port in scan["scan"][ip_address]['tcp'].items():
			print(f"{port[0]}, {port[1]['state']} , {port[1]['name']}, {port[1]['conf']}")
	except:
		print("Use sudo")
	

def scan_verb():
	nm = nmap.PortScanner()
	ip_address = input("\tEnter the IP address : ")
	print("Wait........................")
	try:
		scan = nm.scan(hosts = ip_address,arguments = "-sS -O -Pn -v")
		for i in scan["scan"][ip_address]['osmatch']:
			print(f"Name => {i['name']}")
			print(f"Accuracy => {i['accuracy']}")
			print(f"OSClass => {i['osclass']}")
	except:
		print("Use sudo")
		
	

	
while True:
	main_menu()
	ch =  int(input("Enter your choice : "))
	if ch == 1:
		scan_single_host()
	elif ch == 2:
		scan_range()
	elif ch == 3:
		scan_network()
	elif ch == 4:
		agg_scan()
	elif ch == 5:
		arp_packets()
	elif ch == 6:
		scan_all_ports()
	elif ch == 7:
		scan_verb()
	elif ch == 8:
		break;
	else:
		print("Invalid Choice")
