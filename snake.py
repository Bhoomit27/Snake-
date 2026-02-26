import pygame, sys, random

pygame.init()
screen_size = 600
score = 0
screen = pygame.display.set_mode((screen_size,screen_size))
clock = pygame.time.Clock()

snake = [(1, 1)]
snake_size = 40
direction = (0, 0)
food = (random.randrange(0, 15, 1), random.randrange(0, 15, 1))

def start_screen():
    title_font = pygame.font.SysFont("comicsansms", 50)
    subtitle_font = pygame.font.SysFont("comicsansms", 25)

    title_text = title_font.render("Snake Game", True, "green")
    subtitle_text = subtitle_font.render("By Bhoomit", True, "white")
    instruction_text = subtitle_font.render("Press any key to start", True, "white")

    while True:
        screen.fill("black")

        # Center the text
        screen.blit(
            title_text,
            (screen_size//2 - title_text.get_width()//2, screen_size//2 - 80)
        )
        screen.blit(
            subtitle_text,
            (screen_size//2 - subtitle_text.get_width()//2, screen_size//2 - 20)
        )
        screen.blit(
            instruction_text,
            (screen_size//2 - instruction_text.get_width()//2, screen_size//2 + 40)
        )

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return   # Exit start screen and start game
        
        clock.tick(15)

start_screen()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direction == (0,1):
                    continue
                else:
                    direction = (0, -1)
            if event.key == pygame.K_DOWN:
                if direction == (0 ,-1):
                    continue
                else: 
                    direction = (0, 1)
            if event.key == pygame.K_LEFT: 
                if direction == (1,0):
                    continue
                else:
                    direction = (-1, 0)
            if event.key == pygame.K_RIGHT: 
                if direction == (-1,0):
                    continue
                else:
                    direction = (1, 0)
            
    snake = [(snake[0][0] + direction[0], snake[0][1] + direction[1])] + snake[:-1]
    
    if snake[0] in snake[1:]:
        snake = [(1,1)]
        direction = (0,0)
        score = 0
        pygame.display.set_caption(f"Points:{str(score)}")

    if snake[0] == food:
        food = (random.randrange(0, 15, 1), random.randrange(0, 15, 1))
        while food in snake:
            food = (random.randrange(0, 15, 1), random.randrange(0, 15, 1))

        snake.append(snake[-1])
        score = score + 1
        pygame.display.set_caption(f"Points:{str(score)}")

    if snake[0][0] > 15 or snake[0][0] < 0:
        snake = [(1,1)]
        direction = (0,0)
        score = 0
        pygame.display.set_caption(f"Points:{str(score)}")
    if snake[0][1] > 15 or snake[0][1] < 0:
        snake = [(1,1)]
        direction = (0,0)
        score = 0
        pygame.display.set_caption(f"Points:{str(score)}")

    screen.fill((0, 0, 0))

    for x in range(screen_size//snake_size):  
        for y in range(screen_size//snake_size):
            pygame.draw.rect(screen ,"white",(x*snake_size,y*snake_size,snake_size,snake_size),1)


    for segment in snake: 
        pygame.draw.rect(screen, "white", (segment[0]*snake_size,segment[1]*snake_size, snake_size, snake_size),0)

    pygame.draw.rect(screen, (255, 0, 0), (food[0]*snake_size,food[1]*snake_size, snake_size, snake_size),0)
    pygame.display.flip()
    clock.tick(10)