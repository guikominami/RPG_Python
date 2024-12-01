import os
from setup import Setup
from player import Person

os.system("cls")

# attack * dado

# tempo
# 1 pergunta de matemática
# 1 pergunta de geografia
# 1 pergunta de cultura geek

# 3 acertos = (5, 6)
# 2 acertos = (3, 4)
# 1 acerto = (1, 2)
# 0 acerto = sem dado


character1 = Setup(1)
character_data1 = character1.menu()

character2 = Setup(2)
character_data2 = character1.menu()

player1 = Person(
    character_data1["name"],
    character_data1["type_class"],
    character_data1["attack_points"],
    character_data1["defense_points"],
)
player2 = Person(
    character_data2["name"],
    character_data2["type_class"],
    character_data2["attack_points"],
    character_data2["defense_points"],
)

player1.list_player()
player2.list_player()

while True:

    follow = input("Press return for the next turn...")
    os.system("cls")

    # Player 1 attacks opponent
    player1.attack_opponent()

    # Player 2 try to defense
    player2.defense_opponent(player1.attack_force)

    if player2.health_current <= 0:
        print(f"{player2.name} has died!")
        break

    follow = input("Press return for the next turn...")
    os.system("cls")

    # Player 2 attacks opponent
    player2.attack_opponent()

    # Player 1 try to defense
    player1.defense_opponent(player2.attack_force)

    if player1.health_current <= 0:
        print(f"{player1.name} has died!")
        break
