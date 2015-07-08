#!/usr/bin/env python

"""
  Usage
  $ python cipher.py < cipher.txt
"""

import sys

def decrypt(encrypted_number):
  # calcurate code**d mod n
  d = 299
  n = 493
  mod = 1
  for i in range(d):
    mod *= encrypted_number
    mod %= n
  return mod

# receive cipher.txt by redirection
for line in sys.stdin:
  input_strs = line.split()
  # parse each str to Integer
  input_nums = map(int, input_strs)
  # decrypt each number
  decrypted_nums = map(decrypt ,input_nums)
  
  list_size = len(decrypted_nums)
  text = 0
  step = 8
  bitlen = 5
  stack = []

  print "Input"
  print input_nums
  print ""
  print ""
  print "-------------------------------------------------"

  for i in range(0, list_size, step):

    # packing 8numbers to 40bit (5bit * 8numbers = 40bit)
    for j in range(0, step):
      text = text<<bitlen
      text += decrypted_nums[i+j]&0x1F

    # pop each character(8bit) from LSB and push to stack
    for j in range(0, bitlen):
      char = text&0xFF
      stack.append(char)
      text = text>>step
    text = 0

    # pop 5 characters from stack
    for j in range(0, bitlen):
      char = stack.pop()
      sys.stdout.write(chr(char))
  print ""
  print "-------------------------------------------------"
  print ""
