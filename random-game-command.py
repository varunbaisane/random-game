import random as rand
import math
import time as t
print('Welcome to random choice game.')
sb = []                 #scoreboard
sb.append(['Player', 'Highscore'])
name = None

#Add new Highscore
#loop for continuous asking to play until exit
while True:
    print()
    #Menu
    start = input("Enter 'i' for Instructions\nEnter 'p' to Play the GAME\nEnter 's' to see Score Board\nEnter 'e' to exit: ")

    #Instructions
    if start.lower() == 'i':
        print()
        print('\nInstructions\n\nGive values for a range of numbers.\nChoose a number between specified range.\nIf it matches with number randomly chosen by the computer you win.\nWin the game in 25 rounds.\nWin the game in least time and least rounds and\ncome in the Scoreboard of TOP 3 Players.')

    #Playing Game
    elif start.lower() == 'p':
        print("\nLet's Begin")
        name = input('Enter your name: ')
        choice = 'yes'
        start = int(input('\nEnter starting number of the range: '))
        end = int(input('Starting number < Ending number\nEnter ending number of the range.: '))
        while end < start:
            print('Enter valid end number. \nend number > start number.')
            end = int(input('Enter ending number of the range.'))
        chances = 0
        s = t.time()
        while choice.lower() == 'yes':
            chances += 1
            print(f'Round {chances}')
            n = int(input(f'Choose number between {start} to {end}: '))
            res = rand.randint(start,end)
            if n == res:
                e = t.time()
                print('Hoooooooorayyyyyyyy!!!!!!!!!')
                print(f'Congratulations {name}')
                print(f'You took {chances} rounds to win the game.;)')
                score = (math.ceil(250 - (e - s)))*(25-chances)
                print(f'Your score: {score}')
                sb.append([name, score])
                if score == 6000:
                    print(f'{name} is legend.') #show something different on scoreboard
                print()
                choice = input(f'{name}, Want to Replay?(Yes/No) ')
                if choice.lower() == 'no':
                    pass
                elif choice.lower() == 'yes':
                    chances = 0
                    s = t.time()
                else:
                    print('Enter valid command.\n')
                    chances = 0
                    choice = input(f'{name}, Want to Replay?(Yes/No): ')
            elif n not in range(start, end+1):
                print()
                print('Enter valid number. ')
                print()
            else:
                print(f'Soooory, {name}. Retry.')
                print(f'Ans: {res}')
                print(f'You just missed by {int(math.fabs(res-n))}')
                print()
            if chances == 25:
                print('Oooo!\n25 rounds completed.\nGAME OVER')
                print(f'{name} scored: 0')
                chances = 0
                print()
                choice = input(f'{name}, Want to Replay?(Yes/No) ')
                if choice.lower() == 'no':
                    pass
                elif choice.lower() == 'yes':
                    chances = 0
                else:
                    print('Enter valid command.\n')
                    choice = input(f'{name}, Want to Replay?(Yes/No): ')

    #display scoreboard
    elif start.lower() == 's':
        if len(sb) == 1:
            print('\n No scores.')
        else:
            print('\n SCORE BOARD \n')
            print('\n TOP SCORERS \n')

            for x in range(1,len(sb)-1):
                for y in range(1,len(sb)-x):
                    if int(sb[y][1]) < int(sb[y+1][1]):
                        sb[y], sb[y+1] = sb[y+1], sb[y]

            tlen = len(str(sb[0][0]))
            for x in range(len(sb)):
                for y in range(len(sb[x])):
                    if len(str(sb[x][y])) > tlen:
                        tlen = len(str(sb[x][y]))

            c = 0
            for x in range(len(sb)):
                c += 1
                if c > 4:
                    break
                for y in range(len(sb[x])):
                    print('| {:<{}} '.format(sb[x][y], tlen), end = ' |')
                print()

    #Exit                
    elif start.lower() == 'e':
        break
    else:
        print('Enter valid command')

print()
if name != None :
    print(f'Thank You, {name}. Come Again ;)')
else:
    print('Thank You. Come Again ;)')
