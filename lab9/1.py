import pygame
from pygame.locals import *
from random import randint, choice
import time

pygame.init()

# Музыка
pygame.mixer.music.load("images/background.wav")
pygame.mixer.music.play()

# Основные переменные
done = False
clock = pygame.time.Clock()
speed = 5
score = 0
count_of_coins = 0
cirle = 1

# Фон
background = pygame.image.load("images/AnimatedStreet.png")
background = pygame.transform.scale(background, (400, 600))

# Цвета
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Шрифты
font = pygame.font.SysFont("Verdana", 50)
GAME_TOCHNO_OVER = font.render("GAME OVER", True, BLACK)
WE_DID_IT = font.render("SCORE:", True, BLACK)
BOHACH = font.render("COINS:", True, YELLOW)

# Экран
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer")
screen.fill(WHITE)


# Вражеская машина
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (randint(40, 360), -100)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.bottom > 710:
            score += 1
            self.rect.top = -100
            self.rect.center = (randint(30, 370), -100)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# Игрок
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Player.png")
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < 400 and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# Монеты трех видов
coin_data = {
    "images/coin1.png": 1,
    "images/coin5.png": 5,
    "images/coin10.png": 10
}
coin_images = list(coin_data.keys())


class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.respawn()

    def move(self):
        self.rect.move_ip(0, 8)
        if self.rect.bottom > 710:
            self.respawn()

    def respawn(self):
        self.image_path = choice(coin_images)
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (randint(10, 390), -50)
        self.value = coin_data[self.image_path]

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# Объекты
P1 = Player()
E1 = Enemy()
C1 = Coins()

# Ускорение
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Игровой цикл
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if count_of_coins > 50 * cirle:
        cirle += 2
        speed += 2

    screen.blit(background, (0, 0))
    P1.move()
    E1.move()

    denga = font.render(str(count_of_coins), True, YELLOW)
    screen.blit(denga, (10, 50))
    scores = font.render(str(score), True, WHITE)
    screen.blit(scores, (10, 5))

    P1.draw(screen)
    E1.draw(screen)

    if P1.rect.colliderect(E1.rect):
        pygame.mixer.music.stop()
        pygame.mixer.Sound("images/crash.wav").play()
        time.sleep(0.5)

        screen.fill(RED)
        screen.blit(GAME_TOCHNO_OVER, (50, 250))
        screen.blit(WE_DID_IT, (50, 320))
        screen.blit(scores, (250, 320))
        screen.blit(BOHACH, (50, 380))
        screen.blit(denga, (250, 380))
        pygame.display.update()
        time.sleep(5)
        done = True

    if P1.rect.colliderect(C1.rect):
        count_of_coins += C1.value
        C1.respawn()
    else:
        C1.move()
        C1.draw(screen)

    pygame.display.flip()
    clock.tick(60)
