import pygame
import random
import time

pygame.init()

# Настройки экрана
width, height = 600, 400
cell_size = 20
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)

# Экран
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Шрифт
font = pygame.font.Font(None, 36)


# Класс змейки
class Snake:
    def __init__(self):
        self.body = [(width // 2,height // 2)]
        self.direction = (cell_size, 0)
        self.grow = False



    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0],
                    head_y + self.direction[1])



        # Проверка на столкновение со стенами
        if new_head[0] < 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height:
            return False



        # Проверка на столкновение с самой собой

        if new_head in self.body:
            return False

        self.body.insert(0,new_head)

        if self.grow:
            self.grow = False

        else:
            self.body.pop()

        return True



    def change_direction(self, new_direction):
        """ Изменение направления змейки, исключая движение назад """
        if (new_direction[0] == -self.direction[0] and new_direction[1] == -self.direction[1]):
            return
        self.direction = new_direction

    def grow_snake(self):
        self.grow = True

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, green, (segment[0], segment[1], cell_size, cell_size))



# Класс еды с разными весами, цветами и временем исчезновения
class Food:
    def __init__(self, snake_body):
        self.position = self.generate_food(snake_body)
        self.weight = random.choice([1, 2, 3])  # Случайный вес еды
        self.color = self.get_color()  # Цвет в зависимости от веса
        self.spawn_time = time.time()  # Время появления еды
        self.lifetime = random.randint(5, 10)  # Время до исчезновения еды





    def generate_food(self, snake_body):
        """ Генерация еды, избегая позиций змейки """
        while True:
            x = random.randint(0, (width // cell_size) - 1) * cell_size
            y = random.randint(0, (height // cell_size) - 1) * cell_size
            if (x, y) not in snake_body:
                return (x, y)




    def get_color(self):
        """ Определяет цвет еды в зависимости от её веса """
        if self.weight == 1:
            return red
        elif self.weight == 2:
            return blue
        else:
            return yellow

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], cell_size, cell_size))

    def is_expired(self):
        """ Проверка, истекло ли время жизни еды """
        return time.time() - self.spawn_time > self.lifetime


# Функция отрисовки текста
def draw_text(text, x, y):
    text_surface = font.render(text, True, white)
    screen.blit(text_surface, (x, y))


# Главная функция игры
def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food(snake.body)

    score = 0
    level = 1
    speed = 6
    running = True

    while running:
        screen.fill(black)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -cell_size))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, cell_size))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-cell_size, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((cell_size, 0))

        # Движение змейки
        if not snake.move():
            running = False

            # Проверка на поедание еды
        if snake.body[0] == food.position:
            snake.grow_snake()
            score += food.weight
            food = Food(snake.body)

            # Повышение уровня каждые 5 очков
            if score % 5 == 0:
                level += 1
                speed += 2  # Ускорение

        # Проверка, не исчезла ли еда
        if food.is_expired():
            food = Food(snake.body)

        # Отрисовка объектов
        snake.draw()
        food.draw()
        draw_text(f"Score: {score}", 10, 10)
        draw_text(f"Level: {level}", 10, 40)

        pygame.display.flip()
        clock.tick(speed)

    pygame.quit()


if __name__ == "__main__":
    main()