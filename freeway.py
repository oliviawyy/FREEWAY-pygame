import pygame as py

#INICIALIZAR AS CONFIGURAÇOES PADRAO
py.init()

CORES = {"branco":(255,255,255),
         "amarelo":(255,255,0),
         "rosa":(255,200,255),
         "cinza":(100,100,100),
         "verde":(0,255,0)}

#CRIAR A TELA
py.display.set_mode((800,600))
tela = py.display.set_mode((800,600))
tela.fill(CORES["rosa"])

#CRIAR OS OBJETOS
carroo = py.image.load("imagem/carroo.png")
carroo = py.transform.scale(carroo,(100,80))
carroo_x = 0 

#LOOP INFINITO para manter o jogo rodando
fim_jogo = False
while not fim_jogo:
    #TRATAR DE EVENTOS
    for evento in py.event.get():
        if evento.type == py.QUIT:
            fim_jogo = True


    #DESENHAR OS OBJETOS
    tela.fill(CORES["rosa"])
    tela.blit(carroo,(carroo_x,260))
    carroo_x += 1

    #ATUALIZAR A PAGINA
    py.display.update()












































