import pygame, sys, time, random
from functions import *

pygame.init()

def main():

    screen = pygame.display.set_mode((1150,700))
    clock = pygame.time.Clock()
    
    #coordinates of each box placement
    coordinates = coordinate_generator(map_generator())
    print(coordinates)

    #Animations
    box  = pygame.image.load("box.png")
    character = pygame.image.load("character.png")
    character_rect = character.get_rect(midbottom = (coordinates[1][0],coordinates[1][1]))
    jump_char = pygame.image.load("jump.png")
    jump_char_rect = character_rect
    background = pygame.image.load("background.png")
    background_rect = background.get_rect(bottomleft = (0,700))
    menu_img = pygame.image.load("MENU.png")
    logo = pygame.image.load("LOGO.png")
    logo_rect = logo.get_rect(topleft = (350,42))
    press = pygame.image.load("PRESSKEY.png")
    press_rect = press.get_rect(topleft = (475,420))
    game_over = pygame.image.load("gameover.png")
    scoreboard = pygame.image.load("scoreboard.png")
    scoreboard_rect = scoreboard.get_rect(midtop = (575,0))
    heaven = pygame.image.load("heaven.png")

    #Game variables
    velocity = 5
    gravity = -25
    logo_key = 2
    score = 0
    scorecounter = 1
    
    #Bools
    jump = False
    menu = True
    gameover = False
    win = False

    #gameloop
    while True:
        clock.tick(60)
        screen.fill((0,0,0))
        screen.blit(background,background_rect)
        quit()
        
        with open ("hs","r") as highscore:
                hs = highscore.read()

        keys = pygame.key.get_pressed()
        velocity = 5
        if menu:
            screen.blit(menu_img,(0,0))
            screen.blit(logo,logo_rect)
            logo_rect.y += logo_key
            if logo_rect.y >= 100:
                logo_key = -2
            if logo_rect.y <= 40:
                logo_key = 2
            screen.blit(press,press_rect)
            text_display("Highscore: "+str(hs),(0,0,0),500,465,screen)
            
            if keys[pygame.K_SPACE]:
                menu = False
                gameover = False

        
        elif gameover:
            screen.blit(game_over,(0,0))
            text_display("Score: "+str(score//10)+"  |  "+"Highscore: "+str(hs),(0,0,0),320,275,screen)
            text_display("Press Enter Key to Continue",(0,0,0),310 ,330,screen)
            if keys[pygame.K_RETURN]:
                main()

        elif win:
            screen.blit(heaven,(0,0))
            text_display("Congratulations on reaching Heaven",(0,0,0), 10,10,screen)
            text_display("Press Enter to Restart The Game",(0,0,0),10,50,screen)
            if keys[pygame.K_RETURN]:
                main()

        else:

            for coordinate in (coordinates):
                coordinates[coordinate][1] += 1
                box_rect = box.get_rect(topleft = (coordinates[coordinate][0],coordinates[coordinate][1]))
                screen.blit(box,box_rect)

                if coordinates[len(coordinates)-1][1] >= 700:
                    win = True

                #vertical collision
                if vertical_collision_top(character_rect.x,character_rect.y,coordinates[coordinate][0],coordinates[coordinate][1]):
                    velocity = 2
                    if keys[pygame.K_SPACE]:
                        gravity = -25
                        jump = True  
                    else:
                        character_rect.y -= velocity
                        jump = False
                        gravity = -25
                            
                if vertical_collision_bottom(character_rect.x,character_rect.y,coordinates[coordinate][0],coordinates[coordinate][1]):
                    character_rect.y += velocity
                    jump = False
                    gravity = -25           

                #Horizontal collision
                if horizontal_collision_left(character_rect.x,character_rect.y,coordinates[coordinate][0],coordinates[coordinate][1]):
                    character_rect.x -= velocity
            
                if horizontal_collision_right(character_rect.x,character_rect.y,coordinates[coordinate][0],coordinates[coordinate][1]):
                    character_rect.x += velocity                         

            if not jump:
                screen.blit(character,character_rect)

            if keys[pygame.K_RIGHT]:
                character_rect.x += 5
            if keys[pygame.K_LEFT]:
                character_rect.x -= 5

            if jump:
                if vertical_collision_bottom(character_rect.x,character_rect.y + gravity ,coordinates[coordinate][0],coordinates[coordinate][1]) or vertical_collision_top(character_rect.x,character_rect.y + gravity ,coordinates[coordinate][0],coordinates[coordinate][1]):
                    jump = False
                screen.blit(jump_char,jump_char_rect)
                jump_char_rect.y += gravity
                gravity += 1
            if character_rect.y >= 725:
                gameover = True
                if score//10 > int(hs):
                    with open ("hs","w") as f:
                        f.write(str(score//10))

            if scorecounter % 5 == 0:
                score += 1
            scorecounter += 1
            
            character_rect.y += velocity
            background_rect.y +=1

            screen.blit(scoreboard,scoreboard_rect)
            text_display("score = "+str(score//10), (230,230,230), 497, 0, screen)
        
        if keys[pygame.K_p]:
            with open ("hs","w") as f:
                f.write("0")
    
        pygame.display.flip()

if __name__ == "__main__":
    main()

