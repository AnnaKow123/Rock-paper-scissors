import random

print('Witaj w grze kamień, papier, nożyce. Wybierz opcję ;)')
options=['papier', 'kamień', 'nożyce']
check='tak'
while check=='tak':
        
    player1=input('Gracz 1: ').lower()
    while player1 not in options:
        print('Wpisano nieprawidłowe wyrażenie. Wpisz jeszcze raz')
        player1=input('Gracz 1: ')
        
        
    player2=random.choice(options)
    print(f'Komputer: {player2}')
    
    if player1==player2:
        print('Remis')
    else:
        if player1=='papier':
            if player2=='kamień':
                print('Gracz 1 wygrał')
            else:
                print('Komputer wygrał')
        elif player1=='kamień':
            if player2=='papier':
                print('Komputer wygrał')
            else:
                print('Gracz 1 wygrał')
        elif player1=='nożyce':
            if player2=='papier':
                print('Gracz 1 wygrał')
            else:
                print('Komputer wygrał')
    check=input('Czy kontynuować grę? (Tak/Nie): ').lower()

