from pygame import *

win_width, win_height = 600, 500
window = display.set_mode((win_width, win_height))
back = (200, 255, 255) 

class GameSprite(sprite.Sprite):
    def __init__(self, color, x, y, speed, w, h):
        super().__init__()
        self.image = Surface((w, h))
        self.image.fill(color)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5: self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 155: self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5: self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 155: self.rect.y += self.speed


racket1 = Player((0, 0, 255), 30, 200, 5, 20, 150)
racket2 = Player((0, 0, 255), 550, 200, 5, 20, 150)
ball = GameSprite((255, 0, 0), 200, 200, 4, 30, 30)

game, finish = True, False
clock = time.Clock()
speed_x, speed_y = 3, 3

while game:
    for e in event.get():
        if e.type == QUIT: game = False

    if not finish:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.y > win_height - 30 or ball.rect.y < 0:
            speed_y *= -1

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(60)