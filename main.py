import pygame

Inicjalizacja
pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zadanie 2 – litera Z")

Kolor
CZERWONY = (255, 0, 0)
TLO = (255, 255, 255)

Główna pętla
run = True
while run:
    win.fill(TLO)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    pygame.draw.line(win, CZERWONY, (200, 100), (400, 100), 10)     
    pygame.draw.line(win, CZERWONY, (400, 100), (200, 300), 10)     
    pygame.draw.line(win, CZERWONY, (200, 300), (400, 300), 10)     
    pygame.display.update()

pygame.quit()
