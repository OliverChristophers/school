import random
import time
import os


def game(skill, fatigue, num_targets):
    targets = ['*' for _ in range(num_targets)]
    
    print(f'you got {num_targets} shots')
    
    for i in range(num_targets):
        print(' '.join(targets))
        print('\n')
        
        shot = input(f'Shot number {i + 1} at: ')
        hit = True if skill * fatigue > random.randint(1, 100)/100 else False
        
        if hit:
            if targets[int(shot) - 1] == '*':
                print('Hit on open target\n')
                targets[int(shot) - 1] = 'O'
            else:
                print('Hit on closed target\n')
        else:
            print('Miss')
            
    print(f'You hit {targets.count("O")} out of {num_targets}') 
    
    return targets.count("O")


def create_players():
    player1 = {
        'skill':random.randint(85, 100)/100,
        'fatigue':random.randint(90, 100)/100
    } 
    
    player2 = {
        'skill':random.randint(85, 100)/100,
        'fatigue':random.randint(90, 100)/100
    }    
    
    return player1, player2



def startGame():
    
    v = '''
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Biathlon

            a hit or miss game
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    print(v)
    time.sleep(2)
    os.system('cls')
    num_targets = int(input('number of targets? '))
    playto = int(input('winning score? '))
    time.sleep(1)
    os.system('cls')
    
    return num_targets, playto

    
def gameloop(num_targets, playto, player1, player2):
    
    score1 = 0
    score2 = 0
    x = 0
    
    while True:
        x += 1
        print(f'begin round {x}...\n')
        print('Player 1:')
        score1 += game(player1['skill'], player1['fatigue'], num_targets=num_targets) 
        time.sleep(2)
        os.system('cls')

        time.sleep(1)
        print('Player 2:')
        score2 += game(player2['skill'], player2['fatigue'], num_targets=num_targets)  
        time.sleep(2)
        os.system('cls')
        
        print(f'\nscore: {score1}-{score2}\n')
        time.sleep(2)
        os.system('cls')
                
        if max([score1, score2]) > playto:
            print(f'player {[score1, score2].index(max([score1, score2])) + 1} wins!!!!!!')
            break
        
        player1['fatigue'] = player1['fatigue'] * random.randint(90, 100)/100
        player2['fatigue'] = player2['fatigue'] * random.randint(90, 100)/100
        
        
        


if __name__ == '__main__':
    
    player1, player2 = create_players()
    num_targets, playto = startGame()
    gameloop(num_targets, playto, player1, player2)
    
    


