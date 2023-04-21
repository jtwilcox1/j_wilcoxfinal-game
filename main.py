# File created by: JT Wilcox


# This file was created by: JT Wilcox
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: my friend Charlie
'''
My goal is:
make the sprite a different image
randomize position of platforms for each game 
reach goal: make platforms move

Goals: Hit all of the orange mobs 
Rules: Must stay withing the boundaries of the screen
Feedback: All mobs will be gone when game is finished
Freedom: You the freedom to move whenever you want and jump on any platforms
'''

# import libs
import pygame as pg
import os
# import settings and sprites
from settings import *
from sprites import *
# from timer import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
# displays the screen with width and height
screen = pg.display.set_mode((WIDTH, HEIGHT))


# game class to pass properties in sprites
class Game:
    # initiate self
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        # sets up the screen the game will be displayed in in pygame
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # caption of window
        pg.display.set_caption("my game")
        # used to track a certain amount of time that has passed
        self.clock = pg.time.Clock()
      # start of game loop
        self.running = True
        # displays self.screen
        print(self.screen)
    def new(self):
        # starting a new game
        self.score = 0
        # imports sprites
        self.all_sprites = pg.sprite.Group()
        # imports platforms
        self.platforms = pg.sprite.Group()
        # import enemies
        self.enemies = pg.sprite.Group()
        # import player
        self.player = Player(self)
        
        # self.health = 8
        # the characteristics of each platform
        # this is the bottom platform
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (SAND), "normal")
        # this is a platform so that the player lands on a platform every game
        self.plat2 = Platform(200, 30, 300, 400, (LGREEN), "normal")
        # I made it so that each platform is randomely placed in a new spot after every game 
        # i did this by returning a random integer for the width and height 
        # it will choose a random spot for each platform
        # the reason there is a -75 next to the height and width is so that it is not inside of the bottom platform or far off the screen
        self.plat3 = Platform(100, 30, randint(0,WIDTH-75), randint(0,HEIGHT-75), (LGREEN), "normal")
        self.plat4 = Platform(150, 30, randint(0,WIDTH)-75, randint(0,HEIGHT-75), (LGREEN), "normal")
        self.plat5 = Platform(175, 30, randint(0,WIDTH-75), randint(0,HEIGHT-75), (LGREEN), "normal")
        self.plat6 = Platform(175, 30, randint(0,WIDTH-75), randint(0,HEIGHT-75), (LGREEN), "normal")
        self.all_sprites.add(self.plat1)
        self.all_sprites.add(self.plat2)
        self.all_sprites.add(self.plat3)
        self.all_sprites.add(self.plat4)
        self.all_sprites.add(self.plat5)
        self.all_sprites.add(self.plat6)
        self.platforms.add(self.plat1)
        self.platforms.add(self.plat2)
        self.platforms.add(self.plat3)
        self.platforms.add(self.plat4)
        self.platforms.add(self.plat5)
        self.platforms.add(self.plat6)
        self.all_sprites.add(self.player)
        # the range in from 0-10
        # says there are 10 mobs
        for i in range(0,10):
            # size and color of mob
            m = Mob(20,20,(0,255,0))
            # adds all sprites to the game
            self.all_sprites.add(m)
            # adds enemies
            self.enemies.add(m)
            # self is a parameter and run is a method
        self.run()
        # instance of a class
    def run(self):
        # boolean
        self.playing = True
        # animations happen while game is running
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    

# defines the method events
    def events(self):
        # internal events and retrieves list of external events
        for event in pg.event.get():
            # if event object is quit, pg.quit is called
            if event.type == pg.QUIT:
                # it is not possible to be playing when game is quit
                if self.playing:
                    self.playing = False
                self.running = False
                # keybinds for how to control sprite
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    # what action to do when keybind is pressed
                    self.player.jump()
    def update(self):
        self.all_sprites.update()
        # this makes it so that the player does not fall through the platforms
        if self.player.vel.y > 0:
            # if the false is switched to true, then the sprite will fall through the platform
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)  
            # makes it so that when the player collide with an enemy the enemy dissapears
            enemieshits = pg.sprite.spritecollide(self.player, self.enemies, True)
           
            
        


        
# if commented sprite will fall through platform
            if hits:
                if hits[0].variant == "dissapearing":
                    hits[0].kill()
                elif hits[0].variant == "dissapearing ":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    PLAYER_FRICTION = 0
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0

    def draw(self):
        # color of background
        self.screen.fill(BLUE)
        # makes it so sprites appear 
        self.all_sprites.draw(self.screen)
        # full display surface to screen
        pg.display.flip() 
    
    # get_mouse_now is a tuple
    def get_mouse_now(self):
        # x and y is the position where the cursor is
        x,y = pg.mouse.get_pos()
        # equal to 1 if x and y are eqaul to each other
        return (x,y)
    

# instantiate the game class
g = Game()

# kick off the game loop
while g.running:
    g.new()
    

pg.quit()

    

# self.draw_TIMER(self.screen)
