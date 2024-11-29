import os
import random

class Person:
    health_initial = 100

    def __init__(self, name, class_type, attack_points, defense_points):
        self._name = name
        self._class_type = class_type
        self._attack_points = attack_points
        self._defense_points = defense_points
        self.health_current = self.health_initial
        
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
        return self._hit_points
    
    @hit_points.setter
    def hit_points(self, value):
        self._hit_points = value   
        
    @property
    def health_current(self):
        return self._health_current
    
    @health_current.setter
    def health_current(self, value):
        self._health_current = value

    def list_player(self):
        print(
            f"{self.name}, {self.class_type}, attack: {self.attack_points}, defense: {self.defense_points}, life: {self.health_initial}"
        )

    def attack_opponent(self, opponent_name):
        dice = random.randrange(1, 6)    

        self.attack_force = int(self.attack_points) * dice
        print(f'{self.name} - Attack force (attack_points: {self.attack_points}) * (dice: {dice}) = {self.attack_force}')     
        print()

    def defense_opponent(self, opponent_name, attack_force_opponent_points):
        dice = random.randrange(1, 6)    

        self.defense_force = int(self.defense_points) * dice
        print(f'{self.name} - Defense force (defense_points: {self.defense_points}) * (dice: {dice}) = {self.defense_force}')             
        print()
        
        self.hit_points = attack_force_opponent_points - self.defense_force

        if self.hit_points > 0:
            self.health_current = self.health_current - self.hit_points            

        print(f'Attack force ({attack_force_opponent_points}) - Defense Force ({self.defense_force}) = hit points: {self.hit_points}')
        
        word = ""
        if self.hit_points <= 0:
            word = " not"
            
        print(f"{self.name} has{word} suffer damage!")
        
        if self.health_current < 0:
            self.health_current = 0
            
        print(f'current health = {self.health_current}')            
        print()
    

