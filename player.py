# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}

    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]
        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        if self.current_room is not None:
            self.history.append(self.current_room)
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        print(self.current_room.get_inventory())

        hist = self.get_history()
        if hist != "":
            print(hist)
            print()

        return True

    def get_history(self):
        if not self.history:
            return ""
        lines = ["\nVous avez déja visité les pièces suivantes:"]
        for room in self.history:
            lines.append(f"    - {room.description}")
        return "\n".join(lines)

    def get_inventory(self):
        if not self.inventory:
            return "Votre inventaire est vide."
        lines = ["Vous disposez des objets suivants :"]
        for item in self.inventory.values():
            lines.append(f"    - {item}")
        return "\n".join(lines)
    
    def back(self):
    # Si l'historique est vide, on ne peut pas revenir en arrière
        if len(self.history) == 0:
            print("\nVous ne pouvez pas revenir en arrière : aucun déplacement précédent.\n")
            return False

        # On récupère la dernière pièce visitée (structure de pile : LIFO)
        previous_room = self.history.pop()
        self.current_room = previous_room

        # On affiche la description complète de la pièce
        print(self.current_room.get_long_description())

        # On réaffiche l'historique mis à jour
        hist = self.get_history()
        if hist != "":
            print(hist)
            print()

        return True

