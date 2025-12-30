# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)

        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        raw_direction = list_of_words[1]
        # Normalisation : tout en majuscules
        direction = raw_direction.upper()

        # Définition de equivalences
        equivalences = {
            "N": "N",
            "NORD": "N",
            "E": "E",
            "EST": "E",
            "S": "S",
            "SUD": "S",
            "O": "O",
            "OUEST": "O",
            "U" : "U",
            "UP" : "U",
            "D" : "D",
            "DOWN" : "D",
        }

        # Vérification que la direction est valide
        if direction not in equivalences:
            current_room = player.current_room
            print(f"\nDirection '{raw_direction}' non reconnue.\n")
            print(f"Vous êtes dans {current_room.description}\n")
            print(f"Vous appercevez '{current_room.cha}")
            print(current_room.get_exit_string())
            return False

        # Direction normalisée (N, E, S, O, U, D)
        direction_normale = equivalences[direction]

        # Move the player in the direction specified by the parameter.
        player.move(direction_normale)
        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    def history(game, list_of_words, number_of_parameters):
        """Affiche l'historique des salles visitées."""
        l = len(list_of_words)
        # Vérification du nombre de paramètres
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        hist = game.player.get_history()

        if hist == "":
            print("\nAucun historique pour l’instant.\n")
        else:
            print("\n" + hist + "\n")

        return True

    def back(game, list_of_words, number_of_parameters):
        """Revenir à la pièce précédemment visitée."""
        l = len(list_of_words)
        
        # Vérification du nombre de paramètres
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        return game.player.back()

    def look(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG0.format(command_word=list_of_words[0]))
            return False

        player = game.player
        room = player.current_room

        if room.dark and "torche" not in player.inventory:
            print("\nIl fait trop sombre pour voir quoi que ce soit...\n")
            return True

        print(room.get_long_description())
        print(room.get_inventory())
        print(room.get_characters())
        return True


    def take(game, list_of_words, number_of_parameters):
        """Ajouter des items dans l'inventaire du joueur et le retirer de la pièce."""
        l = len(list_of_words)
        # Vérification du nombre de paramètres
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        item_name = list_of_words[1]

        return game.player.take(item_name)

    def drop(game, list_of_words, number_of_parameters):
        """Retirer des items dans l'inventaire du joueur et l'ajouter à la pièce."""
        l = len(list_of_words)
        # Vérification du nombre de paramètres
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        item_name = list_of_words[1]
        return game.player.drop(item_name)

    def check(game, list_of_words, number_of_parameters):
        """Affiche la description de l'inventaire du joueur."""
        l = len(list_of_words)
        # Vérification du nombre de paramètres
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        print("\n" + game.player.get_inventory() + "\n")
        return True

        player = game.player

        # On délègue le travail à la méthode back() du joueur
        return player.back()
    
    def charge(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG0.format(command_word=list_of_words[0]))
            return False

        player = game.player

        if "beamer" not in player.inventory:
            print("\nVous n'avez pas de beamer.\n")
            return False

        player.beamer_room = player.current_room
        print("\nLe beamer est chargé.\n")
        return True

    def use(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG1.format(command_word=list_of_words[0]))
            return False

        player = game.player
        item_name = list_of_words[1].lower()

        if item_name not in player.inventory:
            print(f"\nVous n'avez pas {item_name}.\n")
            return False

    # --- BEAMER ---
        if item_name == "beamer":
            if player.beamer_room is None:
                print("\nLe beamer n'est pas chargé.\n")
                return False

            player.current_room = player.beamer_room
            print("\nTéléportation réussie !\n")
            print(player.current_room.get_long_description())
            return True

    # --- POTION ---
        if item_name == "potion":
            if player.health == player.max_health:
                print("\nVous êtes déjà en pleine santé.\n")
                return False

            player.health = min(player.max_health, player.health + 5)
            player.inventory.pop("potion")

            print(f"\nVous buvez la potion. Santé : {player.health}/{player.max_health}\n")
            return True

        print("\nVous ne pouvez pas utiliser cet objet.\n")
        return False

    def unlock(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG1.format(command_word=list_of_words[0]))
            return False

        player = game.player
        room = player.current_room
        direction = list_of_words[1].upper()

        door = room.exits.get(direction)
        if door is None:
            print("\nIl n'y a pas de porte dans cette direction.\n")
            return False

        if not door.locked:
            print("\nLa porte est déjà ouverte.\n")
            return True

    # Vérifier la clé requise
        needed = door.key_name  # ex: "clef"
        if needed is None:
            print("\nCette porte ne peut pas être déverrouillée.\n")
            return False

        if needed not in player.inventory:
            print(f"\nIl vous faut '{needed}' pour ouvrir cette porte.\n")
            return False

        door.locked = False
        print("\nVous déverrouillez la porte.\n")
        return True

    