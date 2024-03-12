import pygame

BASE_IMG_PATH = 'data/images/'

def load_image(path):
    # El convert de aqui permite optimizacion
    img = pygame.image.load(BASE_IMG_PATH+path).convert()
    img.set_colorkey((0, 0, 0))

    return img