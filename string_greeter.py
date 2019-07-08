still_work = 'yes'
while still_work == 'yes':
    greet = 'Hello name'
    hiname = input('Your name pls ')
    nstr = greet.replace('name', hiname)
    print(nstr)
    still_work = input('Still work? yes? ')
    print('ok')
