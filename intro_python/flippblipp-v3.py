
def flippblipp(n:int) -> str:
    if n % 15 == 0:
        return 'flipp blipp'
    elif n % 5 == 0:
        return 'flipp'
    elif n % 3 == 0:
        return 'blipp'
    else:
        return str(n)
    

n = 0
print(1)
while True:
    n += 1
    
    inp = input('Nästa: ')
    if str(inp) != flippblipp(n=n + 1):
        print(f'Fel - {inp}')
        print('Game over')
        break
    