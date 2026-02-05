import pygame as pg


class Assetmanager():
    def __init__(self):
        #dictionary maken voor geluid, afbeeldingen en etc.
        self.images = {}
        self.sound = {}
        self.music = {}


    def load_assets(self,window_size):
        # afbeeldingen van knoppen laden
        self.images['start_img'] = pg.image.load('albeedingen/knoppen/napoleonic/Start.png').convert_alpha()
        self.images['exit_img'] = pg.image.load('albeedingen/knoppen/napoleonic/Quit.png').convert_alpha()
        self.images['how_to_img'] = pg.image.load('albeedingen/knoppen/napoleonic/How_to_play.png').convert_alpha()
        self.images['how_to_img'] = pg.transform.scale(self.images['how_to_img'], (200,200))
        self.images['settings_img'] = pg.image.load('albeedingen/knoppen/napoleonic/Settings.png').convert_alpha()
        self.images["return_img"]= pg.image.load('albeedingen/knoppen/napoleonic/back_arrow.png').convert_alpha()
        self.images["anton_button_img"] = pg.image.load('albeedingen/button_anton.png').convert_alpha()

        # afbeeldingen laden
        self.images["anton_img"] = pg.image.load('albeedingen/anton.png')
        self.images["anton_img"] = pg.transform.scale(
            self.images["anton_img"],
            (int(window_size.x), int(window_size.y))
        )

        # achtergrond laden
        self.images["menu"] = pg.image.load(
            'albeedingen/achtergrond/napoleonic/achtergrond_menu.png').convert_alpha()
        self.images["menu"] = pg.transform.scale(
            self.images["menu"],
            (int(window_size.x), int(window_size.y))
        )
        self.images["spel_achtergrond"] = pg.image.load(
            'albeedingen/achtergrond/spel_achtergrond.jpg').convert_alpha()
        self.images["spel_achtergrond"] = pg.transform.scale(
            self.images["spel_achtergrond"],
            (int(window_size.x), int(window_size.y))
        )

        #muziek laden
        self.music["menu_muziek"] = pg.mixer.music.load('geluid/muziek/Two Steps From Hell - Victory.ogg')


        #geluidseffecten laden
        self.sound['anton_schreeuw'] = pg.mixer.Sound('geluid/keemstar-screaming.mp3')






    def get_images(self, name):
        #functie voor het oproepen van afbeeldingen
        return self.images[name]

    def get_music(self,name):
        #fucntie voor het oproepen van muziek
        return self.music[name]

    def get_sound(self,name):
        #functie voor het oproepen van geluidseffecten
        return self.sound[name]

