import random
import pygame as py

class Obstaculo:

    def __init__(self, end_imagem, largura, altura):
        #guardando a largura e altura do obstaculo
        self.largura = largura
        self.altura = altura

        #carregando e alterando o tamanho da imagem
        self.imagem = py.image.load(end_imagem)
        self.imagem = py.transform.scale(self.imagem,(self.largura,self.altura))

        #guardando a posição inicial e final
        faixas = [100,200,300,400,500]
        self.x_inicial = 1280
        #self.y_inicial = 220
        self.posicao_x = self.x_inicial
        self.posicao_y = random.choice(self.faixas)

    #controlando a velocidade do obstaculo
        self.velocidade = random.randint(5,25)



    def movimentar(self):
        self.posicao_x -= self.velocidade
        if self.posicao_x < 0 - self.largura:
            self.posicao_x = self.x_inicial
            self.velociade = random.randint(5,25)
            self.posicao_y = random.choice(self.faixas)