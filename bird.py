import pygame as pg
from settings import *

class Bird(pg.sprite.Sprite):
    def __init__(self):
        super(Bird, self).__init__()
        self.load_animations()
        self.current_animation = self.animation
        self.current_image = 0
        self.image = self.current_animation[self.current_image]
        self.angle = 0
        self.is_flying = False

        self.timer = pg.time.get_ticks()
        self.interval = 200
        self.gravity = 2

        self.velocity_x = 0
        self.velocity_y = 0

        self.jump_sound = pg.mixer.Sound("jump.mp3")

        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2)

    def update(self):
        if pg.time.get_ticks() - self.timer > self.interval:
            self.current_image += 1
            if self.current_image >= len(self.current_animation):
                self.current_image = 0
            self.image = pg.transform.rotate(self.current_animation[self.current_image], self.angle)
            self.timer = pg.time.get_ticks()
        if pg.mouse.get_pressed()[0] and not self.is_flying:
            self.jump()
        else:
            self.is_flying = False
        self.rect.y += self.velocity_y
        self.velocity_y += self.gravity
        self.angle -= 3

    def jump(self):
        self.velocity_y = -16
        self.angle = 30
        self.is_flying = True
        self.jump_sound.play()

    def load_animations(self):
        self.animation = []
        num_images = 4
        sprite_sheet = pg.image.load("Flappy Bird Assets 1.6 (Zip)/Flappy Bird Assets/Player/StyleBird1/Bird1-1.png")
        for i in range(num_images):
            x = i * 16
            y = 0
            rect = pg.Rect(x, y, 16, 16)
            image = sprite_sheet.subsurface(rect)
            image = pg.transform.scale_by(image, 2)
            self.animation.append(image)
