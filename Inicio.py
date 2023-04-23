import pygame
from Cobra import Cobra
cobra = Cobra()

pygame.init()

# Definindo as dimensões da tela
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Definindo as coordenadas do botão "play"
button_x = 240
button_y = 200
button_width = 160
button_height = 80

# Definindo as cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Verifica se o botão foi clicado
            mouse_pos = pygame.mouse.get_pos()
            if button_x < mouse_pos[0] < button_x + button_width and button_y < mouse_pos[1] < button_y + button_height:
                # Inicia o jogo
                print("Jogo iniciado!")
                cobra.start()
                running = False
                
    # Desenha o botão "play"
    pygame.draw.rect(screen, red, (button_x, button_y, button_width, button_height))
    pygame.draw.rect(screen, white, (button_x+5, button_y+5, button_width-10, button_height-10))
    font = pygame.font.Font(None, 36)
    text = font.render("Play", True, black)
    text_rect = text.get_rect(center=(button_x + button_width//2, button_y + button_height//2))
    screen.blit(text, text_rect)
    
    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
