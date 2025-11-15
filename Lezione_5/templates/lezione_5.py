# Lezione 5: Collisioni proiettili-nemici
import pygame
import math
import random

# --- Inizializzazione ---
pygame.init()

# --- Costanti e finestra ---
LARGHEZZA_SCHERMO = 800
ALTEZZA_SCHERMO = 600
schermo = pygame.display.set_mode((LARGHEZZA_SCHERMO, ALTEZZA_SCHERMO))
pygame.display.set_caption("Lezione 5 — Collisioni proiettili-nemici")

BIANCO = (255, 255, 255)
NERO = (0, 0, 0)
ROSSO = (255, 0, 0)
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
   personaggio.x = max(0, min(personaggio.x, LARGHEZZA_SCHERMO - LARGHEZZA_PERSONAGGIO))
   personaggio.y = max(0, min(personaggio.y, ALTEZZA_SCHERMO - ALTEZZA_PERSONAGGIO))

# --- Proiettili ---
lista_proiettili = []  
DIMENSIONE_PROIETTILE = 10
VELOCITA_PROIETTILE = 10

def spara(mouse_pos, personaggio):
   mouse_x, mouse_y = mouse_pos
   dx = mouse_x - personaggio.centerx
   dy = mouse_y - personaggio.centery
   distanza = math.hypot(dx, dy)
   if distanza != 0:
       dx /= distanza
       dy /= distanza
   proiettile = [personaggio.centerx, personaggio.centery, dx, dy]
   lista_proiettili.append(proiettile)

def muovi_proiettili(proiettili):
   nuovi_proiettili = []
   for p in proiettili:
       p[0] += p[2] * VELOCITA_PROIETTILE
       p[1] += p[3] * VELOCITA_PROIETTILE
       if 0 < p[0] < LARGHEZZA_SCHERMO and 0 < p[1] < ALTEZZA_SCHERMO:
           nuovi_proiettili.append(p)
   return nuovi_proiettili

# --- Nemici ---
lista_nemici = []  
DIMENSIONE_NEMICO = 30
velocita_nemico = 2
tempo_spawn = 2000
ultimo_spawn = pygame.time.get_ticks()

def genera_nemico():
   lato = random.choice(['sinistra', 'destra', 'alto', 'basso'])
   if lato == 'sinistra':
       x = 0
       y = random.randint(0, ALTEZZA_SCHERMO)
   elif lato == 'destra':
       x = LARGHEZZA_SCHERMO
       y = random.randint(0, ALTEZZA_SCHERMO)
   elif lato == 'alto':
       x = random.randint(0, LARGHEZZA_SCHERMO)
       y = 0
   else:
       x = random.randint(0, LARGHEZZA_SCHERMO)
       y = ALTEZZA_SCHERMO
   return pygame.Rect(x, y, DIMENSIONE_NEMICO, DIMENSIONE_NEMICO)

def muovi_nemico(nemico, giocatore):
   dx = giocatore.centerx - nemico.centerx
   dy = giocatore.centery - nemico.centery
   distanza = math.hypot(dx, dy)
   if distanza != 0:
       dx, dy = dx / distanza, dy / distanza
       nemico.x += dx * velocita_nemico
       nemico.y += dy * velocita_nemico

# TODO: Scrivere funzione che controlla le collisioni fra proiettili e nemici

# --- Orologio ---
orologio = pygame.time.Clock()

# --- Ciclo principale ---
gioco_attivo = True
while gioco_attivo:
   for evento in pygame.event.get():
       if evento.type == pygame.QUIT:
           gioco_attivo = False
       elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
           spara(evento.pos, personaggio)

   # --- Movimento personaggio ---
   muovi_personaggio(personaggio, velocita_personaggio)

   # --- Spawn nemici e movimento nemici ---
   tempo_corrente = pygame.time.get_ticks()
   if tempo_corrente - ultimo_spawn > tempo_spawn:
       lista_nemici.append(genera_nemico())
       ultimo_spawn = tempo_corrente
   
   for nemico in lista_nemici:
       muovi_nemico(nemico, personaggio)

   # --- Movimento proiettili ---
   lista_proiettili = muovi_proiettili(lista_proiettili)
   # --- Disegno ---
   schermo.fill(NERO)
   pygame.draw.rect(schermo, BIANCO, personaggio)
   
   for p in lista_proiettili:
       pygame.draw.circle(schermo, GIALLO, (int(p[0]), int(p[1])), DIMENSIONE_PROIETTILE // 2)
   
   for nemico in lista_nemici:
       pygame.draw.rect(schermo, ROSSO, nemico)

   pygame.display.flip()
   orologio.tick(60)

pygame.quit()
