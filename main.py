import pygame


def load_image(index):
    background = pygame.image.load(f'{index}.jpg')
    background = pygame.transform.scale(background, (img_size[0], img_size[1]))
    background = background.convert_alpha()
    return background


def inc_index(index):
    new_index = index + 1
    if new_index > 3:
        new_index = 1
    return new_index


def fade(background):
    for alpha in range(0, 300, 2):
        screen.fill(pygame.Color(0, 0, 0))
        background.set_alpha(alpha)
        screen.blit(background, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)


running = True

pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill(pygame.Color(0, 0, 0))
img_size = pygame.Surface.get_size(screen)

image_index = 1

# load initial image
background = load_image(image_index)
screen.blit(background, (0, 0))
pygame.display.update()


while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            image_index = inc_index(image_index)
            background = load_image(image_index)
            fade(background)

        if event.type == pygame.KEYDOWN:
            running = False

pygame.quit()
