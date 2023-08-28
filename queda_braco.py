# https://www.pygame.org/docs/tut/newbieguide.html

import pygame
import sys
import os

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

# posições iniciais da bola
x = 320
y = 320
x2 = 640
y2 = 320
k1 = 0
k2 = 0
k3 = 1
score = 0
score_increment = 1
score2 = 0
while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                score2 += score_increment
                k2 += 15
            if event.key == pygame.K_w:
                score += score_increment
                k1 += 15

    # captura de eventos do teclado
    # https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame
    # Do logical updates here.
    # ...

    screen.fill("purple")  # Fill the display with a solid color

    pygame.draw.circle(screen, (10, 10, 10), [x, y], 15, 5)
    pygame.draw.circle(screen, (10, 10, 10), [x2, y2], 15, 5)
    pygame.draw.rect(screen, (0, 0, 255), 
                 [250, 600, 350, 100], 2)
    pygame.draw.rect(screen, (250, 250, 0), 
                 [0.5, 718 - k1 + k3, 100,k1], 200)
    pygame.draw.rect(screen, (250, 0, 0), 
                 [1185, 718 - k2 + k3, 100,k2], 200)
    if k1 > 0:
        k1 = k1 - 1


    if k2 > 0:
        k2 = k2 - 1
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    core_text = font.render(f'Score: {score}', True, (0, 255, 0))
    
    score_text = font.render(f'Score: {score2}', True, (255, 255, 255))
    screen.blit(score_text, (1180, 10))
    core_text = font.render(f'Score: {score2}', True, (0, 255, 0))


    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPSww

