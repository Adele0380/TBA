# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.dark = False 
        self.locked = False
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties:" 
        for direction, door in self.exits.items():
            if door is not None:
                exit_string += direction + ", "
        return exit_string.strip(", ")

    def get_inventory(self):
        if not self.inventory:
            return "\nIl n'y a rien ici.\n"
        lines = ["\nLa pièce contient :"]
        for item in self.inventory.values():
            lines.append(f"    - {item}")
        return "\n".join(lines)+"\n"

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"
