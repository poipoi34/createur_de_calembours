import pygame

class Obj:
    def __init__(o,surf,pos = [0,0]):
        o.surf = surf
        o.pos = pos
        
    def get_image(o):
        return o.surf