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
carroo = Jogador("imagem\carroo.png",100,100,360,500)
jujuba4 = Jogador("imagem\jujuba1.png", 100, 100, 0,0)


estrada = py.image.load("imagem\estrada.png")
estrada = py.transform.scale(estrada,(1280,720))

obstaculo1 = Obstaculo("imagem\carro1.png",130, 100)
obstaculo2 = Obstaculo("imagem/carro-2.png", 130, 100)

#loop infinito 
fimjogo  = False
while not fimjogo:
    #ttratar de eventos
    for eventos in py.event.get():    
        if eventos.type == py.QUIT:
            fimjogo = True

        
    #desenhar os objetos
    tela.blit (estrada,(0,0))

    obstaculo1.movimentar()
    tela.blit(obstaculo1.imagem,(obstaculo1.posicao_x, obstaculo1.posicao_y))

    obstaculo2.movimentar()
    tela.blit(obstaculo2.imagem,(obstaculo2.posicao_x,obstaculo2.posicao_y))
    
    tela.blit(carroo.imagem, (carroo.posicao_x, carroo.posicao_y))
    tela.blit(jujuba4.imagem, (jujuba4.posicao_x, jujuba4.posicao_y))


    #desenhar outros objetos TESTE

    teclas = py.key.get_pressed()

    carroo.movimentar(py.K_w, 
                      py.K_s, 
                      py.K_d, 
                      py.K_a)
    
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

