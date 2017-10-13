# port_scanner

A tool to check a host's open ports using python

## Usage

```
% python port_scanner_updated.py
```

You will then be presented with a prompt to input the host to be scanned (IP or hostname), followed by a comma-separated list of ports to scan. The below is an example of the output:

```
[>]Input the host to be scanned: dns.server
[>]Enter the comma-separated list of ports to be scanned: 53,80
['53', '80']
[+]Scan starting, be patient
[+]Scan finished, Results :
[*]Open ports
[*] 53
[*]Closed ports
[*] 80
```