# prvo pretvorimo stringove (tekst) u brojeve i rješavanje s modulom, a to znači (igrač_1 - računalo_igrač_2)%5...ostatak 1 ili 2 - Win igrač_1...3, 4 Win računalo_igrač_2..0 neriješeno
# "rock", "Spock", "paper", "lizard", "scissors" pretvoriti u sljedeće brojeve:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random
from rpslsError import RpslsError
class Rpsls:
    def __init__(self):
        self.player_input = None
        self.player_number = -1
        self.computer_number = -1
        self.computer_choice_name = None
        self.num_round = 1
        
    def broj_u_string(self):
        """
        pretvara brojeve (0, 1, 2, 3, 4) u nazive/tekst (rock, Spock, paper, lizard, scissors)
        """
        if self.computer_number == 0:
            self.computer_choice_name = "rock"
        elif self.computer_number == 1:
            self.computer_choice_name = "Spock"
        elif self.computer_number == 2:
            self.computer_choice_name = "paper"
        elif self.computer_number == 3:
            self.computer_choice_name = "lizard"
        elif self.computer_number == 4:
            self.computer_choice_name = "scissors"
        else:
            self.computer_choice_name = None
            raise RpslsError(103)
        return self.computer_choice_name
    
       
    def string_u_broj(self):
        """
        pretvara naziv/tekst (rock, Spock, paper, lizard, scissors) u broj (0, 1, 2, 3, 4)
        """
        if self.player_input == "rock":
            self.player_number = 0
        elif self.player_input == "spock":
            self.player_number = 1
        elif self.player_input == "paper":
            self.player_number = 2
        elif self.player_input == "lizard":
            self.player_number = 3
        elif self.player_input == "scissors":
            self.player_number = 4
        else:
            self.player_number = -1
            raise RpslsError(101)
        return self.player_number

    def play(self):
        #korisnik i računalo igraju ti runde
        computer = random.randint(1, 3)
        # unos korisnikovog tekst
        self.player_input = input("Odaberite rock, spock, paper, lizard ili scissors: ").lower()
        # pretvorba korisnikovog tekst u broj
        self.player_number = self.string_u_broj()
        # racunalo odabire pomocu random metode
        self.computer_number = random.randrange(0,5)
        ostatak = (self.player_number - self.computer_number)%5
        if(self.player_number == -1):
            winner = "Greška"
            raise RpslsError(000)
        else:
            if ostatak == 0:
                winner = "Neriješeno"
            elif ostatak == 1 or ostatak == 2:
                winner = "Vi (čovjek) pobjeđujete"
            elif ostatak == 3 or ostatak == 4:
                winner = "Računalo pobjeđuje"
        self.computer_choice_name = self.broj_u_string()
        print("Vi (čovjek) ste odabrali: {}".format(self.player_input.title()))
        print("Računalo je odabralo: {}".format(self.computer_choice_name.title()))
        print(winner)
        
if __name__ == "__main__":
    game = Rpsls()
    game.play()
        
        
            

        
        
        