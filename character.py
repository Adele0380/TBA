class character:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.current_room = None
        self.msgs = []

    def __str__(self):
        return f"{self.name} : {self.description}"