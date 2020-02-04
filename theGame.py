import pygame
import playerClass
import pathFunction
import monsterClass
import random
import music
import eventFunctions

"""
variables:
clock = to get frames by time past
main = bool to create game loop
menu = bool to create menu loop
fps = to get frames / second with the clock
tilt = variable to move the text in menus
time = time survived
health = int -show health in %
points = int - what is a game like this without a point system
score_table = to create a list of scores
"""
pygame.init()
        #Y-20 y 530
        #x -32 x 740
menu = True
main = False
game_on = False
lost = False
game_window_sizeX = 795
game_window_sizeY = 600
fps = 60
clock = pygame.time.Clock()
tilt = 0
moveY = 220
moveX = 50
time = 0
health = 100
points = 0

"""
Create the pygame display
"""
game_world = pygame.display.set_mode([game_window_sizeX, game_window_sizeY])
game_background = pygame.image.load('./gimages/bakgrundSpel.png')
game_box = game_world.get_rect()

""" 
Game window objects the maybe not so obvious variables explained

moveY = used to check positions of frog and player
moveX = -"-
score_table = object with scores
frog = object of a frog
frogs = put them into pygame sprites group
player = creates a player from the PlayerClass --> class Player
"""

frog = monsterClass.Frog(moveX+700,random.randint(40,500))
frogs = pygame.sprite.Group()
frogs.add(frog)

frog_image = pathFunction.get_image_path('./mimages/')
position = (moveX,moveY)
player_images = pathFunction.get_image_path('./pimages/')
player = playerClass.Player(position=position, images=player_images)

player_animate = pygame.sprite.Group(player)
player_animate.add(player)

def ingame_events(time, frogs, lost, game_on, menu):
    """
    This function take care of the ingame controllers. ( events)
    """
    global main
    global health
    global pause_
    for event in pygame.event.get():
        """
        This will make you able to move the flying pig
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.velocity.x = 12
            elif event.key == pygame.K_LEFT or event.key == ord('a'):
                player.velocity.x = -12
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                player.velocity.y = 12
            elif event.key == pygame.K_UP or event.key == ord('w'):
                player.velocity.y = -20
            elif event.key == pygame.K_ESCAPE:
                menu = True
                game_on = False
                time = 0
                health = 100
                for enemy in frogs:
                    frogs.remove(enemy)
                music.menu_music()
                lost = False
                main = False
                menu = True
               # return main
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == ord('d') or event.key == ord('a'):
                player.velocity.x = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == ord('w') or event.key == ord('s'):
                player.velocity.y = 0

def menu_events(game_on, menu):
    """
    This function take care of the menu controllers. ( events)
    """
    global pause_
    global main
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == ord('1'):
                for enemy in frogs:
                    frogs.remove(enemy)
                main = True
                game_on = True
                music.game_music()
                get_game_running(time , points)

            elif event.key == ord('2'):
                pause_ = True
                menu = False
                get_info(0,0,main,game_on)
            elif event.key == ord('3'):
                menu = False
                pygame.display.quit()

def check_hitbox():
    global health
    """
    For each monster frog in frog , this loop will "print"
    out every frog in the group. And within the loop it will
    check if player hits by using the monsterClass function bool
    """
    for frog in frogs:
        frog.show_frog(game_world)
        frog.move_you_fool(random.randint(4,20))
        if frog.bool(moveX,moveY,frog.x, frog.y) == True:
            game_world.fill((random.randint(1,254),random.randint(1,254),random.randint(1,254)))
            health -= 2
            pygame.mixer.music.load('./gameMusic/mySuperGameSong.wav')
            pygame.mixer.music.play()


def get_frogs_flying(time):                                                                                                                                     
    """
    This function will check if the time is between certain mseconds
    and if the condition is right enemies will arrive.
    Because of the time i input here, it certainly will come out
    random amount of enemies every time.. so be carefull out there 
    """
    if time >= 2 and time <=2.1:
        frogs.add(monsterClass.Frog(moveX+600,random.randint(10,300)))
    elif time >= 2.4 and time <=2.5:
        frogs.add(monsterClass.Frog(moveX+600,random.randint(350,550)))
    elif time >= 3.1 and time <= 3.15:
        frogs.add(monsterClass.Frog(moveX+650,random.randint(320,420)))
    elif time >= 9 and time <= 9.05:
        frogs.add(monsterClass.Frog(moveX+600,random.randint(0,600)))
    elif time >=11 and time <= 11.05:
        frogs.add(monsterClass.Frog(moveX+600,random.randint(0,550)))
    elif time >=13 and time <= 13.05:
        frogs.add(monsterClass.Frog(moveX+600,random.randint(0,550)))
    elif time >=15 and time <= 15.1:
        frogs.add(monsterClass.Frog(moveX+600,random.randint(100,500)))

def text_format(message, textFont, textSize, textColor):
    """
    This function is for easy putting texts and give
    them fonts , size and color ( found this checking out others code, i liked the idea)
    """
    newFont=pygame.font.SysFont(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText

def get_game_running(time , points):
    """
    This function will take care of the game while it is running.
    Parameters:
        main = bool
        time = float
        health = int
        points = int
    """
 
    global moveY
    global moveX
    global lost
    global game_on
    global health
    global menu
    global main


    # if main == True and menu == False:
    #     pygame.mixer.music.load('./gameMusic/mySuperGameSong.wav')
    #     pygame.mixer.music.play()
    while main:
        """
        This is the game loop 
        Below is where the action happens
        I have some texts left commented out , i use them to see locations
        and see if they are correct.
        """
        # Amount of seconds between each loop.
        time_fps = clock.tick(fps) / 1000
        points += int(time)

        player_points = text_format(f'Points: {points}', "segoescript", 30, (2,214,113,0))
        player_life = text_format(f'LIFE: {health} %', "segoescript", 30, (255,77,244,0))
        # This gives the game the superb background
        game_world.blit(game_background, game_box)

        # moveX and moveY below become accurate positioning the player
        moveX += player.velocity.x
        moveY += player.velocity.y
        
        get_frogs_flying(time)

        time += time_fps
        clock.tick(fps)

        ingame_events(time, frogs, lost, game_on, menu )
        """
        This condition is the thing pulling the litle piggy down all the time
        """
        if moveY < 533:
            player.velocity.y += 1
        """
        The conditions below will keep player inside the game window
        """
        if moveX > 740:
            player.velocity.x -=10
        elif moveX < -32:
            player.velocity.x +=10
        elif moveY < -5:
            player.velocity.y +=10
        elif moveY > 530:
            player.velocity.y -=10

        game_world.blit(player_points,(380,-7))
        game_world.blit(player_life,(180,-7))

        player.update_animation(time)
        player_animate.draw(game_world)

        #
        # RedrawMonsters()  
        #                    It might be a good idea to break down the code into 
        #                    self explaining parts by dividing into methods and/or classes
        #

        check_hitbox()
        
        if health <= 0:
            """
            If your health is 0 or below , main game ends and dead is true.
            dead goes into another function with a "game over" loop
            """
            main = False
            dead = True
            get_game_over(dead,tilt, time, points)
            
        pygame.display.update()

def get_game_over( lost, tilt, time, points):
    """
    This function will check how much time the player survived
    and depending on how long the player will get a certain 
    amount extra on points.
    game_done = takes earned * points
    Parameters:
        lost = bool
        tilt = int
        time = float
        points = int
        health = int
    """
    global health
    global menu
    global moveY
    global moveX
    global game_on
    if time > 6 and time <= 11:
        earned = 2
    elif time > 11 and time <= 15:
        earned = 3
    elif time > 14:
        earned = 5
    else:
        earned = 5
    game_done = earned*points

    while lost:
        game_on = False
        clock.tick(5)
        game_world.fill((0,0,0))

        game_title = text_format('GAME OVER', "segoescript", 50, (255,5,5,0))
        game_title1 = text_format(f'You lost the game and earned {game_done} points', "mongolianbaiti", 30, (2,214,113,0))
        game_title2 = text_format('Have a nice day...', "mongolianbaiti", 30, (2,214,113,0))
        game_title3 = text_format('PRESS Q TO QUIT', "mongolianbaiti", 30, (255,5,5,0))
        game_title4 = text_format('PRESS 1 FOR MENU', "mongolianbaiti", 30, (255,5,5,0))

        #game_world.blit(menu_background, game_box)
        game_world.blit(game_title,(150+random.randint(1,110) , 30+random.randint(1,150)))
        game_world.blit(game_title1,(150 , 250 ))
        game_world.blit(game_title2,(150 , 300 ))
        game_world.blit(game_title3,(250 , 450 ))
        game_world.blit(game_title4,(250 , 350 ))


        if tilt == 70:
            tilt = 0
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.display.quit()
                    lost = False
                if event.key == ord('1'):
                    points = 0
                    time = 0
                    health = 100
                    for enemy in frogs:
                        frogs.remove(enemy)
                    music.menu_music()
                    lost = False
                    menu = True

def get_info(time, points, main, game_on):   
    """
    This function take care of game when in Pause mode, 
    AND if you click "How To play" in main menu.
    Pause will only work to unpause if the game has been started.
    Parameters:
        info_ = bool
        time = float
        health = int
        points = int
    """
    info_ = True
    global menu

    music.menu_music()
    while info_:
        game_world.fill((0,0,0))
        game_title = text_format('=)', "segoescript", 55, (2,244,50,0))
        game_title1 = text_format('How To Play:', "mongolianbaiti", 40, (255,255,255,0))
        game_title2 = text_format('W=Up, A=Left, S=Down, D=Right', "mongolianbaiti", 40, (255,255,255,0))
        game_title3 = text_format('You Can Also Use The Arrow', "mongolianbaiti", 40, (255,255,255,0))
        game_title4 = text_format('Keys= Up, Left, Down, Right', "mongolianbaiti", 40, (255,255,255,0))
        game_title5 = text_format('Press 1 For Menu', "mongolianbaiti", 40, (255,5,5,0))
        game_title6 = text_format('______________________________', "mongolianbaiti", 40, (255,5,5,0))
        game_title7 = text_format('-To Quit Ingame Press \"ESC\"-', "mongolianbaiti", 45, (255,5,5,0))

        game_world.blit(game_title,(120 , 30+tilt ))
        game_world.blit(game_title1,(150 , 300 ))
        game_world.blit(game_title2,(150 , 350 ))
        game_world.blit(game_title3,(150 , 450 ))
        game_world.blit(game_title4,(150 , 500 ))
        game_world.blit(game_title5,(150 , 150 ))
        game_world.blit(game_title6,(150 , 200 ))
        game_world.blit(game_title7,(150 , 400 ))


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ord('1'):
                    info_ = False
                    game_on = False
                    menu = True
                    music.menu_music()
            
        pygame.display.flip()
        clock.tick(20)    

if menu == True:   
    music.menu_music()

while menu:
    """
    Menu Loop
    Here i put in just a simple screen 
    and give the player some choices
    """

    animate = 1
    tilt +=1
    game_world.fill((0,0,0))
    player_animate.update(animate)
    player_animate.draw(game_world)

    game_title = text_format('Flying Pig', "segoescript", 75, (2,244,50,0))
    game_title1 = text_format('Press 1 To START', "mongolianbaiti", 50, (255,255,255,0))
    game_title3 = text_format('Press 3 To QUIT', "mongolianbaiti", 50, (255,5,5,0))
    game_title4 = text_format("A Flying Pig Is Captured By Cloned Mutaded Frogs!", "segoescript", 28, (2,244,50,0))
    game_title5 = text_format("Survive Until You Get Saved!!", "segoescript", 35, (2,244,50,0))
    game_title6 = text_format('Press 2 To See Controls', "mongolianbaiti", 50, (255,255,255,0))

    game_world.blit(game_title,(120 , 30+tilt ))
    game_world.blit(game_title1,(150 , 250 ))
    game_world.blit(game_title3,(150 , 400 ))
    game_world.blit(game_title4,(20 , 500 ))
    game_world.blit(game_title5,(95 , 550 ))
    game_world.blit(game_title6,(95 , 350 ))



    if tilt == 70:
        tilt = 0
    
    pygame.display.flip()
    clock.tick(20)
    menu_events(game_on, menu)