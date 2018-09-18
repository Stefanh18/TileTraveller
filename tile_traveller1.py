start = (1,1)

print('You can travel: (N)orth.')

while start != (3,1):
    
    if start == (1,1):
        direction = input('Direction: ').lower()
        if direction == "n":
            start = (1,2)
            print('You can travel: (N)orth or (E)ast or (S)outh.')
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            start = start

    if start == (1,2):
        if direction == 'n':
            start = (1,3)   
            print('You can travel: (E)ast or (S)outh.')
            direction = input('Direction: ')
        elif direction == 'E':
            start = (2,2) 
            print('You can travel: (S)outh or (W)est.')
            direction = input('Direction: ')
        elif direction == 's':
            start = (1,1)
            print('You can travel: (N)orth.')
        else:
            print('Not a valid direction!')
            start = start
            direction = input('Direction: ')

    if start == (1,3):
        if direction == 's':
            start = (1,2)
            print('You can travel: (N)orth or (E)ast or (S)outh.')
            direction = input('Direction: ')
        elif direction == 'e':
            start = (2,3)
            print('You can travel: (E)ast or (W)est.' )
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            start = start
            direction = input('Direction: ')

    if start == (2,2):
        if direction == 's':
            start = (2,1)    
            print('You can travel: (N)orth.' )
            direction = input('Direction: ')
        elif direction == 'w':
            start = (1,2)  
            print('You can travel: (N)orth or (E)ast or (S)outh.')
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            start = start
            direction = input('Direction: ')

    if start == (2,1):
        if direction == 'n':
            start = (2,2)
            print('You can travel: (S)outh or (W)est.')
            direction = input('Direction: ')    
        else:
            print('Not a valid direction!')
            start = start
            direction = input('Direction: ')

    if start == (2,3):
        if direction == 'e':
            start = (3,3) 
            print('You can travel: (S)outh or (W)est.')
            direction = input('Direction: ')
        elif direction == 'w':
            start = (1,3)  
            print('You can travel: (E)ast our (S)outh.')
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            start = start
            direction = input('Direction: ')

    if start == (3,3):
        if direction == 'w':
            start = (2,3)  
            print('You can travel: (E)ast or (W)est.')
            direction = input('Direction: ')
        elif direction == 's':
            start = (3,2) 
            print('You can travel: (N)orth or (S)outh.')
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            start = start
            direction = input('Direction: ')

    if start == (3,2):
        if direction == 's':
            start = (3,1) 
        elif direction == 'n':
            start = (3,3)  
            print('You can travel: (S)outh or (W)est.')
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            start = start
            direction = input('Direction: ')

    if start == (3,1):
        print('Victory!')