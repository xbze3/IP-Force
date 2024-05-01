import argparse
import pyfiglet
import threading
import socket

global running
running = True

global topPorts
topPorts = 0

global th
th = []

parser = argparse.ArgumentParser(prog='python portScanner.py', description="Python Port Scanner")

parser.add_argument("-ip", "--ipaddr", type=str, required=True ,help="Target IP (xxx.xxx.xxx.xxx)")
parser.add_argument("-p", "--port", type=int, help="Port number to be scanned", default=-1)
parser.add_argument("-a", "--all", action='store_true', help="Scan all ports")
parser.add_argument("-v", "--verbose", action='store_true', help="Turn on/off verbose mode")

args = parser.parse_args()

global p
p = args.port

ascii_banner = pyfiglet.figlet_format("IP-FORCE")

print(ascii_banner)

print(" " + "=" * 60)
print(" IP-Force")
print(" by @xbze3 on GitHub")
print(" " + "-" * 60)
print(" Target IP: " + args.ipaddr)
print(" " + "=" * 60)

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


def scanner1Normal(ip, mode, all, wordlist):

    if(all):

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

        for port in range(0, len(wordlist), 3):
            if(running):
                s = connect1()

                result = s.connect_ex((ip,int(wordlist[port])))

                if result == 0:
                    print(f" Port:{wordlist[port].strip()} is open")

                elif(result != 0 and mode):
                    print(f" Port:{wordlist[port].strip()} is closed")

                s.close()

            else:
                return 0
    done(1)      
    return 0


def scanner2Normal(ip, mode, portNum, all, wordlist):

    if(portNum == -1 and all == True):

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
        
    elif(portNum != -1 and all == False):

        s = connect2()
                
        result = s.connect_ex((ip,portNum))

        if result == 0:
            print(f" Port:{portNum} is open")

        elif result != 0:
            print(f" Port:{portNum} is closed")
        
        s.close()

    else:

        for port in range(1, len(wordlist), 3):
            if(running):
                s = connect2()

                result = s.connect_ex((ip,int(wordlist[port])))

                if result == 0:
                    print(f" Port:{wordlist[port].strip()} is open")

                elif(result != 0 and mode):
                    print(f" Port:{wordlist[port].strip()} is closed")

                s.close()

            else:
                return 0
    done(2)
    return 0
            

def scanner3Normal(ip, mode, all, wordlist):

    if(all):
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
            
    else:
        for port in range(2, len(wordlist), 3):
            if(running):
                s = connect3()

                result = s.connect_ex((ip,int(wordlist[port])))

                if result == 0:
                    print(f" Port:{wordlist[port].strip()} is open")

                elif(result != 0 and mode):
                    print(f" Port:{wordlist[port].strip()} is closed")

                s.close()

            else:
                return 0
    done(3)
    return 0


def done(done):

    th.append(done)

    if(p == -1 and len(th) == 3): 

        print("\n " + "=" * 27 + " " + "Done" + " " + "=" * 27)

    elif(p != -1 and len(th) == 1):

        print("\n " + "=" * 27 + " " + "Done" + " " + "=" * 27)

    return 0      

if(args.port == -1):

    if(args.all != True):

        topPorts = open("topPorts.txt", 'r')
        topPorts = topPorts.readlines()

        thread1 = threading.Thread(target=scanner1Normal, daemon=True, args=(target, args.verbose, args.all, topPorts))
        thread2 = threading.Thread(target=scanner2Normal, daemon=True, args=(target, args.verbose, args.port, args.all, topPorts))
        thread3 = threading.Thread(target=scanner3Normal, daemon=True, args=(target, args.verbose, args.all, topPorts))

        thread1.start()
        thread2.start() 
        thread3.start()

        try:
            input(" [Press enter-key to exit]\n\n")
            print(" [Enter-Key] Detected | Closing IP-Force")

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

        thread1 = threading.Thread(target=scanner1Normal, daemon=True, args=(target, args.verbose, args.all, topPorts))
        thread2 = threading.Thread(target=scanner2Normal, daemon=True, args=(target, args.verbose, args.port, args.all, topPorts))
        thread3 = threading.Thread(target=scanner3Normal, daemon=True, args=(target, args.verbose, args.all, topPorts))

        thread1.start()
        thread2.start() 
        thread3.start()

        try:
            input(" [Press enter-key to exit]\n\n")
            print(" [Enter-Key] Detected | Closing IP-Force")

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
    thread2 = threading.Thread(target=scanner2Normal, daemon=True, args=(target, args.verbose, args.port, args.all, topPorts))
    thread2.start()

    try:
        input(" [Press enter-key to exit]\n\n")
        print(" [Enter-Key] Detected | Closing IP-Force")

    except KeyboardInterrupt:
        running = False
        thread2.join() 
        print("\n [CTRL+C] Detected | Closing IP-Force")

    except socket.gaierror:
        running = False
        print("\n Hostname Could Not Be Resolved | Closing IP-Force")

    except socket.error:
        running = False
        print("\ Server not responding | Closing IP-Force")
