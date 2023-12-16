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

print(max(my_list))
