import pygame
import random
import time
import psycopg2

pygame.init()

# Настройки экрана и цвета
width, height = 600, 400
cell_size = 20
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
font = pygame.font.Font(None, 36)

# Подключение к базе данных
def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="5432"
    )

def get_user_id(username):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cur.fetchone()
    if result:
        user_id = result[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return user_id

def get_last_level(user_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT MAX(level) FROM user_score WHERE user_id = %s", (user_id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[0] if result[0] else 1

def save_score(user_id, score, level):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
                (user_id, score, level))
    conn.commit()
    cur.close()
    conn.close()
    print("Прогресс сохранён!")

# Классы змейки и еды
class Snake:
    def __init__(self):
        self.body = [(width // 2, height // 2)]
        self.direction = (cell_size, 0)
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        if new_head in self.body or new_head[0] < 0 or new_head[1] < 0 or new_head[0] >= width or new_head[1] >= height:
            return False
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        return True

    def change_direction(self, new_direction):
        if (new_direction[0] == -self.direction[0] and new_direction[1] == -self.direction[1]):
            return
        self.direction = new_direction

    def grow_snake(self):
        self.grow = True

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, green, (*segment, cell_size, cell_size))

class Food:
    def __init__(self, snake_body):
        self.position = self.generate_food(snake_body)
        self.weight = random.choice([1, 2, 3])
        self.color = self.get_color()
        self.spawn_time = time.time()
        self.lifetime = random.randint(5, 10)

    def generate_food(self, snake_body):
        while True:
            x = random.randint(0, (width // cell_size) - 1) * cell_size
            y = random.randint(0, (height // cell_size) - 1) * cell_size
            if (x, y) not in snake_body:
                return (x, y)

    def get_color(self):
        return {1: red, 2: blue, 3: yellow}[self.weight]

    def draw(self):
        pygame.draw.rect(screen, self.color, (*self.position, cell_size, cell_size))

    def is_expired(self):
        return time.time() - self.spawn_time > self.lifetime

def draw_text(text, x, y, color=white):
    screen.blit(font.render(text, True, color), (x, y))

# Главная игра
def main():
    username = input("Введите имя игрока: ")
    if len(username) > 100:
        print("Имя слишком длинное! Макс 100 символов.")
        return

    user_id = get_user_id(username)
    level = get_last_level(user_id)
    score = 0
    speed = 6 + (level - 1) * 2
    paused = False

    clock = pygame.time.Clock()
    snake = Snake()
    food = Food(snake.body)
    running = True

    while running:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score(user_id, score, level)
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: snake.change_direction((0, -cell_size))
                elif event.key == pygame.K_DOWN: snake.change_direction((0, cell_size))
                elif event.key == pygame.K_LEFT: snake.change_direction((-cell_size, 0))
                elif event.key == pygame.K_RIGHT: snake.change_direction((cell_size, 0))
                elif event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        save_score(user_id, score, level)

        if paused:
            draw_text("PAUSED", width // 2 - 60, height // 2, yellow)
            pygame.display.flip()
            clock.tick(5)
            continue

        if not snake.move():
            save_score(user_id, score, level)
            running = False

        if snake.body[0] == food.position:
            snake.grow_snake()
            score += food.weight
            food = Food(snake.body)
            if score % 5 == 0:
                level += 1
                speed += 2

        if food.is_expired():
            food = Food(snake.body)

        snake.draw()
        food.draw()
        draw_text(f"Score: {score}", 10, 10)
        draw_text(f"Level: {level}", 10, 40)

        pygame.display.flip()
        clock.tick(speed)

    pygame.quit()

if __name__ == "__main__":
    main()