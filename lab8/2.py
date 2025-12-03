import pygame
import random

pygame.init()

# цвета и тд
width, height = 600, 400
cell_size = 20
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

# экран
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# шрифт
font = pygame.font.Font(None, 36)


# класс змейки
class Snake:
    def __init__(self):
        self.body = [(width // 2, height // 2)]
        self.direction = (cell_size, 0)
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        # проверка на столкновение со стенами
        if new_head[0] < 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height:
            return False

        # проверка на столкновение с самой собой
        if new_head in self.body:
            return False

        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

        return True

    def change_direction(self, new_direction):
        """ изменение направления змейки, исключая движение назад """
        if (new_direction[0] == -self.direction[0] and new_direction[1] == -self.direction[1]):
            return
        self.direction = new_direction

    def grow_snake(self):
        self.grow = True

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, green, (segment[0], segment[1], cell_size, cell_size))


# класс еды
class Food:
    def __init__(self, snake_body):
        self.position = self.generate_food(snake_body)

    def generate_food(self, snake_body):
        """ генерация еды, избегая позиций змейки """
        while True:
            x = random.randint(0, (width // cell_size) - 1) * cell_size
            y = random.randint(0, (height // cell_size) - 1) * cell_size
            if (x, y) not in snake_body:
                return (x, y)

    def draw(self):
        pygame.draw.rect(screen, red, (self.position[0], self.position[1], cell_size, cell_size))


# функция отрисовки текста
def draw_text(text, x, y):
    text_surface = font.render(text, True, white)
    screen.blit(text_surface, (x, y))


# главная функция игры
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

        # обработка событий
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

        # движение змейки
        if not snake.move():
            running = False

            # проверка на поедание еды
        if snake.body[0] == food.position:
            snake.grow_snake()
            food = Food(snake.body)
            score += 1

            # повышение уровня каждые 3 еды
            if score % 3 == 0:
                level += 1
                speed += 2  # ускорение

        # отрисовка объектов
        snake.draw()
        food.draw()
        draw_text(f"score: {score}", 10, 10)
        draw_text(f"level: {level}", 10, 40)

        pygame.display.flip()
        clock.tick(speed)

    pygame.quit()


if __name__ == "__main__":
    main()