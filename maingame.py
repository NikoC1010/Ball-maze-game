import os
import sys
import pygame
import time
import maps
import maze
import ball
from GLOBAL import *
os.environ['SDL_VIDEO_CENTERED'] = '1'
path_ = os.getcwd()
path.path=path_.replace('\\','/')


pygame.init()

note_image = pygame.image.load(r''+path.path+'/picture/note.jpg')
win_image = pygame.image.load(r''+path.path+'/picture/win.png')
lose_image = pygame.image.load(r''+path.path+'/picture/lose.png')
clock=pygame.time.Clock()
window = pygame.display.set_mode((W_WIDTH,W_HEIGHT))
pygame.display.set_caption("Group project--Maze")

global maze_list
map_group = pygame.sprite.Group()
maps_map = maze.Maze(20,20)
maze_list=maps_map.create_maze()
ball1=ball.Ball()
countdown_time = 60
start_time = time.time()

def impactor():
    for i in range(maps_map.len):
        for j in range(maps_map.wid):
            if maze_list[i][j]==0:
                map1 = maps.Maps(j*50, i*50, 50, 50)
                map_group.add(map1)

impactor()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit() 
    window.fill((255, 255, 255))
    window.blit(pygame.transform.scale(note_image, (350,500)),(960,400))
    ball1.move(map_group)
    window.blit(pygame.transform.scale(ball1.image,(25,25)),ball1.rect)
    map_group.draw(window)
    pygame.display.flip()

    font1 = pygame.font.SysFont(None, 33)
    elapsed_time = int(time.time() - start_time)
    font3 = pygame.font.SysFont(None, 33)
    lose_text = font3.render("Game over Sorry you lost.", True, (139,69,19))
    remaining_time = countdown_time - elapsed_time

    if remaining_time <= 0:
        window.blit(lose_text, (50,25))
        window.blit(pygame.transform.scale(lose_image,(200,200)),(1020,200))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()
        
    time_text = font1.render("Remaining Time: "+str(remaining_time), True, (220,20,60))
    window.blit(time_text, (1020,50))
    
    if ball1.rect.bottom >= 19*50 or ball1.rect.right >= 19*50:
        font2 = pygame.font.SysFont(None, 33)
        end_text = font2.render("Congratulations!You win the game!", True, (139,69,19))
        window.blit(end_text, (50,25))
        window.blit(pygame.transform.scale(win_image,(200,200)),(1020,200))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

        
    pygame.display.update()
    clock.tick(60)
