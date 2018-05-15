#!/usr/local/bin/python3

import requests

#TODO configurate this
todosFile='/Users/ccolquitt/notes/todos.txt'

with open(todosFile) as payload:
    headers = {'content-type': 'text/plain; charset=UTF-8'}
    r = requests.post('http://ec2-18-191-74-145.us-east-2.compute.amazonaws.com/cgi-bin/simple-data-server.py', data=payload, verify=False, headers=headers)
    print(r.text)

