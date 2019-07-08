n = 5
while n > 0:
    print(n)
    n = n - 1
print('Kaboom')
print(n)

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done1!')

n = 0
while True:
    n = n + 1
    line = input('Do you want to see next? ')
    if line == 'no':
        break
    if (n%2 != 0):
        print('Nothing to show')
        continue        
    print(n)
print('Done2!')
