import random
from Rocket import Rocket
from Tenk import Tenk
class Brod(Rocket):
    # Igra brod simulira ratni brod , ali zapravo koristi sve metode rakete
    # pa ga možemo zvati simulacija rakete
    def __init__(self, x=0, y=0, route = 0):
        super().__init__(x, y)
        self.route = route
    
    def display_title_bar(self):
        # prikazujemo glavni naslov igre korisniku
        print("\t****************************")
        print("\t*** Igra - Borba brodova ***")
        print("\t****************************")
    
    def get_user_choice(self):
        # pokazujemo korisniku meni i pitamo ga što želi napraviti te vracamo aplikaciji njegov odgovor
        print("\n[1] Pokreni borbu Tenkova.")
        print("\n[2] Pokreni borbu Brodova.")
        print("[x] Izlaz.")
        
        return input("Odaberite što želite napraviti!?")
    
    def fight(self):
        # kreiram nekoliko brodova i raketa s pozicijama slučajnog odabira (biblioteka random)
        # tenkovi imaju random broj odrađenih/napravljenih ruta na ratnom polju
        brodNum = int(input("Unesite broj brodova na ratnom polju:")) # upisao broj 5
        brod = []
        rockets = []
        for x in range(0,brodNum): # for petlja se vrti od 0 do 5
            x = random.randint(0,100)
            y = random.randint(1,100)
            self.route = random.randint(0,10)
            brod.append(Brod(x,y,self.route))
        
        for x in range(0, brodNum): # for petlja se vrti od 0 do 5
            x = random.randint(0, 100)
            y = random.randint(1,100)
            rockets.append(Rocket(x, y))
        
        # prikazivanje/ispis napravljene rute svakog broda u listi na ratnom polju
        for index, brod in enumerate(brod):
            print("Brod {} je napravio {} rutu/e".format(index+1, brod.route))
        
        print("\n")
        yourBrod = int(input("Od {} brodova, vaš brod je pod brojem:".format(brodNum)))
        
        chosenBrod = brod[yourBrod-1]
        # prikazivanje/ispis udaljenosti vašeg broda i ostalih brodova
        for index, brod
         in enumerate(brod):
            distance = chosenBrod.get_distance(brod)
            print("Vaš brod je udaljen {} kilometara od brod broj {}.".format(distance, index+1))
        
        print("\n")
        # prikazivanje/ispis udaljenosti vašeg broda od raketa u listi raketa
        for index, Rocket in enumerate(rockets):
            distance = chosenBrod.get_distance(rocket)
            print("Vaš brod je udaljen {} kilometara od rakete broj {}.".format(distance, index+1))
        
    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            # na temelju korisnikova odabira izvršavamo programsku logiku naše igrice ovisno o tome
            #što je korisnik odabrao
            self.display_title_bar()
            if choice == '1':
                self.fight()
            elif choice == 'x':
                print("\nHvala na igri i poštenoj borbi :) . Pozdrav.")
            else:
                print("\nGreška - napravite hvatanje izuzetaka za zadaću.\n")
    
if __name__ == "__main__":
    game = Brod()
    game.play() 
        
        