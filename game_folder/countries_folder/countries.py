import pygame as pg
import os
import json
from shapely.geometry import Point, Polygon
from ..text_folder.text import draw_text, draw_multiline_text

class Country():
    def __init__(self, name:str, coords:list):
        self.name = name
        self.coords = coords
        self.polygon = Polygon(self.coords)
        self.hovered = False
        self.discovered = False



    def update(self, mouse_pos:pg.Vector2):
        self.hovered = False
        if Point(mouse_pos.x, mouse_pos.y).within(self.polygon):
            self.hovered = True

    def draw(self, screen: pg.Surface, scroll: pg.Vector2):
        if self.hovered:
            color = (255, 0, 0)  # hover met muis
        else:
            color = (60, 60, 60)
        pg.draw.polygon(
            screen,
            color,
            [(x - scroll.x, y - scroll.y) for x, y in self.coords]
        )

        # outline altijd zichtbaar (door wolken)
        pg.draw.polygon(
            screen,
            (255, 255, 255),
            [(x - scroll.x, y - scroll.y) for x, y in self.coords],
            width=1
        )




class World:

    MAP_WIDTH = 2.05 * 4000
    MAP_HEIGHT = 1.0 * 4000
    def __init__(self):
        self.read_geo_data()
        self.countries = self.create_countries()
        self.scroll = pg.Vector2(3650,395 )


        self.hovered_country = None
        self.hover_surface = pg.Surface((300,100), pg.SRCALPHA)
        self.hover_surface.fill((25,24,86, 155))
 # BEKIJK DIT EENSSSS; 
    def read_geo_data(self):
        with open('game_folder/countries_folder/country_coords.json', 'r') as f:
            self.geo_data = json.load(f)

    def create_countries(self) -> dict:
        countries = {}
        for name, coords in self.geo_data.items():  # coords = [[lon, lat], ...]
            xy_coords = []
            for coord in coords:
                x = (self.MAP_WIDTH / 360) * (180 + coord[0])
                y = (self.MAP_HEIGHT / 180) * (90 - coord[1])
                xy_coords.append(pg.Vector2(x, y))
            countries[name] = Country(name, xy_coords)
        return countries

    def draw(self, screen:pg.Surface):
        for country in self.countries.values():
            country.draw(screen, self.scroll)
        if self.hovered_country is not None:
            self.draw_hovered_country(screen)



    def update(self):
        self.update_camera()
        mouse_pos = pg.mouse.get_pos()
        self.hovered_country = None
        for country in self.countries.values():
            country.update(pg.Vector2(mouse_pos[0] + self.scroll.x, mouse_pos[1] + self.scroll.y))
            if country.hovered:
                self.hovered_country = country

    def update_camera(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_q]:
            self.scroll.x -= 10
        elif keys[pg.K_d]:
            self.scroll.x += 10

        if keys[pg.K_z]:
            self.scroll.y -= 10
        elif keys[pg.K_s]:
            self.scroll.y += 10

        if keys[pg.K_SPACE]:
            self.scroll = pg.Vector2(3650, 395)

    def draw_hovered_country(self, screen: pg.Surface):
        screen.blit(self.hover_surface, (pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]))

        if self.hovered_country.discovered:
            text = self.hovered_country
        else:
            text = '????'


        draw_text(
            screen,
            text,
            (255,255,255),
            pg.mouse.get_pos()[0]+150,
            pg.mouse.get_pos()[1]+50,
            True,
            24)




