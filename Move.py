#General movement class
class Movement:
    
    def __init__(self) -> None:
        pass
    
    def move(Tiles):
        pass
    
#Movement subclasses handle exactly how changing tiles should be handled 
class Move_Left(Movement):
    
    def move(Tiles):
        #Tiles move as much as possible from one tap in 2048, so a while loop checks if there's any more movement that can be done
        check = False
        while (check == False):
            #check tiles from left to right
            check = True
            for i in range(1,4):
                for j in range(4):
                    #Tiles can only be combined once per move, so they have a boolean to check if they already have
                    if (Tiles[i][j].value == Tiles[i-1][j].value and Tiles[i][j].value != 0 and Tiles[i-1][j].combined == False and Tiles[i][j].combined == False):
                        Tiles[i-1][j].update_value((Tiles[i-1][j].value)*2)
                        Tiles[i][j].update_value(0)
                        Tiles[i-1][j].update_combined()
                        check = False
                    elif (Tiles[i-1][j].value == 0 and Tiles[i][j].value != 0):
                        Tiles[i-1][j].update_value(Tiles[i][j].value)
                        Tiles[i][j].update_value(0)
                        check = False
        #Combination booleans are reset
        for i in range(4):
                for j in range(4):
                    if (Tiles[i][j].combined == True):
                        Tiles[i][j].update_combined()
                    

class Move_Right(Movement):
    
    def move(Tiles):
        check = False
        while (check == False):
            #Check tiles from right to left
            check = True
            for i in reversed(range(3)):
                for j in range(4):
                    if (Tiles[i][j].value == Tiles[i+1][j].value and Tiles[i][j].value != 0 and Tiles[i+1][j].combined == False and Tiles[i][j].combined == False):
                        Tiles[i+1][j].update_value((Tiles[i+1][j].value)*2)
                        Tiles[i][j].update_value(0)
                        Tiles[i+1][j].update_combined()
                        check = False
                    elif (Tiles[i+1][j].value == 0 and Tiles[i][j].value != 0):
                        Tiles[i+1][j].update_value(Tiles[i][j].value)
                        Tiles[i][j].update_value(0)
                        check = False
        for i in range(4):
                for j in range(4):
                    if (Tiles[i][j].combined == True):
                        Tiles[i][j].update_combined()

class Move_Up(Movement):
    
    def move(Tiles):
        check = False
        while (check == False):
            #Check tiles from top to bottom
            check = True
            for j in range(1,4):
                for i in range(4):
                    if (Tiles[i][j].value == Tiles[i][j-1].value and Tiles[i][j].value != 0 and Tiles[i][j-1].combined == False and Tiles[i][j].combined == False):
                        Tiles[i][j-1].update_value((Tiles[i][j-1].value)*2)
                        Tiles[i][j].update_value(0)
                        Tiles[i][j-1].update_combined()
                        check = False
                    elif (Tiles[i][j-1].value == 0 and Tiles[i][j].value != 0):
                        Tiles[i][j-1].update_value(Tiles[i][j].value)
                        Tiles[i][j].update_value(0)
                        check = False
        for i in range(4):
                for j in range(4):
                    if (Tiles[i][j].combined == True):
                        Tiles[i][j].update_combined()

class Move_Down(Movement):
    
    def move(Tiles):
        check = False
        while (check == False):
            #Check tiles from bottom to top
            check = True
            for j in reversed(range(3)):
                for i in range(4):
                    if (Tiles[i][j].value == Tiles[i][j+1].value and Tiles[i][j].value != 0 and Tiles[i][j+1].combined == False and Tiles[i][j].combined == False):
                        Tiles[i][j+1].update_value((Tiles[i][j+1].value)*2)
                        Tiles[i][j].update_value(0)
                        Tiles[i][j+1].update_combined()
                        check = False
                    elif (Tiles[i][j+1].value == 0 and Tiles[i][j].value != 0):
                        Tiles[i][j+1].update_value(Tiles[i][j].value)
                        Tiles[i][j].update_value(0)
                        check = False
        for i in range(4):
                for j in range(4):
                    if (Tiles[i][j].combined == True):
                        Tiles[i][j].update_combined()
