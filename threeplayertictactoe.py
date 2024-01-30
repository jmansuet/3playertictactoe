# Import modules
import pygame
from pygame.locals import *
import math as math

pygame.init()

screen_width = 700
screen_height = 700

grid_size = 4 #!! THIS FOR GRID SIZE!!

line_width = 6
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic Tac Toe')

#define colours
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pink = (255, 182, 193)

#define font
font = pygame.font.SysFont(None, 40)

#define variables
clicked = False
player = 1
pos = (0,0)
markers = []
game_over = False
winner = 0

#setup a rectangle for "Play Again" Option
again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)

for x in range(4): # !! THIS FOR GRID!! also have to change second game grid
    row = [0] * 4
    markers.append(row)


# Update the grid drawing loop
def draw_board():
    bg = (253, 237, 235)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1, grid_size):
        pygame.draw.line(screen, grid, (0, screen_height // grid_size * x), (screen_width, screen_height // grid_size * x), line_width)
        pygame.draw.line(screen, grid, (screen_width // grid_size * x, 0), (screen_width // grid_size * x, screen_height), line_width)

# Update the marker drawing loop
def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == -1:
                pygame.draw.line(screen, red, (x_pos * screen_width // grid_size + 15, y_pos * screen_height // grid_size + 15),
                                 (x_pos * screen_width // grid_size + screen_width // grid_size - 15, y_pos * screen_height // grid_size + screen_height // grid_size - 15), line_width)
                pygame.draw.line(screen, red, (x_pos * screen_width // grid_size + screen_width // grid_size - 15, y_pos * screen_height // grid_size + 15),
                                 (x_pos * screen_width // grid_size + 15, y_pos * screen_height // grid_size + screen_height // grid_size - 15), line_width)
            elif y == 1:
                pygame.draw.circle(screen, green, (x_pos * screen_width // grid_size + screen_width // (2 * grid_size),
                                                  y_pos * screen_height // grid_size + screen_height // (2 * grid_size)), screen_width // (2 * grid_size) - 15, line_width)
            elif y == 10:
                star_x = x_pos * screen_width // grid_size + screen_width // (2 * grid_size)
                star_y = y_pos * screen_height // grid_size + screen_height // (2 * grid_size)
                star_size = screen_width // (3 * grid_size)  
                outer_points = []
                inner_points = []

                for i in range(5):
                    angle_outer = i * (2 * math.pi / 5)
                    angle_inner = (i + 0.5) * (2 * math.pi / 5)

                    outer_x = star_x + 0.9 * star_size * math.cos(angle_outer)
                    outer_y = star_y + 0.9 * star_size * math.sin(angle_outer)

                    inner_x = star_x + 0.4 * star_size * math.cos(angle_inner)
                    inner_y = star_y + 0.4 * star_size * math.sin(angle_inner)

                    outer_points.append((outer_x, outer_y))
                    inner_points.append((inner_x, inner_y))

                pygame.draw.polygon(screen, pink, outer_points, line_width)
                pygame.draw.polygon(screen, pink, inner_points, line_width)

            y_pos += 1
        x_pos += 1


def check_game_over():
    global game_over
    global winner
    
    if 3 == 3:
        game_over = False
    y_pos = 0
    x_pos = 0
    for x in markers:
        # check columns
        if markers[y_pos][0] + markers[y_pos][1] + markers[y_pos][2] == 3 or markers[y_pos][1] + markers[y_pos][2] + markers[y_pos][3] == 3:
            winner = 1
            game_over = True
        if markers[y_pos][0] + markers[y_pos][1] + markers[y_pos][2] == -3 or markers[y_pos][1] + markers[y_pos][2] + markers[y_pos][3] == -3:
            winner = 2
            game_over = True
        if markers[y_pos][0] + markers[y_pos][1] + markers[y_pos][2] == 30 or markers[y_pos][1] + markers[y_pos][2] + markers[y_pos][3] == 30:
            winner = 3
            game_over = True
        y_pos += 1
        # check rows
        if markers[0][x_pos] + markers[1][x_pos] + markers[2][x_pos] == 3 or markers[1][x_pos] + markers[2][x_pos] + markers[3][x_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][x_pos] + markers[1][x_pos] + markers[2][x_pos] == -3 or markers[1][x_pos] + markers[2][x_pos] + markers[3][x_pos] == -3:
            winner = 2
            game_over = True
        if markers[0][x_pos] + markers[1][x_pos] + markers[2][x_pos] == 30 or markers[1][x_pos] + markers[2][x_pos] + markers[3][x_pos] == 30:
            winner = 3
            game_over = True
        x_pos += 1

    # check cross
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3 or markers[1][0] + markers[2][1] + markers[3][2] == 3 or markers[0][1] + markers[1][2] + markers[2][3] == 3 or markers[1][1] + markers[2][2] + markers[3][3] == 3 or markers[0][3] + markers[1][2] + markers[2][2] == 3 or markers[1][2] + markers[2][1] + markers[3][0] == 3 or markers[1][3] + markers[2][2] + markers[3][1] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3 or markers[1][0] + markers[2][1] + markers[3][2] == -3 or markers[0][1] + markers[1][2] + markers[2][3] == -3 or markers[1][1] + markers[2][2] + markers[3][3] == -3 or markers[0][3] + markers[1][2] + markers[2][2] == -3 or markers[1][2] + markers[2][1] + markers[3][0] == -3 or markers[1][3] + markers[2][2] + markers[3][1] == -3:
        winner = 2
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == 30 or markers[2][0] + markers[1][1] + markers[0][2] == 30 or markers[1][0] + markers[2][1] + markers[3][2] == 30 or markers[0][1] + markers[1][2] + markers[2][3] == 30 or markers[1][1] + markers[2][2] + markers[3][3] == 30 or markers[0][3] + markers[1][2] + markers[2][2] == 30 or markers[1][2] + markers[2][1] + markers[3][0] == 30 or markers[1][3] + markers[2][2] + markers[3][1] == 30:
        winner = 3
        game_over = True

    # check for tie
    if game_over == False:
        tie = True
        for row in markers:
            for i in row:
                if i == 0:
                    tie = False
       #  if it is a tie, then call game over and set winner to 0 (no one)
        if tie == True:
            game_over = True
            winner = 0


def draw_game_over(winner):

    if winner != 0:
        end_text = "Player " + str(winner) + " wins!"
    elif winner == 0:
        end_text = "You have tied!"

    end_img = font.render(end_text, True, blue)
    pygame.draw.rect(screen, green, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
    screen.blit(end_img, (screen_width // 2 - 100, screen_height // 2 - 50))

    again_text = 'Play Again?'
    again_img = font.render(again_text, True, blue)
    pygame.draw.rect(screen, green, again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10))


# main loop
run = True
while run:
    # draw board and markers first
    draw_board()
    draw_markers()

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # handle game exit
            run = False  # run new game
        if game_over == False:
            # check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0] // (screen_width // grid_size)
                cell_y = pos[1] // (screen_height // grid_size)
                if 0 <= cell_x < grid_size and 0 <= cell_y < grid_size and markers[cell_x][cell_y] == 0:
                    markers[cell_x][cell_y] = player
                    if player == 1:
                        player = -1
                    elif player == -1:
                        player = 10
                    elif player == 10:
                        player = 1
                        
                    check_game_over()

    # check if game has been won
    if game_over == True:
        draw_game_over(winner)
        # check for mouse click to see if we clicked on Play Again
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                # reset variables
                game_over = False
                player = 1
                pos = (0, 0)
                markers = []
                winner = 0
                # create empty 3 x 3 list to represent the grid !!THIS IS SECOND GRID MUST BE CHANGED TOO!!
                for x in range(5):
                    row = [0] * 5
                    markers.append(row)

    # update display
    pygame.display.update()

pygame.quit()
