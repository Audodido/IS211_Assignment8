import argparse
from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides 

    def roll(self):
        dots = randint(1,6)
        return dots


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
# https://www.youtube.com/watch?v=-a1PFtooGo4
class PlayerFactory:
    def get_player(self, species, name):
        self.species = species
        
        if species == 'human':
            return Human(name)
        if species == 'computer':
            return ComputerPlayer(name)
        else:
            print(f'invalid species type: {species}. Please choose \'human\' or \'computer\'')
    

class Game:
    def __init__(self, die, species):
        self.species = species #list of species types to be instantiated
        self.die = die
        self.players = []


    def make_players(self): #creates instances of players from PlayerFactory
        for p in range(len(self.species)):
            player = PlayerFactory()
            self.players.append(player.get_player(self.species[p], str(p)))


    def is_game_over(self): # will have to eventually check for game duration as well
        for player in self.players:
            if player.overall_total >= 100:
                return True
            else:
                return False

    def turn(self, player):
        pass

    def message(self, player, msg):
        self.player = player
        #store messages for any occasion here:
        msg_bank = {            
            'turn_tot_msg' : f'Current turn-total for player {player.name}: {player.turn_total}',
        }

        return msg_bank[msg]


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--player1", help="'human' or 'computer'", type=str, required=False)
    parser.add_argument("--player2", help="'human' or 'computer'", type=str, required=False)
    parser.add_argument("--timed", help="'y' or 'n'", type=str, required=False)
    args = parser.parse_args()
    
    print("Welcome to Pig")
    players = [args.player1, args.player2] 
    die = Die()

    game = Game(die, players)
    game.make_players()

    #below for testing
    for p in game.players:
        print(p.name, p.species)
        print(game.message(p, 'turn_tot_msg'))