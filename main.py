import pygame, sys, random, settings

'''Класс игры'''
class Game:  
    pygame.init()
    def __init__(self):
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.bg = pygame.image.load('images/star_bg/bg.png').convert_alpha() 
        self.bg_y = 0
        self.clock = pygame.time.Clock()
        self.name = pygame.display.set_caption('Star Guardian')
        self.gameIcon = pygame.display.set_icon(pygame.image.load('images/spaceArt/png/player.png').convert_alpha())

    def run(self):       
        player = Player()
        framesForShake = 0
        self.shakeValue = 1

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.bg, (0, self.bg_y))
            self.screen.blit(self.bg, (0, self.bg_y - 720))
            self.bg_y += 1
            if self.bg_y == 720: 
                self.bg_y = 0

            player.move()

            framesForShake += 1
            if framesForShake == 15:
                framesForShake = 0
                self.shakeValue *= -1

            pygame.display.update()
            self.clock.tick(settings.FPS)

'''Класс игрока'''
class Player:
    def __init__(self):
        self.middlePos = pygame.image.load('images/spaceArt/png/player.png').convert_alpha()
        self.leftPos = pygame.image.load('images/spaceArt/png/playerLeft.png').convert_alpha()
        self.rightPos = pygame.image.load('images/spaceArt/png/playerRight.png').convert_alpha()
        self.x = 610
        self.y = 639 
        self.speed = 10 
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 10 and not keys[pygame.K_RIGHT]: 
            self.x -= self.speed
            game.screen.blit(self.leftPos, (self.x, self.y + game.shakeValue))
        elif keys[pygame.K_RIGHT] and self.x < 1170 and not keys[pygame.K_LEFT]: 
            self.x += self.speed
            game.screen.blit(self.rightPos, (self.x, self.y + game.shakeValue))
        else: game.screen.blit(self.middlePos, (self.x, self.y + game.shakeValue))
        if keys[pygame.K_UP] and self.y > 10 and not keys[pygame.K_DOWN]:
            self.y -= self.speed
        elif keys[pygame.K_DOWN] and self.y < 635 and not keys[pygame.K_UP]:
            self.y += self.speed
        

if __name__ == '__main__':
    game = Game()
    game.run()     


    