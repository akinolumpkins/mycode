#!/usr/bin/python3

import requests

URL= "http://api.open-notify.org/astros.json"

URL= "http://api.open-notify.org/iss-now.json"

sliceme= requests.get(url).json()

def main():
    # requests.get() requests info from the URL
    # .json() method transforms that data into a Pythonic dictionary!
    sliceme= requests.get(URL).json()

# print out this person's name
print(sliceme["name"])

# print out the craft this person's on
print(type(sliceme["craft"]))

main()
