import pygame as py
from jogador import Jogador

print("""          
                      
            
███████╗██████╗ ███████╗███████╗██╗    ██╗ █████╗ ██╗   ██╗
██╔════╝██╔══██╗██╔════╝██╔════╝██║    ██║██╔══██╗╚██╗ ██╔╝
█████╗  ██████╔╝█████╗  █████╗  ██║ █╗ ██║███████║ ╚████╔╝ 
██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ██║███╗██║██╔══██║  ╚██╔╝  
██║     ██║  ██║███████╗███████╗╚███╔███╔╝██║  ██║   ██║   
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   
                                                           

""")





#INICIALIZAR AS CONFIGURAÇOES PADRAO
py.init()
clock = py.time.Clock()

CORES = {"branco":(255,255,255),
         "amarelo":(255,255,0),
         "rosa":(255,200,255),
         "cinza":(100,100,100),
         "verde":(0,255,0)}

#CRIAR A TELA
py.display.set_mode((1280,720))
tela = py.display.set_mode((1280,720))
tela.fill(CORES["rosa"])

#CRIAR OS OBJETOS
estrada = py.image.load("imagem/estrada.png")
estrada = py.transform.scale(estrada,( 1280, 720))

#jujuba

carroo = Jogador("imagem/carroo.png",100,80,590,620)
carroo = py.image.load("imagem/carroo.png")
carroo = py.transform.scale(carroo,(100,80))
carroo_x = 590
carroo_y = 620

#LOOP INFINITO para manter o jogo rodando
fim_jogo = False
while not fim_jogo:
    #TRATAR DE EVENTOS
    for evento in py.event.get():
        if evento.type == py.QUIT:
            fim_jogo = True


    #DESENHAR OS OBJETOS
    tela.fill(CORES["rosa"])
    tela.blit(estrada, (0,0))
    tela.blit(carroo,(carroo_x,carroo_y))


    teclas = py.key.get_pressed()
    if teclas[py.K_RIGHT]:
        carroo_x -= 5
    if teclas[py.K_UP]:
        carroo_y -= 5
    if teclas[py.K_DOWN]:
        carroo_y += 5


    #LIMITAR MOVIMENTOS

    if (carroo_x <= 1280 and carroo_y >= 640): # BAIXO
        carroo_y -= 5

    if (carroo_y <= 0): # Cima
        carroo_y += 5

    if (carroo_y >= 0) and carroo_x <= 0: #esquerrda
        personagem_x += 5

    if (carroo_y <= 720) and carroo_x >= 1200: #esquerrda
        carroo_x -= 5
    
    #ATUALIZAR A PAGINA
    py.display.update()
    clock.tick(60)












































