# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item

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
        history = Command("history", " : afficher l'historique des pièces visitées", Actions.history, 0)
        self.commands["history"] = history
        back = Command("back", " : revenir en arrière", Actions.back, 0)
        self.commands["back"] = back
        look = Command("look", " : décrire la pièce et les objets présents", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " <item> : prendre un objet dans la pièce", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " <item> : deposer un objet dans la pièce", Actions.drop, 1)
        self.commands["drop"] = drop
        check = Command("check", " : décrire les objets présents dans l'inventaire du joueur", Actions.check, 0)
        self.commands["check"] = check

        # Setup rooms

        jardin = Room("Jardin", "un jardin silencieux, presque figé, où chaque statue semble veiller sur les lieux depuis des siècles.")
        self.rooms.append(jardin)
        vestibule = Room("Vestibule", "un vaste vestibule où chaque bruit résonne trop fort, comme si quelque chose, quelque part caché dans l’ombre de cette immensité, écoutait.")
        self.rooms.append(vestibule)
        couloir_bleu = Room("Couloir bleu", "un couloir silencieux, bleu sombre, où chaque pas résonne comme un avertissement.")
        self.rooms.append(couloir_bleu)
        couloir_rouge = Room("Couloir rouge", "un long couloir rouge sombre, qui semble n'avoir aucune fin.")
        self.rooms.append(couloir_rouge)
        couloir_vert = Room("Couloir vert", "un couloir d'un vert profond, rendant l'atmosphère intimidante")
        self.rooms.append(couloir_vert)
        salle_de_banquet = Room("Salle de banquet", "une salle de banquet immense, où le moindre craquement du bois résonne comme un murmure inquiétant.")
        self.rooms.append(salle_de_banquet)
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
        tour_est= Room("Tour Est", "une haute tour isolée, dont les fenêtres étroites laissent filtrer une faible lueur, difficile à distinguer du brouillard environnant.")
        self.rooms.append(tour_est)
        tour_ouest= Room("Tour Ouest", "une haute tour, où quelques pierres manquantes semblent avoir été les témoins d'un incident.")
        self.rooms.append(tour_ouest)
        cuisine = Room("Cuisine", "une cuisine spacieuse aux grandes tables de bois massif, et aux belles casseroles en cuivre, où la lumière des lanternes se reflète doucement sur la pierre froide du sol.")
        self.rooms.append(cuisine)
        arrière_cour = Room("Arrière Cour", "une arrière cour pavée et entourée de grands arbres et d'une végétation luxuriante où un calme parfait règne.")
        self.rooms.append(arrière_cour)
        atelier = Room("Atelier", "un atelier discret, encombré d’établis en bois massif et d’outils soigneusement rangés, où une fine couche de poussière atteste du temps écoulé.")
        self.rooms.append(atelier)
        chambre_au_trésor = Room("Chambre au trésor", "une chambre où l’or s’empile en silence, mais où chaque pas résonne avec un léger décalage, comme si quelqu’un marchait juste derrière vous.")
        self.rooms.append(chambre_au_trésor)
        escalier_hall= Room("Escalier hall", "un escalier divisés en deux parties symétriques s’élevant de part et d’autre du hall, leurs marches de pierre polie s’enfonçant dans une pénombre silencieuse.")
        self.rooms.append(escalier_hall)
        escalier_est = Room("Escalier_Est", "un escalier élégant, recouvert d’un tapis richement brodé")
        self.rooms.append(escalier_est)
        escalier_ouest = Room("Escalier_Ouest", "un escalier en parquet, soigneusement ciré")
        self.rooms.append(escalier_ouest)
        escalier_rdc = Room("Escaliers_RDC", "un vieil escalier, dont l'obscurité en cache la sortie")
        self.rooms.append(escalier_rdc)
        cabanon = Room("Cabanon", "un vieil escalier, dont l'obscurité en cache la sortie")
        self.rooms.append(cabanon)
        atelier_couture = Room("Atelier de couture", "un vieil escalier, dont l'obscurité en cache la sortie")
        self.rooms.append(atelier_couture)
        atelier_peinture = Room("Atelier de peinture", "un vieil escalier, dont l'obscurité en cache la sortie")
        self.rooms.append(atelier_peinture)
        couloir_vert_est = Room("Couloir vert Est", "le couloir vert Est face à trois chambres : Victor, Madère, Gwendoline")
        self.rooms.append(couloir_vert_est)
        couloir_vert_ouest = Room("Couloir vert Ouest", "le couloir vert Ouest où se trouvent trois salles : chambre François, salle de peinture et l'atelier de couture.")
        self.rooms.append(couloir_vert_ouest)
        bibliothèque = Room("Bibiothèque", "une bibliothèque majestueuse, où certains ouvrages ont été laissés entrouverts, comme interrompus au milieu d’une dernière lecture.")
        self.rooms.append(bibliothèque)
        salon = Room("Salon", "un salon décoré de tableaux anciens, dont les regards peints paraissent suivre discrètement les mouvements des visiteurs.")
        self.rooms.append(salon)
        quartiers = Room("Quartiers", "des quartiers silencieux, alignés le long d’un couloir étroit, où chaque porte close semble dissimuler une présence endormie.")
        self.rooms.append(quartiers)

        clefs = Item("clefs", "un bouclier léger et résistant", 1)
        manuscrit = Item("manuscrit", "un casque en métal (1 kg)", 1)
        coffret_souvenirs = Item("coffret_souvenirs", "un bouclier léger et résistant", 1)
        dague = Item("dague", "un casque en métal (1 kg)", 1)
        bougies = Item("bougies", "un bouclier léger et résistant", 1)
        allumettes = Item("allumettes", "un casque en métal (1 kg)", 1)
        pistolet = Item("pistolet", "un bouclier léger et résistant", 1)
        miroir = Item("miroir", "un casque en métal (1 kg)", 1)
        portrait_familial = Item("portrait_familial", "un bouclier léger et résistant", 1)
        horloge = Item("horloge", "un casque en métal (1 kg)", 1)
        boite_à_musique = Item("boite_à_musique", "un bouclier léger et résistant", 1)
        carte_postale = Item("carte_postale", "un casque en métal (1 kg)", 1)
        fiole_de_parfum = Item("fiole_de_parfum", "un bouclier léger et résistant", 1)

        # Create exits for rooms
        
        jardin.exits = {"N" : vestibule, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None }
        vestibule.exits = {"N" : escalier_hall, "E" : salle_de_banquet, "S" : jardin, "O" : None, "U" : None, "D" : None }
        couloir_bleu.exits = {"N" : arrière_cour, "E" : bureau, "S" : escalier_hall, "O" : bibliothèque, "U" : None, "D" : None }
        couloir_rouge.exits = { "N" : couloir_vert,"S" : escalier_hall,"E" :escalier_est,"O" :escalier_ouest,"U" : None,"D" : None}
        couloir_vert.exits = { "N" : chambre_1,"S" : couloir_rouge,"E" : couloir_vert_est,"O" : couloir_vert_ouest,"U" : None,"D" : None}
        salle_de_banquet.exits = {"N" : None, "E" : None, "S" : None, "O" : vestibule, "U" : None, "D" : None }
        bureau.exits = {"N" : None, "E" : escalier_rdc, "S" : None, "O" : couloir_bleu, "U" : None , "D" : None }
        cachot.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : escalier_hall, "D" : None}
        tour_est.exits = { "N" : None ,"S" : None ,"E" : None,"O" : None,"U" : None,"D" : escalier_est }
        tour_ouest.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : escalier_ouest }
        cuisine.exits = {"N" : None, "E" : None, "S" : salle_de_banquet, "O" : escalier_hall, "U" : None, "D" : None }
        arrière_cour.exits = {"N" : None, "E" : atelier, "S" : couloir_bleu, "O" : cabanon, "U" : None, "D" : None }
        atelier.exits = {"N" : None, "E" : None, "S" : None, "O" : arrière_cour, "U" : None, "D" : None }
        chambre_au_trésor.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : escalier_rdc, "D" : None }
        escalier_hall.exits = {"N" : couloir_bleu, "E" : cuisine, "S" : vestibule, "O" : salon, "U" : couloir_rouge, "D" : cachot}
        quartiers.exits = { "N" : salon,"S" : None,"E" : None,"O" : None,"U" : None,"D" : None }
        bibliothèque.exits = { "N" : None,"S" :salon ,"E" :couloir_bleu,"O" : None,"U" : None,"D" :None}
        salon.exits = { "N" : bibliothèque,"S" : quartiers,"E" :escalier_hall ,"O" :None ,"U" :None ,"D" : None }
        atelier_couture.exits = { "N" : None,"S" : None,"E" :couloir_vert ,"O" :None ,"U" :None ,"D" : None }
        atelier_peinture.exits = { "N" : None,"S" : None,"E" :couloir_vert ,"O" :None ,"U" :None ,"D" : None }
        escalier_est.exits = { "N" : None,"S" : None,"E" : None,"O" : couloir_rouge,"U" : tour_est,"D" : None }
        escalier_ouest.exits = { "N" : None,"S" : None,"E" : couloir_rouge,"O" : None,"U" : tour_ouest,"D" : None }
        escalier_rdc.exits = { "N" : None,"S" : None ,"E" : None ,"O" : bureau,"U" : None,"D" : chambre_au_trésor}
        cabanon.exits = { "N" : None,"S" : None,"E" : arrière_cour,"O" : None,"U" : None,"D" : None}
        couloir_vert_est.exits = { "N" : chambre_3,"S" : couloir_vert,"E" : chambre_4,"O" : chambre_2,"U" : None,"D" : None}
        couloir_vert_ouest.exits = { "N" : atelier_peinture,"S" : couloir_vert,"E" : atelier_couture,"O" : chambre_5,"U" : None,"D" : None}

        bureau.inventory["clefs"] = clefs
        bibliothèque.inventory["manuscrit"] = manuscrit
        salle_de_banquet.inventory["coffret_souvenirs"] = coffret_souvenirs
        tour_ouest.inventory["dague"] = dague
        couloir_vert_ouest.inventory["allumettes"] = allumettes
        couloir_vert_ouest.inventory["bougies"] = bougies
        chambre_3.inventory["pistolet"] = pistolet
        couloir_rouge.inventory["miroir"] = miroir
        salon.inventory["portrait_familial"] = portrait_familial
        salle_de_banquet.inventory["horloge"] = horloge
        atelier_couture.inventory["boite_à_musique"] = boite_à_musique
        chambre_1.inventory["fiole_de_parfum"] = fiole_de_parfum
        quartiers.inventory["carte_postale"] = carte_postale

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = jardin

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
        print(self.player.current_room.get_inventory())

    
def main():
    # Create a game object and play the game
    Game().play()

if __name__ == "__main__":
    main()
