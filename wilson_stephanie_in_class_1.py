#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Stephanie Wilson
2-20-19
Python 1 - DAT-119 - Spring 2019
In-class assignment week 3

calculating time from a user's input of seconds

"""

# get a number of seconds from user
total_seconds = float(input('Enter the number of seconds: '))

# get the number of hours
hours = total_seconds // 3600

# get the number of remaining minutes
minutes = (total_seconds // 60) % 60

# get the number of remaining seconds
seconds = total_seconds % 60

# display results
print('Here is the time in hours, minutes, and seconds:')
print('Hours:', hours, end=' ')
print(' Minutes:', minutes, end=' ')
print(' Seconds:', seconds, end=' ')