import pygame as pg
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

from .countries_folder.countries import World
from .asset_folder.load_assets import Assetmanager
from .button_folder.create_button import Button_create

class Game():
    def __init__(self, screen: pg.Surface, clock: pg.time.Clock(),window_size: pg.Vector2,):
        self.screen = screen
        self.clock = clock
        self.window_size = window_size
        self.image_size_y = pg.image
        self.font = pg.font.SysFont(None, 24)
        self.playing = True
        self.state = "menu"
        self.world = World()
        self.assets = Assetmanager()
        self.assets.load_assets(self.window_size)
        self.country_names = list(self.world.countries.keys())
        self.create_buttons = Button_create()
        self.create_buttons.load_buttons(self.window_size)
        self.slider = Slider(
            self.screen,
            100, 100,
            800, 40,
            min=0,
            max=100,
            step=1
        )

        self.slider_output = TextBox(
            self.screen,
            475, 200,
            50, 50,
            fontSize=30
        )

        self.slider_output.disable()
        self.volume = 0.5
        self.music()





    def run(self):
        while self.playing:
            events = pg.event.get()
            self.clock.tick(60)
            self.events(events)
            self.update()
            self.draw()
            self.music_volume()

            pygame_widgets.update(events)
            pg.display.update()


    def events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.playing = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playing = False


    def update(self):
        self.world.update()

    def draw(self):
        self.screen.fill((0, 0, 0))

        if self.state == "menu":

            self.screen.blit(self.assets.get_images('menu'), (0, 0))
            if self.create_buttons.get_buttons('start_button').draw(self.screen):
                self.state = "spel"
                print("Start knop geklikt")

            if self.create_buttons.get_buttons('exit_button').draw(self.screen):
                self.playing = False

            if self.create_buttons.get_buttons('how_to_button').draw(self.screen):
                print("How to play")

            if self.create_buttons.get_buttons('settings_button').draw(self.screen):
                print("Settings")
                self.state = "settings"

        if self.state == "spel":
            self.screen.blit(self.assets.get_images('spel_achtergrond'),(0,0))
            self.world.draw(self.screen)
            text_surface = self.font.render(f"Fps: {int(self.clock.get_fps())}", False, (255,255,255))
            self.screen.blit(text_surface, (10,10))

            if self.create_buttons.get_buttons('return_button').draw(self.screen):
                self.state = 'menu'

        if self.state == "settings":
            self.screen.fill((255, 255, 255))

            self.slider.show()
            self.slider_output.show()

            self.slider_output.setText(str(int(self.slider.getValue())))
            if self.create_buttons.get_buttons('anton_button').draw(self.screen):
                self.state = "ANTON"

            if self.create_buttons.get_buttons('return_button').draw(self.screen):
                self.state = "menu"

        if self.state != "settings":
            self.slider.hide()
            self.slider_output.hide()

        if self.state == "ANTON":
            self.screen.blit(self.assets.get_images('anton_img'),(0,0))
            pg.mixer_music.pause()
            pg.mixer.Sound.play(self.assets.get_sound('anton_schreeuw'))


    def music(self):
        pg.mixer.music.set_volume(self.volume)
        pg.mixer.music.play(-1)

    def music_volume(self):
        self.volume = self.slider.getValue() / 100
        pg.mixer.music.set_volume(self.volume)