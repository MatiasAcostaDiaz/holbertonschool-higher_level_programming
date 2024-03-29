#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status"""


import requests


if __name__ == '__main__':
    page = requests.get("https://intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(page.text), page.text))
