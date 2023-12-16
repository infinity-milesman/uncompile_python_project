# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.4 (main, Apr  2 2022, 09:04:19) [GCC 11.2.0]
# Embedded file name: ./sample.py
# Compiled at: 2023-12-16 19:11:21
"""
Approach:-
largest palindrome made from two digit given....will find it
as ....largest number... starts from 99.....9.....
multiply that number with less than that number and then check whether it's palindrome or not.
"""

def is_palindrome_numer(number):
    return str(number) == str(number)[::-1]


my_list = []
for i in range(100, 999, 1):
    for j in range(999, 100, -1):
        number = i * j
        if is_palindrome_numer(number) and len(str(i)) == len(str(j)):
            my_list.append(number)

print max(my_list)