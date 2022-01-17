# username:admin
# password:admin

username=input('Username :')
password=input('Password: ')
if username=='' or password=='':
    print('Melumat doldurulmayib')
else:
    if username=='admin' and password=='admin':
        print('Duzdur')
    else:
        print('Sehvdir')
