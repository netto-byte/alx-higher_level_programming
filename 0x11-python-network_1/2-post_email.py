#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
if __name__ == "__main__":
    from urllib.request import Request, urlopen
    import urllib.parse as parse
    from sys import argv

    url = argv[1]
    email = argv[2]

    values = {'email': email}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = Request(url, data)

    with urlopen(req) as response:
        html_page = response.read()
        print("{}".format(html_page.decode('utf-8')))
