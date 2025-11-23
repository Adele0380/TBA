# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms

        jardin = Room("Jardin", "un jardin silencieux, presque figé, où chaque statue semble veiller sur les lieux depuis des siècles.")
        self.rooms.append(jardin)
        vestibule = Room("Vestibule", "un vaste vestibule où chaque bruit résonne trop fort, comme si quelque chose, quelque part caché dans l’ombre de cette immensité, écoutait.")
        self.rooms.append(vestibule)
        couloir_bleu = Room("Couloir bleu", "un couloir silencieux, bleu sombre, où chaque pas résonne comme un avertissement.")
        self.rooms.append(couloir_bleu)
        couloir_rouge = Room("Couloir rouge", "un long couloir rouge sombre, qui semble n'avoir aucune fin.")
        self.rooms.append(couloir_rouge)
        salle de banquet = Room("Salle de banquet", "une salle de banquet immense, où le moindre craquement du bois résonne comme un murmure inquiétant.")
        self.rooms.append(salle de banquet)
        bureau = Room("Bureau", "un bureau silencieux, où l’on croit entendre, par instants, le faible grincement d’un fauteuil pourtant immobile.")
        self.rooms.append(bureau)
        chambre_1 = Room("Chambre Laetitia", "une belle suite, parfaitement décorée, mais où un léger courant d'air sonnne comme une invitation à partir.")
        self.rooms.append(chambre_1)
        chambre_2 = Room("Chambre Victor", "une suite splendide où les coussins et les draps sont soigneusement disposés, mais où une impression d’observation persistante pèse dans l’air.")
        self.rooms.append(chambre_2)
        chambre_3 = Room("Chambre Madère", "une suite majestueuse, aux couleurs vives, richement décorée, comme si quelqu'un y vivait déjà.")
        self.rooms.append(chambre_3)
        chambre_4 = Room("Chambre Gwendoline", "une suite accueillante, où des fleurs séchées sont disposées sur le bureau et laissent un léger parfum d'antan.")
        self.rooms.append(chambre_4)
        chambre_5 = Room("Chambre François", "une suite élégante et sobre, où le temps semble figé.")
        self.rooms.append(chambre_5)
        cachot = Room("Cachot", "un cachot humide et étroit, où les murs suintants réverbèrent un écho sourd à chacun de vos pas.")
        self.rooms.append(cachot)
        tour_Est= Room("Tour Est", "une haute tour isolée, dont les fenêtres étroites laissent filtrer une faible lueur, difficile à distinguer du brouillard environnant.")
        self.rooms.append(tour_Est)
        tour_Ouest= Room("Tour Ouest", "une haute tour, où quelques pierres manquantes semblent avoir été les témoins d'un incident.")
        self.rooms.append(tour_Ouest)
        cuisine = Room("Cuisine", "une cuisine spacieuse aux grandes tables de bois massif, et aux belles casseroles en cuivre, où la lumière des lanternes se reflète doucement sur la pierre froide du sol.")
        self.rooms.append(cuisine)
        arrière_cour = Room("Arrière Cour", "une arrière cour pavée et entourée de grands arbres et d'une végétation luxuriante où un calme parfait règne.")
        self.rooms.appendarrière_Cour)
        atelier = Room("Atelier", "un atelier discret, encombré d’établis en bois massif et d’outils soigneusement rangés, où une fine couche de poussière atteste du temps écoulé.")
        self.rooms.append(atelier)
        chambre_au_trésor = Room("Chambre au trésor", "une chambre où l’or s’empile en silence, mais où chaque pas résonne avec un léger décalage, comme si quelqu’un marchait juste derrière vous.")
        self.rooms.append(chambre_au_trésor)
        escaliers_hall= Room("Escaliers hall", "l'entrée où deux escaliers symétriques s’élèvent de part et d’autre du hall, leurs marches de pierre polie s’enfonçant dans une pénombre silencieuse.")
        self.rooms.append(escaliers_hall)
        escalier_Est = Room("Escalier_Est", "un escalier élégant, recouvert d’un tapis richement brodé")
        self.rooms.append(escalier_Est)
        escalier_Ouest = Room("Escalier_Ouest", "un escalier en parquet, soigneusement ciré")
        self.rooms.append(escalier_Ouest)
        escalier_rdc = Room("Escaliers_RDC", "un vieil escalier, dont l'obscurité en cache la sortie")
        self.rooms.append(escalier_rdc)
        cabanon = Room("Cabanon", "un vieil escalier, dont l'obscurité en cache la sortie")
        self.rooms.append(cabanon)
        atelier_couture = Room("Atelier de couture", "un vieil escalier, dont l'obscurité en cache la sortie")
        self.rooms.append(atelier_couture)
        atelier_peinture = Room("Atelier de peinture", "un vieil escalier, dont l'obscurité en cache la sortie")
        self.rooms.append(atelier_peinture)

        # Create exits for rooms
        
        L1=["Chambre 1", "Chambre 2", "Chambre 3"]
        L2=["Chambre 5", "Salle de peinture", "Atelier de couture"]
        Jardin.exits = {"N" : Vestibule, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None }
        Vestibule.exits = {"N" : Escaliers, "E" : Salle de banquet, "S" : Jardin, "O" : Salon, "U" : None, "D" : None }
        Couloir1.exits = {"N" : Arrière cour, "E" : atelier, "S" : couloir1, "O" : Cabanon, "U" : None, "D" : None }
        Couloir2.exits = { "N" :,"S" :,"E" :,"O" :,"U" :,"D" :}
        Salle de banquet.exits = {"N" : None, "E" : None, "S" : None, "O" : Vestibule, "U" : None, "D" : None }
        Bureau.exits = {"N" : None, "E" : Escalier0, "S" : None, "O" : Couloir1, "U" : None , "D" : None }
        Suites.exits = {"N" : forest, "E" : swamp, "S" : None, "O" : None, "U" :, "D" : }
        Cachot.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : Escalier hall, "D" : None}
        Tour1.exits = { "N" : None ,"S" : None ,"E" : None,"O" : None,"U" : None,"D" : Escalier1 }
        Tour2.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : Escalier2 }
        Cuisine.exits = {"N" : None, "E" : None, "S" : Salle de banquet, "O" : Escalier hall, "U" : None, "D" : None }
        Arrière cour.exits = {"N" : None, "E" : Atelier, "S" : Couloir1, "O" : Cabanon, "U" : None, "D" : None }
        Atelier.exits = {"N" : None, "E" : None, "S" : None, "O" : Arrière cour, "U" : None, "D" : None }
        Chambre au trésor.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : Escalier0, "D" : None }
        Escaliers hall.exits = {"N" : Couloir1, "E" : Cuisine, "S" : Vestibule, "O" : Sallon, "U" : Couloir2, "D" : Cachot}
        Quartiers.exits = { "N" : Sallon,"S" : None,"E" : None,"O" : None,"U" : None,"D" : None }
        Bibliothèque.exits = { "N" : None,"S" :Sallon ,"E" :Couloir1,"O" : None,"U" : None,"D" :None}
        Sallon.exits = { "N" : Bibliothèque,"S" : Quartiers,"E" :Escalier hall ,"O" :None ,"U" :None ,"D" : None }
        Atelier couture.exits = 
        Salle de peinture.exits = 
        Escalier1.exits = { "N" : None,"S" : None,"E" : None,"O" : None,"U" : Tour1,"D" : None }
        Escalier2.exits = { "N" :,"S" :,"E" :,"O" :,"U" : Tour2,"D" : None }
        Escalier0.exits = { "N" : None,"S" : None ,"E" : None ,"O" : Bureau,"U" : None,"D" : Chambre au trésor}
        Cabanon.exits = { "N" : None,"S" : None,"E" : Arrière cour,"O" : None,"U" : None,"D" : None}

#{ "N" :,"S" :,"E" :,"O" :,"U" :,"D" :}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = swamp

    # Play the game     
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split()

        if not list_of_words :
            return

        command_word = list_of_words[0].lower()

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    
def main():
    # Create a game object and play the game
    Game().play()

if __name__ == "__main__":
    main()
