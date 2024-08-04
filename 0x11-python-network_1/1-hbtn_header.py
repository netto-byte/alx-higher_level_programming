#!/usr/bin/env python3
"""Takes a URL as an argument and displays the value of the
'X-Request-Id' variable found in the header of the response.
#!/usr/bin/python3
"""
import urllib.request
import sys


def get_x_request_id(url):
    with urllib.request.urlopen(url) as response:
        for header in response.getheaders():
            if header[0] == 'X-Request-Id':
                return header[1]
    return None


if __name__ == "__main__":
    url = sys.argv[1]
    x_request_id = get_x_request_id(url)
    if x_request_id:
        print(x_request_id)
