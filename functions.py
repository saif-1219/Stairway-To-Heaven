import random
import pygame,sys

def map_generator():
    row_list = []
       
    a = [[[1,1,1],[1,1,1],[1,1,1]],[[1,1,1],[1,1,1],[1,1]],[[1,1,1],[1,1],[1,1]],[[1,1],[1,1],[1,1]]] 
    
    while len(row_list) < 150:
        row_list.append(random.choice(a))
    return (row_list)

def coordinate_generator(map_gen):
    coordinates = {}
    y_coordinate = 500
    count = 0
    for i in range(len(map_gen)):
        for j in map_gen[i]:
            x_coordinate = random.randint(0,1000)
            for k in range(len(j)):
                coordinate_xy = []
                coordinate_xy.append(x_coordinate)
                coordinate_xy.append(y_coordinate)
                coordinates[count] = (coordinate_xy)
                count+=1
                x_coordinate +=50
        y_coordinate-=150
    return coordinates


def vertical_collision_top(character_rect_x,character_rect_y,x_coordinate,y_coordinate):
    if character_rect_x+10 >= x_coordinate:
        if character_rect_x <= x_coordinate+50:
            if character_rect_y+30 in range(y_coordinate,y_coordinate+25):
                return True
    return False

def vertical_collision_bottom(character_rect_x,character_rect_y,x_coordinate,y_coordinate):
    if character_rect_x+10 >= x_coordinate:
        if character_rect_x <= x_coordinate+50:
            if character_rect_y in range(y_coordinate+26,y_coordinate+50):
                return True
    return False

def horizontal_collision_left(character_rect_x,character_rect_y,x_coordinate,y_coordinate):
    if character_rect_y+30 >= y_coordinate+5:
        if character_rect_y <= y_coordinate+45:
            if character_rect_x+5 in range(x_coordinate-1,x_coordinate+1):
                return True
    return False

def horizontal_collision_right(character_rect_x,character_rect_y,x_coordinate,y_coordinate):
    if character_rect_y+30 >= y_coordinate+5:
        if character_rect_y <= y_coordinate+45:
            if character_rect_x+5 in range(x_coordinate+49,x_coordinate+51):
                return True
    return False

def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                        
def text_display(text, color, x, y, window):
    font = pygame.font.SysFont(None, 55)
    screen_text = font.render(text, True, color)
    window.blit(screen_text,[x, y])


