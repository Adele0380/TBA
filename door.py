# door.py
class Door:
    def __init__(self, destination, locked=False, key_name=None):
        self.destination = destination      
        self.locked = locked                
        self.key_name = key_name   
