# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}
        self.max_weight = 15

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

    def take(self, item_name: str):
        """Prend un objet dans la pièce et le met dans l'inventaire du joueur."""
        room = self.current_room

        if item_name not in room.inventory:
            print(f"\nIl n'y a pas '{item_name}' dans cette pièce.\n")
            return False

        item = room.inventory[item_name]
        if self.total_weight() + item.weight > self.max_weight:
            print(f"\nIl est impossible de prendre {item_name} : trop lourd "
                  f"({self.total_weight()} + {item.weight} > {self.max_weight}).\n")
            return False

        self.inventory[item_name] = room.inventory.pop(item_name)
        print(f"\nVous avez pris l'objet {item}.\n")
        return True

    def drop(self, item_name: str):
        """Prend un objet dans l'inventaire et le met dans la pièce."""
        
        room = self.current_room
        if item_name not in self.inventory:
            print(f"\nIl n'y a pas '{item_name}' dans votre inventaire.\n")
            return False
        
        # On le met dans l'inventaire du joueur
        item = self.inventory[item_name]
        room.inventory[item_name] = self.inventory.pop(item_name)

        print(f"\nVous avez déposé {item}.\n")
        return True

    def total_weight(self):
        return sum(item.weight for item in self.inventory.values())


