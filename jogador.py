import pygame as py

class Jogador:
    
    def __init__(self,figura,largura,altura, posicaoXinicial, posicaoYinicial):
        self.imagem = py.image.load(figura)
        self.imagem = py.transform.scale(self.imagem,(largura, altura))

        self.posicao_x = posicaoXinicial
        self.posicao_y =  posicaoYinicial
    
    def movimentar(self, cima, baixo, direita, esquerda):

        teclas = py.key.get_pressed()

        if teclas[direita]:
            self.posicao_x += 10 

        if teclas[esquerda]:
            self.posicao_x -= 10 
    
        if teclas[cima]:
            self.posicao_y -= 10 

        if teclas[baixo]:
            self.posicao_y += 10

        

    