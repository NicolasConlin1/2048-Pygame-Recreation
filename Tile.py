#Tile class to handle each square on the board
class Tile:
    
    def __init__(self, x, y, v):
        self.x_coord = x
        self.y_coord = y
        self.value = v
        #Default color for blank tiles
        self.color = [187, 173, 160]
        self.combined = False
    

        
    #Updates the value of the tile
    def update_value(self, value):
        self.value = value
        if (value == 0):
            self.color = [187, 173, 160]
        else:
            #Color for tiles in use (ones with a value)
            self.color = [160,160,160]
    
    #Updates if a tile has already been combined this turn, used to make movement accurate to the og game in Move.py
    def update_combined(self):
        if (self.combined == True):
            self.combined = False
        else:
            self.combined = True