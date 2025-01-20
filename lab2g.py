#!/usr/bin/env python3
##Author: Jonathan Hopkins
##Author ID: 013095971
##Date Created: 2025/01/20
import sys

timer = 3
if len(sys.argv) != 1:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer -= 1
print('blast off!')