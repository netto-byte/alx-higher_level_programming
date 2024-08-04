#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(argv) == 1 else argv[1]
    payload = {'q': letter}

    response = requests.post(url, data=payload)

    try:
        json_dict = response.json()
        if json_dict == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_dict["id"], json_dict["name"]))
    except ValueError:
        print("Not a valid JSON")
