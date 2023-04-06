#!/usr/bin/python3
"""
    program to gather data from an API
"""


import requests
import json


api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
response.json()