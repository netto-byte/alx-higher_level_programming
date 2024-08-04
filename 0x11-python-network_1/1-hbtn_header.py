#!/usr/bin/env python3
"""Takes a URL as an argument and displays the value of the
'X-Request-Id' variable found in the header of the response.
"""

import urllib.request
from sys import argv

def main():
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        for header in response.getheaders():
            if header[0] == 'X-Request-Id':
                print(header[1])
                break

if __name__ == '__main__':
    main()

