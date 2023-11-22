from pygame import *
init()
screen = display.set_mode((1280, 720)) 
class Player:
        player_x = 610
        splayer_y = 639
        player_speed = 10
        player = image.load('images/spaceArt/png/player.png').convert_alpha() 
        playerLeft = image.load('images/spaceArt/png/playerLeft.png').convert_alpha() 
        playerRight = image.load('images/spaceArt/png/playerRight.png').convert_alpha() 

player = Player()
player.player_x = 700
print(player.player_x)

player_2 = Player()
print(player_2.player_x)