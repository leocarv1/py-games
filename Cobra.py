import pygame, sys
from pygame.locals import * 
from random import randint

class Cobra: 

    # Cores
    COR_FUNDO = (255, 255, 255)
    COR_DESTAQUE = (245, 27, 230)
    COR_TEXTO = (63, 8, 59)
    COR_COMIDA = (255, 0, 0)
    COR_CABECA = (175, 11, 193)
    COR_CORPO = (255, 0, 255)

    # Bloco
    BLOCO = [18, 18]

    # direções
    DIREITA = 6
    ESQUERDA = 4
    CIMA = 8
    BAIXO = 2

    #controlar o jogo
    morto = False
    pontos = 0
    direcao = None
    relogio = None

    # tela
    COMPRIMENTO_JANELA = 440
    ALTURA_JANELA = 510
    TELA = None

    # Cobra
    COBRA = [[30, 120], [10, 120]]
    CABECA = [30, 120]
    TEM_COMIDA = False
    COMIDA_POS = None

    def start(self):
        # inicia o jogo com a cobra indo para a direita e sem pontos
        self.direcao = self.DIREITA
        self.morto = False
        self.pontos = 0

        pygame.init()
        self.relogio = pygame.time.Clock()

        self.jogar()

    # Cria a tela do jogo
    def contruirJogo(self):
        self.TELA = pygame.display.set_mode((self.COMPRIMENTO_JANELA, self.ALTURA_JANELA), 0, 32)
        pygame.display.set_caption('Cobra Xtreme')

    def jogar(self):
        self.contruirJogo()

        self.adicionarComida()

        while not self.morto:
            
            for evento in pygame.event.get():

                if evento.type == QUIT:
                    pygame.quit() # fecha a janela do jogo
                    sys.exit() # fecha o terminal | para a execução do programa

                if evento.type == KEYDOWN:
                    if evento.key == K_LEFT or evento.key == ord('o'):
                        self.direcao = self.ESQUERDA
                    elif evento.key == K_RIGHT or evento.key == ord('p'):
                        self.direcao = self.DIREITA
                    elif evento.key == K_UP or evento.key == ord('k'):
                        self.direcao = self.CIMA
                    elif evento.key == K_DOWN or evento.key == ord('m'):
                        self.direcao = self.BAIXO   

            self.calculaDirecaoCabeca()    

            if not self.TEM_COMIDA:
                self.adicionarComida()

            # Adiciona a cabeça da cobra na lista do corpo da cobra
            self.COBRA.insert(0, list(self.CABECA))

            #verifica se a cobra comeu a comida
            if self.CABECA[0] == self.COMIDA_POS[0] and self.CABECA[1] == self.COMIDA_POS[1]:
                self.TEM_COMIDA = False
                self.pontos += 1
            else:
                self.COBRA.pop()

            self.desenharJogo()

    def adicionarComida(self):
        while True: 
            x1 = randint(0, 20)
            y1 = randint(0, 17)

            self.COMIDA_POS = [int(x1 * 20) + 10, int(y1 * 20) + 120]

            # verifica se a comida não está na cobra
            if self.COBRA.count(self.COMIDA_POS) == 0:
                self.TEM_COMIDA = True
                break


    def calculaDirecaoCabeca(self):
        match self.direcao:
            case self.DIREITA:
                self.CABECA[0] += 20

                # verifica se a cobra bateu na parede
                if self.CABECA[0] >= self.COMPRIMENTO_JANELA - 20:
                    self.morto = True
                    self.gameOver()

            case self.ESQUERDA:
                self.CABECA[0] -= 20

                if self.CABECA[0] < 10:
                    self.morto = True
                    self.gameOver()

            case self.CIMA:
                self.CABECA[1] -= 20

                if self.CABECA[1] < 110:
                    self.morto = True
                    self.gameOver()

            case self.BAIXO:     
                self.CABECA[1] += 20

                if self.CABECA[1] >= self.ALTURA_JANELA - 30:
                    self.morto = True     
                    self.gameOver()  

        # verifica se a cobra bateu nela mesma
        if self.COBRA.count(self.CABECA) > 0:
            self.morto = True 
            self.gameOver()

    def desenharJogo(self):
        self.TELA.fill(self.COR_FUNDO)

        # desenha o placar de pontuação
        pygame.draw.rect(self.TELA, self.COR_DESTAQUE, Rect([10, 10], [420, 100]), 1)

        # escreve o texto do placar
        font = pygame.font.Font(None, 40)
        placar = font.render("Pontos: " + str(self.pontos), 1, self.COR_TEXTO)

        # posição do placar
        posicaoPlacar = placar.get_rect()
        posicaoPlacar.left = 75
        posicaoPlacar.top = 45

        self.TELA.blit(placar, posicaoPlacar)

        # desenha a área do jogo
        pygame.draw.rect(self.TELA, self.COR_DESTAQUE, Rect([10, 120], [420, 380]), 1)

        # desenha a comida
        pygame.draw.rect(self.TELA, self.COR_COMIDA, Rect(self.COMIDA_POS, self.BLOCO))

        #desenha a cobra
        for quadrado in self.COBRA: 
            if quadrado == self.COBRA[0]:
                pygame.draw.rect(self.TELA, self.COR_CABECA, Rect(quadrado, self.BLOCO))
            else: 
                pygame.draw.rect(self.TELA, self.COR_CORPO, Rect(quadrado, self.BLOCO))

        pygame.display.update()
        self.relogio.tick(9)

    def gameOver(self):
        # desenha o Game Over
        pygame.draw.rect(self.TELA, self.COR_DESTAQUE, Rect([30, 100], [400, 300]), 1)
        # escreve o texto
        font = pygame.font.Font(None, 40)
        placar = font.render("Game Over: " + str(self.pontos), 1, self.COR_TEXTO)