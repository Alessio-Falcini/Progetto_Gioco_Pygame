# Lezione 3: Meccanica di sparo 
import pygame
import math
# --- Inizializzazione ---
pygame.init()
# --- Costanti e finestra ---
LARGHEZZA_SCHERMO = 800
ALTEZZA_SCHERMO = 600
schermo = pygame.display.set_mode((LARGHEZZA_SCHERMO, ALTEZZA_SCHERMO))
pygame.display.set_caption("Progetto: Alessio Falcini, Leonardo Occhirossi e Vittorio Cambiotti - Lezione 3")
BIANCO = (255, 255, 255)
NERO = (0, 0, 0)
GIALLO = (255, 255, 0)
# --- Personaggio ---
LARGHEZZA_PERSONAGGIO = 40
ALTEZZA_PERSONAGGIO = 80
velocita_personaggio = 5
posizione_x = (LARGHEZZA_SCHERMO - LARGHEZZA_PERSONAGGIO) // 2
posizione_y = (ALTEZZA_SCHERMO - ALTEZZA_PERSONAGGIO) // 2
personaggio = pygame.Rect(posizione_x, posizione_y, LARGHEZZA_PERSONAGGIO, ALTEZZA_PERSONAGGIO)
# --- Funzione movimento personaggio ---
def muovi_personaggio(personaggio, velocita):
   tasti = pygame.key.get_pressed()
   if tasti[pygame.K_w]: personaggio.y -= velocita
   if tasti[pygame.K_s]: personaggio.y += velocita
   if tasti[pygame.K_a]: personaggio.x -= velocita
   if tasti[pygame.K_d]: personaggio.x += velocita
   # Limiti finestra
   personaggio.x = max(0, min(personaggio.x, LARGHEZZA_SCHERMO - LARGHEZZA_PERSONAGGIO))
   personaggio.y = max(0, min(personaggio.y, ALTEZZA_SCHERMO - ALTEZZA_PERSONAGGIO))
# --- Proiettili ---
lista_proiettili = []  
DIMENSIONE_PROIETTILE = 10
VELOCITA_PROIETTILE = 10
# TODO: Scrivere funzione spara(mouse_pos, personaggio) per creare proiettili
# TODO: Scrivere funzione muovi_proiettili(proiettili) per aggiornare posizione e rimuovere proiettili fuori schermo
# TODO: Disegnare i proiettili nel ciclo principale
# --- Orologio ---
orologio = pygame.time.Clock()
# --- Ciclo principale ---
gioco_attivo = True
while gioco_attivo:
   for evento in pygame.event.get():
       if evento.type == pygame.QUIT:
           gioco_attivo = False
       # TODO: se click sinistro del mouse, chiamare spara(evento.pos, personaggio)
   # --- Movimento personaggio ---
   muovi_personaggio(personaggio, velocita_personaggio)
   # TODO: aggiornare la posizione dei proiettili
   # --- Disegno ---
   schermo.fill(NERO)
   pygame.draw.rect(schermo, BIANCO, personaggio)
   # TODO: disegnare i proiettili
   pygame.display.flip()
   orologio.tick(60)
pygame.quit()
