# IP-Force

A Multi-Threaded Python Port Scanner.

## Usage

`python ip-force.py -ip IP-ADDRESS`

### Flags

`-ip | --ipaddr` - Target IP Address (Required)

`-p | --port` - The port to be scanned.

`-v | --verbose` - This flag can be used to display the ports which are closed on a specific IP (If not used to program will only display 'open' ports related to the specified IP Address).

`-a | --all` - Tells the program to scan all ports (0-65533)

`-h | --help` - Displays help screen


#### Additional Features

- Program is able scan the top ports under a specific IP in the event no port is specified and `-a` switch (Scan all) has not been used.

#### To be added / Coming soon

- Functionality to allow program to not only determine a port's state, but also to determine the service running on said port.
