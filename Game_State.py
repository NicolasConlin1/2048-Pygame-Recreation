#General game state class
class Game_State:
    
    #Set's up the connected context class
    def __init__(self, input_context) -> None:
        self.context = input_context
    
    def change_state(self, type):
        pass
   
#Different types of states determine how the game runs and what state is transfered into if a change occurs    
class Game_Over(Game_State):
    
    #Type is left unused for states that don't use it so there are fewer opportunities for mistakes in main
    def change_state(self, type):
        self.context.current = self.context.running
    
class Paused(Game_State):
    
    def change_state(self, type):
        self.context.current = self.context.running
    
class Running(Game_State):
    
    #Running can go to paused or game over so it's checked here
    def change_state(self, type):
        if (type == 0):
            self.context.current = self.context.paused
        elif (type == 1):
            self.context.current = self.context.gameOver
 
#Context class for handling states       
class State_Context:
    
    #States are created and the current one (always starts as running) is selected
    def __init__(self):
        self.gameOver = Game_Over(self)
        self.running = Running(self)
        self.paused = Paused(self)
        self.current = self.running
        
    #Changes the state based on what the current one is
    def state_change(self, type):
        self.current.change_state(type)