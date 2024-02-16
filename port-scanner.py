import sys 
import socket 
from datetime import datetime 

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

print(bcolors.GREEN + """

d8888b.  .d88b.  d8888b. d888888b      .d8888.  .o88b.  .d8b.  d8b   db d8b   db d88888b d8888b. 
88  `8D .8P  Y8. 88  `8D `~~88~~'      88'  YP d8P  Y8 d8' `8b 888o  88 888o  88 88'     88  `8D 
88oodD' 88    88 88oobY'    88         `8bo.   8P      88ooo88 88V8o 88 88V8o 88 88ooooo 88oobY' 
88~~~   88    88 88`8b      88           `Y8b. 8b      88~~~88 88 V8o88 88 V8o88 88~~~~~ 88`8b   
88      `8b  d8' 88 `88.    88         db   8D Y8b  d8 88   88 88  V888 88  V888 88.     88 `88. 
88       `Y88P'  88   YD    YP         `8888Y'  `Y88P' YP   YP VP   V8P VP   V8P Y88888P 88   YD 
                                                                                                 
""")
print("Enter your host ip address , Example '192.168.10.10'")
host = socket.gethostbyname(input("Enter your host ip address: "))

print("Enter the range, Example '50'")
ports = input(str("Enter range between 1 to 1000 "))

print("-" * 50)
print("scanning  target" + host)
print("Time started" + str(datetime.now()))
print("-" * 50)
try:
             for port in range(int(ports)):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)
                    result = s.connect_ex((host,port))
                    if result == 0:
                            print(F"Following {port} is open")
                    s.close()
         
except KeyboardInterrupt:
    print("\r Exiting program")

except socket.gaierror:
    print("Host name could not be solved")
    sys.exit()
except socket.error:
    print("could not connect")
    sys.exit()
