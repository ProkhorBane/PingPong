from pygame import *


main_win = display.set_mode((700,500))
main_win.fill((230,57,189))

class GameSprite(sprite.Sprite):
    def __init__(self,p_image,p_x,p_y,p_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(p_image),(size_x,size_y))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
    def reset(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        pressed_keys = key.get_pressed()
        if pressed_keys[K_UP] and self.rect.y > 5:
            self.rect.y += self.speed
        if pressed_keys[K_DOWN] and self.rect.y < 630:
            self.rect.y -= self.speed
    def update_2(self):
        pressed_keys = key.get_pressed()
        if pressed_keys[K_w] and self.rect.y > 5:
            self.rect.y += self.speed
        if pressed_keys[K_s] and self.rect.y < 630:
            self.rect.y -= self.speed

class Ball(GameSprite):
    def update(self):
        if 

player_1 = Player('rocket.png',100,250,10,70,70)
player_2 = Player('rocket.png',600,250,10,70,70)

game = True
clock = Clock()
fps = 60

while game:
    player_1.reset()
    player_1.update_1()
    player_2.reset()
    player_2.update_2()



    clock.tick(fps)
    display.update()