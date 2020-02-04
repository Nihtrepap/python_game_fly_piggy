import pygame

def ingame_events(menu, game_on, time, health, frogs,lost, main, pause):
        
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
                        menu = True
                        main = False
                    elif event.key == ord('p'):
                        main = False
                        pause= True
                        get_info_paus(pause, time , health, points)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == ord('d') or event.key == ord('a'):
                        player.velocity.x = 0
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == ord('w') or event.key == ord('s'):
                        player.velocity.y = 0