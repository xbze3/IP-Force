# IP-Force

A Multi-Threaded Python Port Scanner.

## Usage

`python ip-force.py -ip IP-ADDRESS`

### Flags

`-ip | --ipaddr` - Target IP Address (Required)

`-p | --port` - The port to be scanned (If not specified, the program will scan all ports).

`-v | --verbose` - This flag can be used to display the ports which are closed on a specific IP (If not used to program will only display 'open' ports related to the specified IP Address).

#### To be Added / Coming Soon

- Allow program to only scan the top ports under a specific IP, rather than scan all ports by default.

- Functionality to allow program to not only determine a port's state, but also to determine the service running on said port.
