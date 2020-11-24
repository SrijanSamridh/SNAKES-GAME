import pygame
import random
import os

x = pygame.init()
# colours
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Srijan's First Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, colour, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, colour, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(black)
        text_screen("WELCOME to SNAKE GAMES", (0, 223, 90), 300, 250)
        text_screen(" by (SRIJAN SAMRIDH)", white, 325, 290)
        text_screen("[Press SPACE]", red, 380, 530)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameLoop()

        pygame.display.update()
        clock.tick(60)

# Creating a game loop
def gameLoop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    snake_list = []
    snake_length = 1
    # check if highscore file exists
    if (not  os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    snake_size = 10
    fps = 60

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))

            gameWindow.fill(white)
            text_screen("Game Over! "
                        "[Press Enter To continue]", red, screen_width / 4, screen_height / 2)
            # text_screen("Game Over! Press Enter To continue", red, 200, 300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # print("You have pressed right arrow key")
                        # snake_x = snake_x + 10
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        # print("You have pressed right arrow key")
                        # snake_x = snake_x - 10
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        # print("You have pressed right arrow key")
                        # snake_y = snake_y - 10
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        # print("You have pressed right arrow key")
                        # snake_y = snake_y + 10
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_i:
                        score += 100

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 12

                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snake_length += 5
                # print(highscore)
                if score > int(highscore):
                    highscore = score

            gameWindow.fill(black)
            text_screen("Score: " + str(score) + "  High Score: " + str(highscore), white, 5, 5)
            pygame.draw.rect(gameWindow, white, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
            # pygame.draw.rect(gameWindow, red, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, red, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)



    pygame.quit()
    quit()
welcome()
# gameLoop()