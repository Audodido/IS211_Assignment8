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
            self.players.append(player.get_player(self.species[p], f'player {str(p+1)}'))


    def is_game_over(self): # will have to eventually check for game duration as well
        for player in self.players:
            if player.overall_total >= 100:
                return True
            else:
                return False

    def message(self, player, msg, roll=None):
        self.player = player
        self.roll = roll
        #store messages for any occasion here:
        msg_bank = {            
            'turn_tot_msg' : f'Current turn-total for {self.player.name}: {self.player.turn_total}',
            'roll_prompt' : 'Enter "r" to roll. Enter "h" to hold.',
            'game_tot_msg' : f'{self.player.name} — your current game-total is: {self.player.overall_total} ',
            'die_display' : f'You rolled a {self.roll}',
            'winner_msg' : f'We have a winner: {self.player.name}',
            'snake_eye' : f'Snake eye! {self.player.name} loses their turn and receives no points',
            's_e_g_t' : f'Your game total is STILL {self.player.overall_total}. Next up!',
            'hold_msg' : f'OK {self.player.name}, your game-total is {self.player.overall_total}',
            'invalid_cmd' : 'Must enter an \'r\' or \'h\'. Try again'
        }

        return msg_bank[msg]


    def turn(self, player):
        self.player = player
        player.turn_total = 0
        turn = True # when turn is False, becomes next player's turn

        if not self.is_game_over():
            while turn:
                print('-'*50)
                print(f'{player.name.upper()}\'s TURN')
                print(self.message(self.player, 'game_tot_msg')) # display basic player info at start of their turn
                print('and', self.message(self.player, 'turn_tot_msg'))

                choice = input(self.message(self.player, 'roll_prompt')) #retrieve choice
                
                if choice == 'r':
                    roll = die.roll()
                    
                    if roll != 1:
                        print(self.message(self.player, 'die_display', roll)) 
                        self.player.turn_total += roll

                        if not self.is_game_over():
                            print(self.message(self.player, 'turn_tot_msg'))
                        
                        else:
                            print(self.message(self.player, 'winner_msg'))

                    else:
                        print(self.message(self.player, 'snake_eye'))
                        print(self.message(self.player, 's_e_g_t'))
                        turn = False
                
                elif choice == 'h':
                    self.player.overall_total += self.player.turn_total

                    if not self.is_game_over():
                        print(self.message(self.player, 'hold_msg') + ' . . . NEXT!')
                        turn = False
                    
                    else:
                        print(self.message(self.player, 'hold_msg') + ' That means...')
                        print(self.message(self.player, 'winner_msg'))
                        turn = False
                        break

                else:
                    print(self.message(self.player, 'invalid_cmd'))                         
                # turn = False

                    
    def play(self):
        while not self.is_game_over():
            for p in self.players:
                self.turn(p)

                
        





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
        game.play()
        # print(p.name, p.species)
        # print(game.message(p, 'turn_tot_msg'))