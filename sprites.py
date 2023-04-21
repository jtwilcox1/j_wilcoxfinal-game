# File created by JT Wilcox

# import libs
import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint
import os
# allows to import images onto sprites
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")

# define direction and amount
vec = pg.math.Vector2

# player class

class Player(Sprite):
    # self represents the object of the class
    def __init__(self, game):
        # runs sprite classes
        Sprite.__init__(self)
        # properties of the player sprite
        self.game = game
        # width
        self.image = pg.Surface((50,50))
        # loads the image of the shark onto the main sprite
        self.image = pg.image.load(os.path.join(img_folder, 'shark.png')).convert()
        # returns rectangle
        self.rect = self.image.get_rect()
        # starting point of shark
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        # velocity
        self.vel = vec(0,0)
        # accelleration
        self.acc = vec(0,0)
        # cofric is a float
        self.cofric = 0.1
        # boolean
        self.canjump = False
    def input(self):
        keystate = pg.key.get_pressed()
        # if A is pressed sprite will move left
        
        if keystate[pg.K_a]:
            # the negative sign shows that this will move left
            self.acc.x = -PLAYER_ACC
        # if D is pressed sprite will move right
        if keystate[pg.K_d]:
            # no negative so will move right
            self.acc.x = PLAYER_ACC
        # if keystate[pg.K_p]:
        #     if PAUSED == False:
        #         PAUSED = True
        #         print(PAUSED)
        #     else:
        #         PAUSED = False
        #         print(PAUSED)
    # defines characteristics of when to jump and how high to jump
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        # if hits:
        self.vel.y = -PLAYER_JUMP
    # lets the player know when sprite has left the boundary and where it is
    def inbounds(self):
        if self.rect.x > WIDTH - 50:
            self.pos.x = WIDTH - 25
            self.vel.x = 0
            print("i am off the right side of the screen...")
        if self.rect.x < 0:
            self.pos.x = 25
            self.vel.x = 0
            print("i am off the left side of the screen...")
        if self.rect.y > HEIGHT:
            print("i am off the bottom of the screen")
        if self.rect.y < 0:
            print("i am off the top of the screen...")
            # what text will be displayed and how score will change when there is a collison with player and mob
    def mob_collide(self):
            hits = pg.sprite.spritecollide(self, self.game.enemies, True)
            if hits:
                print("you collided with an enemy...")
                # score goes up 1 when collided with enemy
                self.game.score += 1
                print(SCORE)
    # puts gravity into game so player is not constantly falling
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos


# mob class
class Mob(Sprite):
    # charactersitics of mob
    def __init__(self,width,height, color):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        # position of enemies
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/4, HEIGHT/4)
        # starting point and direction to move when game begins
        self.vel = vec(randint(1,5),randint(1,5))
        self.acc = vec(1,1)
        self.cofric = 0.01

    # ...
    # make it so mobs are actually staying within the screen and are always visible
    def inbounds(self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1
           
        if self.rect.x < 0:
            self.vel.x *= -1
            
        if self.rect.y < 0:
            self.vel.y *= -1
          
        if self.rect.y > HEIGHT:
            self.vel.y *= -1
           
    def update(self):
        self.inbounds()
        # self.pos.x += self.vel.x
        # self.pos.y += self.vel.y
        self.pos += self.vel
        self.rect.center = self.pos

#platform class

class Platform(Sprite):
    # operarting system for platforms
    def __init__(self, width, height, x, y, color, variant):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant

