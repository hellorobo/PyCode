mylist = [1, 2, 3, 4, 5]

for m in mylist:
    if m > 2:
        print(m)

password = ''
secret = 'password123'
while password != secret:
    password = input('enter password: ')
    if password == secret:
        print('you\'re logged in')
    else:
        print('wrong password try again!')
