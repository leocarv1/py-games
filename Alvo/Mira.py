# import pygame
# from Alvo import Alvo

# MIRA = 'Alvo/assets/img/mouse.png'
# DISPARO = 'Alvo/assets/audio/disparo.mp3'

# class Mira(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load(MIRA).convert_alpha()
#         self.image = pygame.transform.scale(self.image, (50, 50))
#         self.rect = self.image.get_rect()
#         self.sound = pygame.mixer.Sound(DISPARO)

#     def update(self):
#         self.rect.center = pygame.mouse.get_pos()

#     def shoot(self):
#         global PONTOS
#         self.sound.play()

#         colisions = pygame.sprite.spritecollide(mira, grupo_de_alvos, False)
#         for colision in colisions:
#             PONTOS += 1
#             colision.kill()
#             alvo = Alvo(random.randrange(0,LARGURA),random.randrange(0,ALTURA)) #só pode desenhar em grupos (conjunto)
#             grupo_de_alvos.add(alvo)