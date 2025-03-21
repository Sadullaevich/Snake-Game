import pygame
import Level1
import Buttons

pygame.init()

# create game screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# game variables
game_paused = False
menu_state = "main"

# define fonts
font = pygame.font.SysFont("arialblack", 40)

# define colours
TEXT_COL = (255, 255, 255)

# load images
play_img = pygame.image.load("./Resources/play.png").convert_alpha()
quit_img = pygame.image.load("./Resources/quit.png").convert_alpha()

# set buttons instances
resume_button = Buttons.Button(304, 125, play_img, 1)
quit_button = Buttons.Button(332, 257, quit_img, 1)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# pygame loop
run = True
while run:

    screen.fill((52, 78, 91))

    # game paused or not
    if game_paused:
        # check menu state
        if menu_state == "main":
            # draw pause buttons
            if resume_button.draw(screen):
                Level1.gameLoop()
            if quit_button.draw(screen):
                run = False
    else:
        draw_text("Press SPACE to start", font, TEXT_COL, 160, 250)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
