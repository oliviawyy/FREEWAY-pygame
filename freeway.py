import pygame as py
from jogador import Jogador
from obstaculo import Obstaculo

print("""          
                      
            
███████╗██████╗ ███████╗███████╗██╗    ██╗ █████╗ ██╗   ██╗
██╔════╝██╔══██╗██╔════╝██╔════╝██║    ██║██╔══██╗╚██╗ ██╔╝
█████╗  ██████╔╝█████╗  █████╗  ██║ █╗ ██║███████║ ╚████╔╝ 
██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ██║███╗██║██╔══██║  ╚██╔╝  
██║     ██║  ██║███████╗███████╗╚███╔███╔╝██║  ██║   ██║   
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   
                                                           

""")


#inicializar as configurações padrão
py.init()
clock = py.time.Clock()

CORES = {"BRANCO":(255,255,255),
         "AMARELO":(255,255,0),
         "ROSA": (255,200,255),
         "CINZA":(100,100,100)}

#criar a tela

tela = py.display.set_mode((1280,720))
tela.fill(CORES["CINZA"])


# Criandoa aqui os personagens, definindo altura largura, e o local que eeles estaram
carroo = Jogador("imagem\carroo.png",100,100,420,610,"imagem/atropelo.mp3")
jujuba4 = Jogador("imagem\jujuba1.png", 100, 100, 500,610, "imagem/atropelo.mp3")


estrada = py.image.load("imagem\estrada.png")
estrada = py.transform.scale(estrada,(1280,720))


lista_obstaculo = [Obstaculo("imagem\carro1.png",130, 100),
                  Obstaculo("imagem/carro-2.png", 130, 100),
                  Obstaculo("imagem\carro-3.png", 140, 100)]

#loop infinito 
fimjogo  = False
while not fimjogo:
    #ttratar de eventos
    for eventos in py.event.get():    
        if eventos.type == py.QUIT:
            fimjogo = True

        
    #desenhar os objetos
    tela.blit (estrada,(0,0))

    for obstaculo in lista_obstaculo:
        obstaculo.movimentar()
        #jake
        tela.blit(obstaculo.imagem,(obstaculo.posicao_x, obstaculo.posicao_y))
        if carroo.mascara.overlap(obstaculo.mascara,(obstaculo.posicao_x-carroo.posicao_x,obstaculo.posicao_y-carroo.posicao_y)):
            carroo.posicao_x = carroo.x_inicial
            carroo.posicao_y = carroo.y_inicial
            carroo.som.play()
            carroo.pontos -= 1
            print(carroo.pontos)
            print("O CARRO TE ATROPELOU!")
        #finn
        if jujuba4.mascara.overlap(obstaculo.mascara,(obstaculo.posicao_x-jujuba4.posicao_x,obstaculo.posicao_y-jujuba4.posicao_y)):
            jujuba4.posicao_x = jujuba4.x_inicial
            jujuba4.posicao_y = jujuba4.y_inicial
            jujuba4.som.play()
            jujuba4.pontos -= 1
            print(jujuba4.pontos)

    tela.blit(carroo.imagem, (carroo.posicao_x, carroo.posicao_y))
    tela.blit(jujuba4.imagem, (jujuba4.posicao_x, jujuba4.posicao_y))

    
    #desenhar outros objetos TESTE

    teclas = py.key.get_pressed()

    carroo.movimentar(py.K_w, 
                      py.K_s, 
                      py.K_d, 
                      py.K_a)
    if carroo.posicao_y <= 10:
        carroo.pontos +=1
        carroo.posicao_x = carroo.x_inicial
        carroo.posicao_y = carroo.y_inicial
        print(carroo.pontos)


    jujuba4.movimentar(py.K_UP, py.K_DOWN, py.K_RIGHT, py.K_LEFT)


    #colisão da tela

    #PARAR NAS BARREIRAS
    if carroo.posicao_x <= 0:
        carroo.posicao_x = 0
    
    if carroo.posicao_y <= 0:
        carroo.posicao_y = 0

    if carroo.posicao_x >= 1280:
        carroo.posicao_x = 1280

    if carroo.posicao_y >= 720:
        carroo.posicao_y = 720

    #atualizar a pagina
    py.display.update()
    clock.tick(60)

