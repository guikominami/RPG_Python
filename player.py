import os
import random

class Person:
    health_initial = 100

    def __init__(self, name, class_type, attack_points, defense_points):
        self._name = name
        self._class_type = class_type
        self._attack_points = attack_points
        self._defense_points = defense_points
        
    @property
    def name(self):
        return self._name      

    @property
    def attack_points(self):
        return self._attack_points

    @property
    def defense_points(self):
        return self._defense_points

    @property
    def class_type(self):
        return self._class_type
    
    @property
    def attack_force(self):
        return self._attack_force
    
    @attack_force.setter
    def attack_force(self, value):
        self._attack_force = value  
        
    @property
    def defense_force(self):
        return self._defense_force
    
    @defense_force.setter
    def defense_force(self, value):
        self._defense_force = value                 

    @property
    def hit_points(self):
        return self.hits
    
    @hit_points.setter
    def hit_points(self, value):
        self.hits = value   
        
    @property
    def health_current (self):
        if self.hit_points > 0:
            return (self.health_initial - self.hit_points)
        return self.health_initial
    
    @health_current .setter
    def health_current (self, value):
        self._health_current  = value

    def list_player(self):
        print(
            f"{self.name}, {self.class_type}, attack: {self.attack_points}, defense: {self.defense_points}, life: {self.health_initial}"
        )

    def attack_opponent(self, opponent_name):

        self.list_player()

        print(
            f"Attacking with force: {self.attack_points} the opponent ({opponent_name})."
        )

        dice = random.randrange(1, 6)
        print()        
        print(f'Roll the dice: {dice}')

        self.attack_force = int(self.attack_points) * dice
        print(f'Attack force (attack_points: {self.attack_points}) * (dice: {dice}): {self.attack_force}')     
        print()

    def defense_opponent(self, opponent_name, attack_force_opponent_points):
        self.list_player()

        print(
            f"Defending from attack force: {attack_force_opponent_points} the opponent ({opponent_name}) with defense: {self.defense_points}"
        )

        dice = random.randrange(1, 6)
        print()        
        print(f'Roll the dice: {dice}')

        self.defense_force = int(self.defense_points) * dice
        print(f'Defense force (defense_points: {self.defense_points}) * (dice: {dice}): {self.defense_force}')             
        print()

    def calculate_hit_points(self, attack_force_player1, defense_force_player2):
        self.hit_points = attack_force_player1 - defense_force_player2
        print(f'hit points: {self.hit_points} - current health : {self.health_current }')
