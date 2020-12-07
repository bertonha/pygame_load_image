import pygame


running = True

pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill(pygame.Color(0, 0, 0))
imgsize = pygame.Surface.get_size(screen)

images = ["1.jpg", "2.jpg", "3.jpg"]
image_index = 1


def load_image(index):
    image = f'{index}.jpg'
    background = pygame.image.load(image)
    background = pygame.transform.scale(background, (imgsize[0], imgsize[1]))
    screen.blit(background, (0, 0))
    pygame.display.update()


def inc_index(index):
    new_index = index + 1
    if new_index > 3:
        new_index = 1
    return new_index


while running:
    load_image(image_index)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            image_index = inc_index(image_index)
            load_image(image_index)

        if event.type == pygame.KEYDOWN:
            running = False

pygame.quit()
