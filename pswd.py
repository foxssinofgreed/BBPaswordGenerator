#!/bin/python3

import random
import cgitb

cgitb.enable()

start_response('200 OK', [('Content-Type', 'text/html')])

print('''
BB Password Generator
=====================
''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*?0123456789'
BBchars = 'BB@'
number = 1
length = 8

print('New BB Password:')

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(BBchars + password)
