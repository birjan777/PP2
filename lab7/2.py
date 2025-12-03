import pygame
import os

pygame.init()

# Создаём плейлист
playlist = []

# Путь к музыке (используем / вместо \)
music_folder = "/Users/khalenovbirzhan/PycharmProjects/PythonProject3/musics"
allmusic = os.listdir(music_folder)

for song in allmusic:
    if song.endswith(".mp3") or song.endswith(".ogg"):
        playlist.append(os.path.join(music_folder, song))

# Окно
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

# Фон для текста
bg = pygame.Surface((500, 200))
bg.fill((255, 255, 255))

font2 = pygame.font.SysFont(None, 20)

# Кнопки
playb = pygame.image.load(os.path.join("music-elements", "play.png"))
pausb = pygame.image.load(os.path.join("music-elements", "pause.png"))
nextb = pygame.image.load(os.path.join("music-elements", "next.png"))
prevb = pygame.image.load(os.path.join("music-elements", "back.png"))

index = 0
aplay = False

# Загрузка первой песни
pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play(1)
aplay = True

run = True

while run:
    screen.fill((100, 100, 100))  # цвет фона окна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_RIGHT:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

    # Отображение текста и кнопок
    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))
    screen.blit(bg, (155, 500))
    screen.blit(text2, (300, 500))

    playb_scaled = pygame.transform.scale(playb, (70, 70))
    pausb_scaled = pygame.transform.scale(pausb, (70, 70))
    nextb_scaled = pygame.transform.scale(nextb, (70, 70))
    prevb_scaled = pygame.transform.scale(prevb, (75, 75))

    if aplay:
        screen.blit(pausb_scaled, (370, 590))
    else:
        screen.blit(playb_scaled, (370, 590))
    screen.blit(nextb_scaled, (460, 587))
    screen.blit(prevb_scaled, (273, 585))

    clock.tick(24)
    pygame.display.update()