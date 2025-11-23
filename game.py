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

        Jardin = Room("Jardin", "un jardin silencieux, presque figé, où chaque statue semble veiller sur les lieux depuis des siècles.")
        self.rooms.append(Jardin)
        Vestibule = Room("Vestibule", "un vaste vestibule où chaque bruit résonne trop fort, comme si quelque chose, quelque part caché dans l’ombre de cette immensité, écoutait.")
        self.rooms.append(Vestibule)
        Couloir = Room("Couloir", "un couloir silencieux où chaque pas résonne comme un avertissement")
        self.rooms.append(Couloir)
        Salle de banquet = Room("Salle de banquet", "une salle de banquet immense, où le moindre craquement du bois résonne comme un murmure inquiétant.")
        self.rooms.append(Salle de banquet)
        Bureau = Room("Bureau", "un bureau silencieux, où l’on croit entendre, par instants, le faible grincement d’un fauteuil pourtant immobile.")
        self.rooms.append(Bureau)

        
        Suites = Room("Suites", "un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(Suites)
        Cachot = Room("Cachot", "une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(Cachot)
        Tour = Room("Tour", "une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(Tour)
        Cuisine = Room("Cuisine", "une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(Cuisine)
        Arrière cour = Room("Arrière Cour", "une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(Arrière Cour)
        Atelier = Room("Atelier", "une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(Atelier)
        Chambre au trésor = Room("Chambre au trésor", "une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(Chambre au trésor)
        Escaliers = Room("Escaliers", "une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(Escaliers)

        # Create exits for rooms

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
