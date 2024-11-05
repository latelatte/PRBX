import random

class City:
    def __init__(self, name, infection_level=0):
        self.name = name
        self.infection_level = infection_level
        
    def increase_infection(self):
        self.infection_level += 1
        
    def treat_infection(self):
        if self.infection_level > 0:
            self.infection_level -= 1
            
class Player:
    def __init__(self, name, strategy):
        self.name = name
        self.city = None
        self.strategy = strategy
        
    def move(self, city):
        self.city = city
        print(f"{self.name} moved to {city.name}")
        
    def action(self):
        self.strategy(self)
        
        
class PandemicSimulation:
    def __init__(self, strategy1, strategy2):
        self.cities = [
            City("Atlanta", infection_level=random.randint(0, 3)),
            City("Chicago", infection_level=random.randint(0, 3)),
            City("New York", infection_level=random.randint(0, 3)),
            City("San Francisco", infection_level=random.randint(0, 3)),
            City("Washington", infection_level=random.randint(0, 3)), 
        ]
        for city in self.cities:
            city.cities = self.cities
            
        self.players = [
            Player("Alice", strategy1),
            Player("Bob", strategy2),
        ]
        self.players[0].move(self.cities[0])
        self.players[1].move(self.cities[1])
        
        self.outbreaks = 0
        
    def run(self):
        print("Starting new turn...")
        for player in self.players:
            player.action()
            
        for city in self.cities:
            if random.random() < 0.3:
                city.increase_infection()
                if city.infection_level > 3:
                    self.outbreaks += 1
                    print(f"Outbreak in {city.name}!")
                    for other_city in city.cities:
                        # 50% chance of spreading to other cities.
                        if other_city != city and random.random() < 0.5:
                            other_city.increase_infection()
                    city.infection_level = 3
                    
                
        self.show_status()
        
    def show_status(self):
        for city in self.cities:
            print(f"{city.name}: Infection Level = {city.infection_level}")
        print("\n")
        
    def is_game_over(self):
        if self.outbreaks >= 8:
                print(f"Game Over! Too many outbreaks.\nTotal Outbreaks: {self.outbreaks}")
                return True
        if self.check_victory():
            print("Game Over! All cities are cured.")
            return True
        return False
    
    def check_victory(self):
        return all(city.infection_level == 0 for city in self.cities)

# Define strategies
def aggressive_strategy(player):
    # move to the city with the highest infection level and treat it
    target_city = max(player.city.cities, key=lambda city: city.infection_level)
    player.move(target_city)
    player.city.treat_infection()
    
def cautious_strategy(player):
    # move to the city with the lowest infection level and treat it
    target_city = min(player.city.cities, key=lambda city: city.infection_level)
    player.move(target_city)
    player.city.treat_infection()
    
def cooperative_strategy(player):
    # asign different roles to players
    if player.name == "Alice":
        # move to the city with the highest infection level and treat it (aggressive)
        target_city = max(player.city.cities, key=lambda city: city.infection_level)
        player.move(target_city)
        player.city.treat_infection()
    else:
        # move to the city with the lowest infection level and treat it (cautious)
        target_city = min(player.city.cities, key=lambda city: city.infection_level)
        player.move(target_city)
        player.city.treat_infection()
        
simulation = PandemicSimulation(aggressive_strategy, aggressive_strategy)
simulation.show_status()

while not simulation.is_game_over():
    simulation.run()