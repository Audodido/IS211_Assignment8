import argparse
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.overall_total = 0
        self.turn_total = 0

class Human(Player):
        species = 'human'

class ComputerPlayer(Player):
        species = 'computer'

# call this from Game class to instantiate players
class PlayerFactory:
    def getPlayer(self, species, name):
        self.species = species
        
        if species == 'human':
            return Human(name)
        else:
            return ComputerPlayer(name)
    
    
    # # check to make sure player is human or computer
    # for s in range(len(species)):
    #     if species[s] in species_options:
    #         #if it is, create an instance of proper type of player -- this is a Factory??
    #         if species[s] == 'human':
    #             players.append(Human(f'{s}'))
    #         else:
    #             players.append(ComputerPlayer(f'{s}'))


class Die:
    def __init__(self, sides=6):
        self.sides = sides 

    def roll(self):
        dots = random.randint(1,6)
        return dots


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--player1", help="'human' or 'computer'", type=str, required=False)
    parser.add_argument("--player2", help="'human' or 'computer'", type=str, required=False)
    args = parser.parse_args()
    
    species = [args.player1, args.player2]
    players = []


# just a test that the facotry is working 
    fac = PlayerFactory()
    player1 = fac.getPlayer(args.player1, '1')

    print(f'player {player1.name} species: {player1.species}')

  
