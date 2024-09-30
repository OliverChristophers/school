def flippblipp(n:int) -> str:
    if n % 15 == 0:
        return 'flipp blipp'
    elif n % 5 == 0:
        return 'flipp'
    elif n % 3 == 0:
        return 'blipp'
    else:
        return str(n)
    

n = 40
for i in range(1, n + 1):
    print(flippblipp(i))