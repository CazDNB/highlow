# Lets make a game of highlow, program gives a hint, user has to pick if the result is Higher or Lower than the hint

import random


def menu ():
    print("""
    --------------------------------------------------
                    Welcome to Highlow
    --------------------------------------------------
            
            (1) Play                
            (2) Quit              
            
            """)



menu()

menu_sel = input('Select an option: ')

if menu_sel == '1':

    #Game picks up a number and a hint

    answer = random.randint(0, 100)
    hint = random.randint(0, 100)

    #Game gives the hint to the user so they can pick higher or lower

    print (f'The hint number is: {hint}')

    #Game loop
    atempt = input ('Input h for high or l for low \n')
    
    #Validation loop
    while atempt == 'h' or atempt == 'l':
        break
    else:
        print('You have to input either H or L')
        atempt = input ('Input h for high or l for low \n')

    #Game
    if answer > hint and atempt == 'h':
        print(f'You Won! The number was: {answer} which is higher than {hint}')        
    elif answer < hint and atempt == 'l':
        print(f'You won! The number was {answer}, which is lower than {hint}')        
    elif answer == hint and atempt == hint:
        print('The numbers were equal, you got lucky!')        
    else:
        print (f'You lost!, the number was {answer}')
        


else:
    print('Goodbye!')
    exit




