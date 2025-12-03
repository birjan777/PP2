import pygame
import random

pygame.init()

# экран
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Собирай монеты!")

# машины и все такое
glavnaya = pygame.image.load(r"lab8\image\first.png")
soperniki = pygame.image.load(r"lab8/image/Enemy.png")
moneta = pygame.image.load(r"lab8\image\moneta.png")
road = pygame.image.load(r"lab8\image\street.png")

# размеры
glavnaya = pygame.transform.scale(glavnaya, (100, 130))
soperniki = pygame.transform.scale(soperniki, (50, 110))
moneta = pygame.transform.scale(moneta, (30, 30))
road = pygame.transform.scale(road, (400, 600))

# скорость
speed = 5
road_y = 0
# шрифт для текста
font = pygame.font.Font(None, 36)


# классы главной машины
class GlavnayaCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = glavnaya
        self.rect = self.image.get_rect(center=(width // 2, height - 120))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += speed

    def draw(self):
        screen.blit(self.image, self.rect)

    # класс другой машины


class SopernikCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = soperniki
        self.rect = self.image.get_rect(center=(random.randint(50, width - 50), -50))

    def move(self):
        self.rect.y += speed
        if self.rect.top > height:
            self.rect.center = (random.randint(50, width - 50), -50)

    def draw(self):
        screen.blit(self.image, self.rect)


# класс койна
class Moneta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = moneta
        self.rect = self.image.get_rect(center=(random.randint(50, width - 50), -50))

    def move(self):
        self.rect.y += speed
        if self.rect.top > height:
            self.respawn()

    def respawn(self):
        self.rect.center = (random.randint(50, width - 50), -50)

    def draw(self):
        screen.blit(self.image, self.rect)


# функция перезапуска игры
def reset_game():
    global player, enemy, coin, score, game_over
    player = GlavnayaCar()
    enemy = SopernikCar()
    coin = Moneta()
    score = 0
    game_over = False


# запуск игры
reset_game()

# цикл
running = True
while running:
    screen.fill((255, 255, 255))

    # дорога движение
    road_y += speed
    if road_y >= height:
        road_y = 0

    screen.blit(road, (0, road_y - height))
    screen.blit(road, (0, road_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_SPACE:
                reset_game()

    if not game_over:
        # машина и монета дживение
        player.move()
        enemy.move()
        coin.move()

        # если столкнется с машиной
        if player.rect.colliderect(enemy.rect):
            game_over = True

            # сбор монет
        if player.rect.colliderect(coin.rect):
            score += 1
            coin.respawn()

            # видимость обьектов
        player.draw()
        enemy.draw()
        coin.draw()

        # общ счет
        score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    else:
        game_over_text = font.render(f"game over! score: {score}", True, (255, 255, 255))
        screen.blit(game_over_text, (width // 2 - 100, height // 2 - 20))

    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()

