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
        import random
        return random.choice(self.msgs)

    def move(self):
        import random
        if self.current_room is None:
            return
        exits = [d for d in self.current_room.exits.keys() if self.current_room.exits[d] is not None and not self.current_room.exits[d].locked]
        if not exits:
            return
        direction = random.choice(exits)
        door = self.current_room.exits[direction]
        # Remove from current room
        for key, char in list(self.current_room.characters.items()):
            if char == self:
                del self.current_room.characters[key]
                break
        # Move
        self.current_room = door.destination
        # Add to new room
        self.current_room.characters[self.name.lower().replace(" ", "_")] = self