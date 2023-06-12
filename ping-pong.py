from pygame import *


main_win = display.set_mode((700,500))
display.set_caption('Ping-Pong')
main_win.fill((20, 59, 199))

font.init()
font = font.Font(None, 70)
lose = font.render('YOU LOSE!', True, (235, 115, 2))

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
        speed_x = 6
        speed_y = 6
        self.rect.x += speed_x
        self.rect.y += speed_y
        if self.rect.x > 695 or self.rect.x < 5:
            speed_x *= -1
        if self.rect.y > 495 or self.rect.y < 5:
            speed_y *= -1
            


player_1 = Player('rocket.png',100,250,10,70,70)
player_2 = Player('rocket.png',600,250,10,70,70)
ball = Ball('ball.png',130,280,0,20,20)

game = True
clock = time.clock()
fps = 60
finish = False

while game:
    if not finish:
        player_1.reset()
        player_1.update_1()
        player_2.reset()
        player_2.update_2()
        ball.update()

        if sptite.spritecollide(player_1, ball, False) or sprite.spritecollide(player_2, ball, False):
            speed_x *= -1

        if ball.rect.x < 100 or ball.rect.x > 600:
            finish = True
            window.blit(lose, 250,250)


        clock.tick(fps)
        display.update()