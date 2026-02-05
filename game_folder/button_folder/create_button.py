from .button_class import Button
from ..asset_folder.load_assets import Assetmanager




class Button_create():
    def __init__(self):
        self.buttons = {}
        self.assets = Assetmanager()


    def load_buttons(self, window_size):
        self.assets.load_assets(window_size)
        # knoppen laden
        self.buttons['start_button'] = Button(100, 200, self.assets.get_images('start_img'), 0.3)

        self.buttons['exit_button'] = Button(100, 600, self.assets.get_images('exit_img'), 0.3)

        self.buttons['how_to_button'] = Button(600, window_size.y - 200, self.assets.get_images('how_to_img'), 0.3)

        self.buttons['settings_button'] = Button(100, 400, self.assets.get_images('settings_img'), 0.3)

        self.buttons['return_button'] = Button(500,300,self.assets.get_images('return_img'), 0.3)

        self.buttons['anton_button'] = Button(300,500,self.assets.get_images('anton_button_img'),1)



    def get_buttons(self, name):
        #functie voor het oproepen van knoppen
        return self.buttons[name]