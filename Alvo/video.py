import pygame
import random
import sys

from Alvo import Alvo
# from Mira import Mira

# tamanho da tela
LARGURA = 1280
ALTURA = 720

# ARQUIVOS
BG = 'Alvo/assets/img/bg.png'
ALVO = 'Alvo/assets/img/target.png'
MIRA = 'Alvo/assets/img/mouse.png'
DISPARO = 'Alvo/assets/audio/disparo.mp3'
FONTE = 'Alvo/assets/font/PixelGameFont.ttf'

# PONTUAÇÃO
PONTOS = 0
RECORDE = 0

# TIMER
TIMER = 600 # 1800/60 = 30 SEGUNDOS

# PAUSE E FECHAR
GAME_PAUSED = False
FINALIZAR = False

# objeto mira
class Mira(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(MIRA).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound(DISPARO)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def shoot(self):
        global PONTOS
        self.sound.play()

        colisions = pygame.sprite.spritecollide(mira, grupo_alvo, False)
        for colision in colisions:
            PONTOS += 1
            colision.kill()
            alvo = Alvo(random.randrange(0,LARGURA),random.randrange(0,ALTURA)) #só pode desenhar em grupos (conjunto)
            grupo_alvo.add(alvo)

pygame.init()

screen = pygame.display.set_mode((LARGURA, ALTURA))

# background
bg = pygame.image.load(BG).convert()
bg = pygame.transform.scale(bg, (LARGURA, ALTURA))

clock = pygame.time.Clock()

font = pygame.font.Font(FONTE, 30)

pygame.display.set_caption('Tiro ao Alvo')

grupo_alvo = pygame.sprite.Group()
for i in range(20):
    alvo = Alvo(random.randrange(0, LARGURA), random.randrange(0, ALTURA))
    grupo_alvo.add(alvo)

mira = Mira()
mira_grupo = pygame.sprite.Group()
mira_grupo.add(mira)

while not FINALIZAR:
    if not GAME_PAUSED:
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type== pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # esc
                    GAME_PAUSED = not GAME_PAUSED

            if event.type == pygame.MOUSEBUTTONDOWN:
                mira.shoot()

        screen.blit(bg, (0, 0))
        grupo_alvo.draw(screen)

        mira_grupo.draw(screen)
        mira_grupo.update()

        score = font.render(f'Pontos: {int(PONTOS)}', True, (0, 0, 0))
        screen.blit(score, (50, 50))

        tempo = font.render(f'Tempo: {TIMER/60:.1f} s', True, (0, 0, 0))
        screen.blit(tempo, (50, 100))

        TIMER -= 1

        if TIMER < 0:
            TIMER = 600

            if PONTOS > RECORDE:
                RECORDE = PONTOS
                PONTOS = 0
            GAME_PAUSED = not GAME_PAUSED

    else:
        screen.fill((252, 132, 3))
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    GAME_PAUSED = not GAME_PAUSED
                
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pause = font.render(f"PRESSIONE ESC PARA INICIAR    ", True, (255, 255, 255))
        points = font.render(f"RECORDE: {RECORDE} ", True, (255, 255, 255))

        pause_rect = pause.get_rect(center = (LARGURA/2, ALTURA/2))
        points_rect = points.get_rect(center = (LARGURA/2, ALTURA/2-50))

        screen.blit(pause, pause_rect)
        screen.blit(points, points_rect)

    pygame.display.flip()
    clock.tick(60)

