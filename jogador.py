import pygame as py

class Jogador:
    
    def __init__(self,figura,largura,altura, posicaoXinicial, posicaoYinicial, som_dor):
        self.imagem = py.image.load(figura)
        self.imagem = py.transform.scale(self.imagem,(largura, altura))
        self.mascara = py.mask.from_surface(self.imagem)

        self.x_inicial = posicaoXinicial
        self.y_inicial = posicaoYinicial    
        self.posicao_x = posicaoXinicial
        self.posicao_y =  posicaoYinicial

        self.som = py.mixer.Sound(som_dor)

        self.pontos = 0
    
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

        

    