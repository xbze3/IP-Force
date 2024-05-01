import argparse
import pyfiglet
import threading
import socket

global running
running = True

parser = argparse.ArgumentParser(prog='python portScanner.py', description="Python Port Scanner")

parser.add_argument("-ip", "--ipaddr", type=str, required=True ,help="Target IP (xxx.xxx.xxx.xxx)")
parser.add_argument("-p", "--port", type=int, help="Port number to be scanned", default=-1)
parser.add_argument("-v", "--verbose", action='store_true',help="Turn on/off verbose mode")

args = parser.parse_args()

ascii_banner = pyfiglet.figlet_format("IP-FORCE")

print(ascii_banner)

print("=" * 60)
print(" IP-Force")
print(" by @xbze3 on GitHub")
print("-" * 60)
print(" Target IP: " + args.ipaddr)
print("=" * 60)

target = socket.gethostbyname(args.ipaddr)

def connect1():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    return connection

def connect2():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    return connection

def connect3():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    return connection


def scanner1Normal(ip, portNum, mode):

    if(portNum == -1):

        for port in range(1, 65535, 3):
            if(running):
                s = connect1()

                result = s.connect_ex((ip,port))

                if result == 0:
                    print(f" Port:{port} is open")

                elif(result != 0 and mode):
                    print(f" Port:{port} is closed")

                s.close()

            else:
                return 0
            
    else:

        s = connect1()
                
        result = s.connect_ex((ip,portNum))

        if result == 0:
            print(f" Port:{portNum} is open")

        else:
            print(f" Port:{port} is closed")
        
        s.close()

def scanner2Normal(ip, mode):

    for port in range(2, 65535, 3):
        if(running):
            s = connect2()

            result = s.connect_ex((ip,port))

            if result == 0:
                print(f" Port:{port} is open")

            elif(result != 0 and mode):
                print(f" Port:{port} is closed")

            s.close()

        else:
            return 0
            

def scanner3Normal(ip, mode):

    for port in range(3, 65535, 3):
        if(running):
            s = connect3()

            result = s.connect_ex((ip,port))

            if result == 0:
                print(f" Port:{port} is open")

            elif(result != 0 and mode):
                print(f" Port:{port} is closed")

            s.close()

        else:
            return 0
                 

if(args.port == -1):

    thread1 = threading.Thread(target=scanner1Normal, daemon=True, args=(target, args.port, args.verbose))
    thread2 = threading.Thread(target=scanner2Normal, daemon=True, args=(target, args.verbose))
    thread3 = threading.Thread(target=scanner3Normal, daemon=True, args=(target, args.verbose))

    thread1.start()
    thread2.start() 
    thread3.start()

    try:
        input("")

    except KeyboardInterrupt:
        running = False
        thread1.join() 
        thread2.join() 
        thread3.join()
        print("\n [CTRL+C] Detected | Closing IP-Force")

    except socket.gaierror:
        running = False
        print("\n Hostname Could Not Be Resolved | Closing IP-Force")

    except socket.error:
        running = False
        print("\ Server not responding | Closing IP-Force")

else:
    thread1 = threading.Thread(target=scanner1Normal, daemon=True, args=(target, args.port, args.verbose))
    
    thread1.start()

    try:
        input("")

    except KeyboardInterrupt:
        running = False
        thread1.join() 
        print("\n [CTRL+C] Detected | Closing IP-Force")

    except socket.gaierror:
        running = False
        print("\n Hostname Could Not Be Resolved | Closing IP-Force")

    except socket.error:
        running = False
        print("\ Server not responding | Closing IP-Force")


