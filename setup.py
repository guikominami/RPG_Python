class Setup():
    
    def __init__(self, number):
        self.number = number
    
    total_points = 20
    
    def create_name(self):
        character_name = input(f"Type the character {self.number} name: ")
        return character_name
    
    def create_type_class(self):
        character_type_class = input("Type the character class: ")
        return character_type_class    
    
    def create_points(self):    
        
        print("You have 20 points to distribute between attack and defense points.")  

        character_attack_points = input("Type the attack points quantity: ")
        try:
            character_attack_points_int = int(character_attack_points)
            print(character_attack_points)               
            if character_attack_points_int > 20 or character_attack_points_int <= 0:
                print("Choose a number between 1 and 19")
                
            character_defense_points = self.total_points - character_attack_points_int   
            
            return [character_attack_points_int, character_defense_points]
                                    
        except:
            print("Type a number.")
            
    def menu(self, number):
        
        setup = Setup(number)

        while True:
            name = setup.create_name()
            
            if name == "":
                print("Character name can´t be empty!")
                continue
            
            break

        while True:
            type_class = setup.create_type_class()
            
            if type_class == "":
                print("Character class can´t be empty!")
                continue
            
            break

        while True:
            points = setup.create_points()

            if points is None:
                continue
            
            attack_point = points[0]
            defense_points = points[1]
                
            break          
        
        character_data = {
            'name': name,
            'type_class': type_class,
            'attack_points': attack_point,
            'defense_points': defense_points
        } 
        
        return character_data        
            
if __name__ == "__main__":

    character1 = Setup(1)
    character_data1 = character1.menu(1)
    
    character_name1 = character_data1['name']
    character_class1 = character_data1['type_class']
    character_attack_points1 = character_data1['attack_points']
    character_defense_points1 = character_data1['defense_points']    
            
    print(character_name1, character_class1, character_attack_points1, character_defense_points1)
    
    character1 = Setup(2)
    character_data1 = character1.menu(2)
    
    character_name1 = character_data1['name']
    character_class1 = character_data1['type_class']
    character_attack_points1 = character_data1['attack_points']
    character_defense_points1 = character_data1['defense_points']    
            
    print(character_name1, character_class1, character_attack_points1, character_defense_points1)    