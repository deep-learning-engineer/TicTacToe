import pygame as pg


class ToeTile:
    def __init__(self, coord: tuple, tile_type: int = -1):
        self.rect = pg.Rect(*coord)
        self.tile_type = tile_type

    def draw(self, surface: pg.Surface):
        pg.draw.rect(surface, rect=self.rect, width=5, color="black")
        if self.tile_type == 0:
            pg.draw.circle(surface, color="black", center=self.rect.center, radius=100, width=5)
        if self.tile_type == 1:
            pg.draw.line(surface, color="black", start_pos=(self.rect.x+50, self.rect.y+50),
                         end_pos=(self.rect.x+self.rect.w-50, self.rect.y+self.rect.h-50), width=5)
            pg.draw.line(surface, color="black", start_pos=(self.rect.x+self.rect.w - 50, self.rect.y + 50),
                         end_pos=(self.rect.x + 50, self.rect.y + self.rect.h - 50), width=5)
