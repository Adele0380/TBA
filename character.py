import random

DEBUG = True

class Character:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.current_room = None
        self.msgs = []

    def __str__(self):
        return f"{self.name} : {self.description}"

    def get_msg(self):
        if not self.msgs:
            return "Je n'ai rien à dire."
        # Récupérer le premier message et le retirer de la liste
        msg = self.msgs.pop(0)
        # Ré-ajouter le message à la fin pour l'affichage cyclique
        self.msgs.append(msg)
        return msg

    def move(self):

    # Pas de pièce -> pas de déplacement
        if self.current_room is None:
            return False

    # 1 chance sur 2 de rester sur place
        if random.choice([True, False]) is False:
            return False

    # Liste des directions possibles (portes existantes + non verrouillées)
        possible_dirs = [
            d for d, door in self.current_room.exits.items()
            if door is not None and not door.locked
        ]

        if not possible_dirs:
            return False

        direction = random.choice(possible_dirs)
        door = self.current_room.exits[direction]

    # Retirer le PNJ de la salle courante
        if hasattr(self.current_room, "characters"):
            for key, char in list(self.current_room.characters.items()):
                if char is self:
                    del self.current_room.characters[key]
                    break

    # Se déplacer
        self.current_room = door.destination
        if DEBUG:
            print(f"DEBUG: PNJ {self.name} tente de bouger")

    # Ajouter le PNJ à la nouvelle salle
        if hasattr(self.current_room, "characters"):
            self.current_room.characters[self.name.lower().replace(" ", "_")] = self
        if DEBUG:
            print(f"DEBUG: PNJ déplacé vers {self.current_room.name}")

        return True
