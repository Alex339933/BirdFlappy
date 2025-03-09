import pygame as pg
from settings import *
import random

class Pipe(pg.sprite.Sprite):
    def __init__(self, is_top, height):
        super().__init__()
        spritesheet = pg.image.load("Flappy Bird Assets 1.6 (Zip)/Flappy Bird Assets/Tiles/Style 1/PipeStyle1.png")
        self.image = pg.Surface((32, height), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        if is_top:
            top = spritesheet.subsurface((0, 0, 32, 18))
            mid = spritesheet.subsurface((0, 18, 32, 16))
            mid = pg.transform.scale(mid, (32, height))
            self.image.blit(mid, (0, 0))
            self.image.blit(top, (0, 0))
            self.rect.bottom = SCREEN_HEIGHT
        else:
            bot = spritesheet.subsurface((0, 62, 32, 18))
            mid = spritesheet.subsurface((0, 18, 32, 16))
            mid = pg.transform.scale(mid, (32, height))
            self.image.blit(mid, (0, 0))
            self.image.blit(bot, (0, height - 18))
            self.rect.top = 0

    def update(self, speed):
        self.rect.x -= speed
