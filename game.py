import os
from player import Person

os.system('cls')

player1 = Person("Guille", "gnome careca", 10, 10)
player2 = Person("Otis", "ogre", 12, 8)

player1.list_player()
player2.list_player()

while True:
    
    print("")
    follow = input("Press return for the next turn...")    
    os.system('cls')

    #Player 1 attacks opponent
    player1.attack_opponent(player2.name)
    
    follow = input("Press return for the next turn...")    
    os.system('cls')      

    #Player 2 try to defense
    player2.defense_opponent(player1.name, player1.attack_force)

    follow = input("Press return for the next turn...")    
    os.system('cls')
    
    if (player2.health_current <= 0):
        print("Player 2 has died!")
        break    

    #Player 2 attacks opponent
    player2.attack_opponent(player1.name)
    
    follow = input("Press return for the next turn...")    
    os.system('cls')  

    #Player 1 try to defense
    player1.defense_opponent(player2.name, player2.attack_force)

    if (player1.health_current <= 0):
        print("Player 1 has died!")        
        break   
