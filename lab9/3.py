import pygame
from math import sqrt

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
prevX = 0  # всегла меняются при движений курсора
prevY = 0
startX = -1  # фиксирует стартовую точку
startY = -1

color = (255, 255, 255)
screen.fill((0, 0, 0))

isMouseDown = False
mode = 0  # 0 ручка 1 прямоугольник. 2 круг. 3 ластик.  4квадрат.  5Right T. 6Equil T. 7Rhombus.

running = True
while running:
    currentX = prevX
    currentY = prevY

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка нажатий мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                isMouseDown = True
                startX, startY = event.pos  # запоминает где была нажата мышка
                temp_surface = screen.copy()

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                isMouseDown = False

        if event.type == pygame.MOUSEMOTION:
            currentX, currentY = event.pos  # координаты при движений

        # Смена цвета
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255, 0, 0)
            elif event.key == pygame.K_g:
                color = (0, 255, 0)
            elif event.key == pygame.K_b:
                color = (0, 0, 255)
            elif event.key == pygame.K_w:
                color = (255, 255, 255)

            # Переключение режимов
            elif event.key == pygame.K_1:
                mode = 1  # Прямоугольник
            elif event.key == pygame.K_2:
                mode = 2  # Круг
            elif event.key == pygame.K_3:
                mode = 3  # Ластик
            elif event.key == pygame.K_0:
                mode = 0  # Перо
            elif event.key == pygame.K_4:
                mode = 4  # квадрат
            elif event.key == pygame.K_5:
                mode = 5  # right
            elif event.key == pygame.K_6:
                mode = 6  # equilat
            elif event.key == pygame.K_7:
                mode = 7  # rhombus

    # Перо
    if isMouseDown and mode == 0:
        pygame.draw.line(screen, color, (prevX, prevY), (currentX, currentY))

    # Прямоугольник
    if isMouseDown and mode == 1 and startX != -1 and startY != -1:
        screen.blit(temp_surface, (0, 0))
        pygame.draw.rect(screen, color,
                         (min(startX, currentX), min(startY, currentY), abs(currentX - startY), abs(currentY - startY)),
                         1)

    # Круг
    if isMouseDown and mode == 2 and startX != -1 and startY != -1:
        screen.blit(temp_surface, (0, 0))
        centerX = (startX + currentX) // 2
        centerY = (startY + currentY) // 2
        radius = int(sqrt((currentX - startX) ** 2 + (currentY - startY) ** 2) // 2)
        pygame.draw.circle(screen, color, (centerX, centerY), radius, 1)

    # Square
    if isMouseDown and mode == 4 and startX != -1 and startY != -1:
        screen.blit(temp_surface, (0, 0))
        pygame.draw.rect(screen, color,
                         (min(startX, currentX), min(startY, currentY), abs(currentX - startY), abs(currentX - startY)),
                         1)

    # Right triangle
    if isMouseDown and mode == 5 and startX != -1 and startY != -1:
        screen.blit(temp_surface, (0, 0))
        points = [
            (startX, startY),  # Прямой угол
            (startX, currentY),  # Вертикальная сторона
            (currentX, currentY)  # Гипотенуза
        ]
        pygame.draw.polygon(screen, color, points, 1)

    # Equilateral triangle
    if isMouseDown and mode == 6 and startX != -1 and startY != -1:
        screen.blit(temp_surface, (0, 0))
        # длина стороны
        side_length = max(abs(currentX - startX), abs(currentY - startY))

        # вершина треугольника
        height = side_length * (3 ** 0.5) / 2  # высота
        points = [
            (startX, startY),  # Верхняя вершина
            (startX - side_length / 2, startY + height),  # левая нижняя
            (startX + side_length / 2, startY + height)  # правая нижняя
        ]

        pygame.draw.polygon(screen, color, points, 1)

    # Rhombus
    if isMouseDown and mode == 7 and startX != -1 and startY != -1:
        screen.blit(temp_surface, (0, 0))
        # половины диагоналей
        half_width = abs(currentX - startX) // 2
        half_height = abs(currentY - startY) // 2

        # центр ромба
        center_x = startX
        center_y = startY

        # вершины ромба
        points = [
            (center_x, center_y - half_height),  # верхняя
            (center_x + half_width, center_y),  # правая
            (center_x, center_y + half_height),  # нижняя
            (center_x - half_width, center_y)  # левая
        ]

        pygame.draw.polygon(screen, color, points, 1)

    # Ластик
    if isMouseDown and mode == 3:
        pygame.draw.line(screen, (0, 0, 0), (prevX, prevY), (currentX, currentY), 30)

    prevX = currentX
    prevY = currentY

    pygame.display.flip()
    clock.tick(45)

pygame.quit()