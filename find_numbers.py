'''
DESCRIPTION
    find multiplication of a given number
    usage of for, range, if, modulo (%), variable casting, regex
NOTES
    Author RJ
    Date 20171207
'''
import re

regex = r"\D+"
l = []

n = input('enter number ')

while re.search(regex, n):
    print(n, 'is not a number!')
    n = input('enter number ')

for i in range(1, 101):
    if (i % int(n)) == 0:
        l.append(i)
# print('multiplications of ', n, ' are :', *l)
print('multiplications of ', n, ' are: ', ' ,'.join(map(str, l)))
