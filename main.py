from xml.etree.ElementInclude import include

import pygame
import pygame_menu
import sys
import random
import Tile
import Move
import Logger_Singleton
import Game_State

#Log is used outside of the game (highscore menu) and within it so it's initialized here
Log = Logger_Singleton.Logger_Singleton("highscore.txt")

# pygame main menu
def main_menu():
    pygame.init()
    surface = pygame.display.set_mode((800, 1000))
    menu = pygame_menu.Menu('Welcome', 800, 1000, theme=pygame_menu.themes.THEME_ORANGE)
    menu.add.label('2048 Game', font_size = 100)
    menu.add.button('Start Game', initialize_game)
    menu.add.button('Read Tutorial', tutorial_menu)
    menu.add.button('Highscore', highscore_menu)
    menu.add.button('Exit', pygame_menu.events.EXIT)
    menu.mainloop(surface)

#Tutorial
def tutorial_menu():
    pygame.init()
    surface = pygame.display.set_mode((800, 800))
    menu = pygame_menu.Menu('Tutorial', 800, 800, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.label('Welcome to 2048!', font_size = 50)
    menu.add.label('Your goal is to make a tile with the highest value possible', font_size = 25)
    menu.add.label('Use the ARROW KEYS to move the tiles up, down, left, and right', font_size = 25)
    menu.add.label('Tiles of the same value will combine into a tile with double the value', font_size = 25)
    menu.add.label('Tiles with a value of 2 will be added every turn if possible', font_size = 25)
    menu.add.label('Use M to return to main menu during the game', font_size = 25)
    menu.add.label('Use R to restart prior to a Game Over', font_size = 25)
    menu.add.label('Use SPACE to pause and unpause', font_size = 25)
    menu.add.label('Use ESC to quit', font_size = 25)
    menu.add.button('Back', main_menu)
    menu.mainloop(surface)
    
#Highscore
def highscore_menu():
    pygame.init()
    surface = pygame.display.set_mode((800, 800))
    menu = pygame_menu.Menu('Highscore', 800, 800, theme=pygame_menu.themes.THEME_GREEN)
    menu.add.label('Current Highcore: ' + str(Log.read_score()), font_size = 75)
    menu.add.button('Reset', reset_score)
    menu.add.button('Back', main_menu)
    menu.mainloop(surface)
    
#Used to refresh the page after resetting the highscore so that the old one is no longer displayed 
def reset_score():
    Log.reset_score()
    highscore_menu()

#The game is initialized and played here
def initialize_game():
    # Initialize game and create a screen object.
    screen = pygame.display.set_mode((800, 1000))
    pygame.display.set_caption("2048")
    pygame.font.init()
    #A general font for the tiles is initialized
    font = pygame.font.Font(pygame.font.get_default_font(), 75)
    #Tiles are initialized and 2 tiles are randomly set from free to '2'
    Tiles = initialize_tiles()
    add_tile(Tiles)
    add_tile(Tiles)
    #Initialize the game state
    state = Game_State.State_Context()
    pygame.event.clear()
    # draw the board
    draw_board(screen, Tiles, font, state)
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and state.current == state.running:
                    Move.Move_Left.move(Tiles)
                    #A tile is added prior to game over as that can cause a game over
                    add_tile(Tiles)
                    if (check_loss(Tiles) == True):
                        state.state_change(1)
                    draw_board(screen, Tiles, font, state)
                elif event.key == pygame.K_RIGHT and state.current == state.running:
                    Move.Move_Right.move(Tiles)
                    add_tile(Tiles)
                    if (check_loss(Tiles) == True):
                        state.state_change(1)
                    draw_board(screen, Tiles, font, state)
                elif event.key == pygame.K_UP and state.current == state.running:
                    Move.Move_Up.move(Tiles)
                    add_tile(Tiles)
                    if (check_loss(Tiles) == True):
                        state.state_change(1)
                    draw_board(screen, Tiles, font, state)
                elif event.key == pygame.K_DOWN and state.current == state.running:
                    Move.Move_Down.move(Tiles)
                    add_tile(Tiles)
                    if (check_loss(Tiles) == True):
                        state.state_change(1)
                    draw_board(screen, Tiles, font, state)
                elif event.key == pygame.K_SPACE:
                    #Space restarts the game during a game over as well as pausing and unpausing, so it's checked if that's the current state
                    if (state.current == state.gameOver):
                        Tiles = initialize_tiles()
                        add_tile(Tiles)
                        add_tile(Tiles)
                    state.state_change(0)
                    draw_board(screen, Tiles, font, state)
                elif event.key == pygame.K_r:
                    Tiles = initialize_tiles()
                    add_tile(Tiles)
                    add_tile(Tiles)
                    draw_board(screen, Tiles, font, state)
                elif event.key == pygame.K_m:
                    main_menu()
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
                #Remove later: only for testing
                elif event.key == pygame.K_n:
                    add_tile(Tiles)
                    draw_board(screen, Tiles, font, state)

# Draw the 2048 board
def draw_board(screen, Tiles, font, state):
    # Draw the background
    screen.fill((250, 248, 239))
    # Draw the grid
    score = 0
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, (Tiles[i][j].color[0],Tiles[i][j].color[1],Tiles[i][j].color[2]), (Tiles[i][j].x_coord * 200, Tiles[i][j].y_coord * 200, 200, 200), 0)
            pygame.draw.rect(screen, (205, 193, 180), (Tiles[i][j].x_coord * 200, Tiles[i][j].y_coord * 200, 200, 200), 5)
            if (Tiles[i][j].value != 0):
                text = font.render(str(Tiles[i][j].value), 1, (0,0,0))
                text_rect = text.get_rect(center=((Tiles[i][j].x_coord * 200)+100, (Tiles[i][j].y_coord * 200)+100))
                screen.blit(text, text_rect)
                if (Tiles[i][j].value > score):
                    score = Tiles[i][j].value
    text = font.render("Score: " + str(score), 1, (0,0,0))
    #The log file is updated if a new highscore is reached
    if (score > Log.read_score()):
        Log.update_score(score)
    text_rect = text.get_rect(center = (400, 850))
    screen.blit(text, text_rect)
    #The highscore is updated and shown during gameplay
    text = font.render("Highscore: " + str(Log.read_score()), 1, (0,0,0))
    text_rect = text.get_rect(center = (400, 950))
    screen.blit(text, text_rect)
    
    #Display pause if the game is paused
    if (state.current == state.paused):
        font = pygame.font.Font(pygame.font.get_default_font(), 50)
        text = font.render("PAUSED", 1, (0,0,0))
        text_rect = text.get_rect(center = (400, 375))
        screen.blit(text, text_rect)
        text = font.render("SPACE to Resume", 1, (0,0,0))
        text_rect = text.get_rect(center = (400, 425))
        screen.blit(text, text_rect)
        font = pygame.font.Font(pygame.font.get_default_font(), 75)
    #Display game over if the game is over
    elif (state.current == state.gameOver):
        font = pygame.font.Font(pygame.font.get_default_font(), 50)
        text = font.render("GAME OVER", 1, (0,0,0))
        text_rect = text.get_rect(center = (400, 375))
        screen.blit(text, text_rect)
        text = font.render("SPACE to Restart", 1, (0,0,0))
        text_rect = text.get_rect(center = (400, 425))
        screen.blit(text, text_rect)
        font = pygame.font.Font(pygame.font.get_default_font(), 75)
    
    pygame.display.flip()

# Updates a 0 value tile to 2 (essentially adding a tile)
def add_tile(Tiles):
    for i in range(4):
        for j in range(4):
            if (Tiles[i][j].value == 0): 
                temp_col = random.randrange(4)
                temp_row = random.randrange(4)
                while Tiles[temp_col][temp_row].value != 0:
                    temp_col = random.randrange(4)
                    temp_row = random.randrange(4)
                Tiles[temp_col][temp_row].update_value(2)
                return
    
#Checks if no more moves can be done (Game Over)
def check_loss(Tiles):
    #Each tile is gone through to check if its neighbor is the same value or if it's 0
    #If this is the case for any tile there's still a move to make
    for i in range(4):
        for j in range(4):
            if (Tiles[i][j].value == 0):
                return False
            #Only the tile to the right and below need to be checked as those above or to the left will have already been checked
            if (i < 3):
                if (Tiles[i+1][j].value  == Tiles[i][j].value):
                    return False
            if (j < 3):
                if (Tiles[i][j+1].value  == Tiles[i][j].value):
                    return False
    return True

#Tiles are initialized in a 2d array according to their position
def initialize_tiles():
    tile_list = [[0 for x in range(4)] for y in range(4)]
    for i in range(4):
        for j in range(4):
            tile_list[i][j] = (Tile.Tile(i, j, 0))
    return tile_list

if __name__ == '__main__':
    main_menu()
    #initialize_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
