import pygame as py

class Jogador:
    def __init__(self,figura,largura,altura,x_inicial,y_inicial):
        self.imagem = py.image.load(figura)
        self.imagem = py.transform.scale(self.imagem,(largura,altura))

        self.pos_x = x_inicial
        self.pos_y = y_inicial

    def andar(self):
        