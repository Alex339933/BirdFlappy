import pygame as pg
from settings import *
from bird import Bird
from pipe import Pipe
import time
import random

pg.init()
font = pg.font.Font(None, 36)

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("BirdFlappy")
        self.timer = pg.time.get_ticks()
        self.interval = 700

        self.game_over_text = font.render("Проигрыш!", True, pg.Color("red"))
        self.game_over_text_rect = self.game_over_text.get_rect()
        self.game_over_text_rect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

        self.score_text = font.render("Счёт: 0", True, pg.Color("white"))
        self.score_text_rect = self.score_text.get_rect()

        self.game_over_sound = pg.mixer.Sound("game_over.wav")

        self.setup()

    def setup(self):
        self.mode = "game"
        self.clock = pg.time.Clock()
        self.background = pg.image.load("Flappy Bird Assets 1.6 (Zip)/Flappy Bird Assets/Background/Background4.png")
        self.background = pg.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.all_sprites = pg.sprite.Group()

        self.score = -1

        self.bird = Bird()
        self.all_sprites.add(self.bird)

        self.pipes = pg.sprite.Group()

        self.speed = 5

        self.run()

    def run(self):
        self.game_running = True
        while self.game_running:
            self.event()
            self.draw()
            self.update()
            self.clock.tick(FPS)
        pg.quit()
        quit()

    def increase_score(self):
        self.score += 1
        self.score_text = font.render(f"Счёт: {self.score}", True, pg.Color("white"))
        self.score_text_rect = self.score_text.get_rect()

        if self.score % 10 == 0:
            self.speed += 1

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game_running = False
            if self.mode == "game over" and event.type == pg.MOUSEBUTTONDOWN:
                self.mode = "game"
                self.setup()


    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        self.pipes.draw(self.screen)
        self.screen.blit(self.score_text, self.score_text_rect)
        if self.mode == "game over":
            self.screen.blit(self.game_over_text, self.game_over_text_rect)
            self.game_over_sound.play()
        pg.display.flip()

    def update(self):
        self.bird.update()
        if self.mode == "game over":
            return
        self.pipes.update(self.speed)

        if pg.time.get_ticks() - self.timer > self.interval:
            height = random.randint(100, 700)
            self.pipes.add(Pipe(False, height))
            self.pipes.add(Pipe(True, SCREEN_HEIGHT - (height + GAP)))
            self.increase_score()
            self.timer = pg.time.get_ticks()

        if pg.sprite.spritecollide(self.bird, self.pipes, False) or self.bird.rect.y > SCREEN_HEIGHT:
            self.mode = "game over"





if __name__ == "__main__":
    game = Game()
