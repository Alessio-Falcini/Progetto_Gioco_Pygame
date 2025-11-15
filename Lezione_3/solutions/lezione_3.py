# Autori: Alessio Falcini, Leonardo Occhirossi, Vittorio Cambiotti
# Lezione 3: Aggiunta della meccanica di sparo 
import pygame 
import random  
import math   
pygame.init()

LARGHEZZA_SCHERMO = 800  
ALTEZZA_SCHERMO = 600    

schermo = pygame.display.set_mode((LARGHEZZA_SCHERMO, ALTEZZA_SCHERMO))
pygame.display.set_caption("Progetto: Alessio Falcini, Leonardo Occhirossi e Vittorio Cambiotti - Lezione 3 (Ristrutturata)")

BIANCO = (255, 255, 255) 
NERO = (0, 0, 0)        
GIALLO = (255, 255, 0)   

LARGHEZZA_PERSONAGGIO = 40
ALTEZZA_PERSONAGGIO = 80
velocita_personaggio = 5

posizione_x = (LARGHEZZA_SCHERMO - LARGHEZZA_PERSONAGGIO) // 2
posizione_y = (ALTEZZA_SCHERMO - ALTEZZA_PERSONAGGIO) // 2

personaggio = pygame.Rect(posizione_x, posizione_y, LARGHEZZA_PERSONAGGIO, ALTEZZA_PERSONAGGIO)

lista_proiettili = [] 
DIMENSIONE_PROIETTILE = 10
VELOCITA_PROIETTILE = 10

orologio = pygame.time.Clock()


def spara_proiettile(lista_proiettili, personaggio_rect, dimensione_proiettile):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    direzione_x = mouse_x - personaggio_rect.centerx
    direzione_y = mouse_y - personaggio_rect.centery
    distanza = (direzione_x**2 + direzione_y**2)**0.5
    if distanza != 0:
        direzione_x /= distanza
        direzione_y /= distanza
        proiettile = pygame.Rect(
            personaggio_rect.centerx - dimensione_proiettile // 2,
            personaggio_rect.centery - dimensione_proiettile // 2,
            dimensione_proiettile,
            dimensione_proiettile
        )
        lista_proiettili.append({
            'rect': proiettile,
            'dx': direzione_x,
            'dy': direzione_y
        })
        
def muovi_proiettili(lista_proiettili, velocita_proiettile, larghezza_schermo, altezza_schermo):
    proiettili_da_mantenere = []
    for proiettile in lista_proiettili:
        proiettile['rect'].x += proiettile['dx'] * velocita_proiettile
        proiettile['rect'].y += proiettile['dy'] * velocita_proiettile
        if (0 < proiettile['rect'].centerx < larghezza_schermo and
            0 < proiettile['rect'].centery < altezza_schermo):
            proiettili_da_mantenere.append(proiettile)
    return proiettili_da_mantenere

gioco_attivo = True
while gioco_attivo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco_attivo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # 1 = tasto sinistro
                spara_proiettile(lista_proiettili, personaggio, DIMENSIONE_PROIETTILE)
               
    tasti = pygame.key.get_pressed()
    if tasti[pygame.K_w]:
        personaggio.y -= velocita_personaggio
    if tasti[pygame.K_s]:
        personaggio.y += velocita_personaggio
    if tasti[pygame.K_a]:
        personaggio.x -= velocita_personaggio
    if tasti[pygame.K_d]:
        personaggio.x += velocita_personaggio
    personaggio.x = max(0, min(personaggio.x, LARGHEZZA_SCHERMO - LARGHEZZA_PERSONAGGIO))
    personaggio.y = max(0, min(personaggio.y, ALTEZZA_SCHERMO - ALTEZZA_PERSONAGGIO))
   
    lista_proiettili = muovi_proiettili(
        lista_proiettili, 
        VELOCITA_PROIETTILE, 
        LARGHEZZA_SCHERMO, 
        ALTEZZA_SCHERMO
    )
   
    schermo.fill(NERO)  # Sfondo
    pygame.draw.rect(schermo, BIANCO, personaggio)
    for proiettile in lista_proiettili:
        pygame.draw.circle(schermo, GIALLO, proiettile['rect'].center, DIMENSIONE_PROIETTILE // 2)
    pygame.display.flip()
    orologio.tick(60)
pygame.quit()
