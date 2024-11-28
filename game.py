import os
from player import Person

os.system('cls')

player1 = Person("Guille", "gnome careca", 10, 10)
player2 = Person("Otis", "ogre", 12, 8)

#Player 1 attacks opponent
player1.attack_opponent(player2.name)

#Player 2 try to defense
player2.defense_opponent(player1.name, player1.attack_force)

#generate hit points
player1.calculate_hit_points(player1.attack_force, player2.defense_force)