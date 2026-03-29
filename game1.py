import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("xomrak Pong")

# Цвета
WHITE = (255, 255, 255)

# Загрузка изображений
try:
    background = pygame.image.load('spalny.jpg')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    
    ball_img = pygame.image.load('xomrak.png')
    ball_img = pygame.transform.scale(ball_img, (50, 50))
    
    paddle_img = pygame.image.load('bita.png')
    paddle_img = pygame.transform.scale(paddle_img, (20, 100))
except pygame.error as e:
    print(f"Ошибка загрузки изображений: {e}")
    pygame.quit()
    sys.exit()

# Параметры объектов
ball_rect = ball_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
ball_speed_x = 5
ball_speed_y = 5

player_rect = paddle_img.get_rect(midleft=(20, HEIGHT // 2))
opponent_rect = paddle_img.get_rect(midright=(WIDTH - 20, HEIGHT // 2))

paddle_speed = 7
clock = pygame.time.Clock()

# Главный цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление игроком (стрелки Вверх/Вниз)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect.y -= paddle_speed
    if keys[pygame.K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect.y += paddle_speed

    # Простая логика противника (автоматическое слежение за мячом)
    if opponent_rect.centery < ball_rect.centery:
        opponent_rect.y += paddle_speed
    if opponent_rect.centery > ball_rect.centery:
        opponent_rect.y -= paddle_speed

    # Движение мяча
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    # Отскок от верхней и нижней границ
    if ball_rect.top <= 0 or ball_rect.bottom >= HEIGHT:
        ball_speed_y *= -1

# Столкновение с ракетками
    if ball_rect.colliderect(player_rect) or ball_rect.colliderect(opponent_rect):
        ball_speed_x *= -1

    # Выход мяча за границы (сброс в центр)
    if ball_rect.left <= 0 or ball_rect.right >= WIDTH:
        ball_rect.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1

    # Отрисовка
    screen.blit(background, (0, 0))
    screen.blit(ball_img, ball_rect)
    screen.blit(paddle_img, player_rect)
    screen.blit(paddle_img, opponent_rect)

    pygame.display.flip()
    clock.tick(60)
