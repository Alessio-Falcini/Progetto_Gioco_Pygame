# Autori: Alessio Falcini, Leonardo Occhirossi, Vittorio Cambiotti
# Lezione 4: Creazione e movimento dei nemici
import pygame
import random
import math
# Inizializzazione di Pygame
pygame.init()
# Dimensioni della finestra
LARGHEZZA_SCHERMO = 800
ALTEZZA_SCHERMO = 600
# Creazione finestra di gioco
schermo = pygame.display.set_mode((LARGHEZZA_SCHERMO, ALTEZZA_SCHERMO))
pygame.display.set_caption("Lezione 4 — Spawn e movimento dei nemici")
# Colori
BIANCO = (255, 255, 255)
NERO = (0, 0, 0)
ROSSO = (255, 0, 0)
GIALLO = (255, 255, 0)
# Personaggio
LARGHEZZA_PERSONAGGIO = 40
ALTEZZA_PERSONAGGIO = 80
posizione_x = (LARGHEZZA_SCHERMO - LARGHEZZA_PERSONAGGIO) // 2
posizione_y = (ALTEZZA_SCHERMO - ALTEZZA_PERSONAGGIO) // 2
personaggio = pygame.Rect(posizione_x, posizione_y, LARGHEZZA_PERSONAGGIO, ALTEZZA_PERSONAGGIO)
velocita_personaggio = 5
# Proiettili (manteniamo dal codice precedente)
proiettili = []
velocita_proiettile = 10
# Nemici
nemici = []
velocita_nemico = 2
tempo_spawn = 2000  # ogni quanti millisecondi appare un nuovo nemico
ultimo_spawn = pygame.time.get_ticks()
# Orologio
orologio = pygame.time.Clock()
gioco_attivo = True
# Funzione per generare un nuovo nemico ai bordi dello schermo
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
   return pygame.Rect(x, y, 30, 30)
# Funzione per muovere un nemico verso il giocatore
def muovi_nemico(nemico, giocatore):
   dx = giocatore.centerx - nemico.centerx
   dy = giocatore.centery - nemico.centery
   distanza = math.hypot(dx, dy)
   if distanza != 0:
       dx, dy = dx / distanza, dy / distanza
       nemico.x += dx * velocita_nemico
       nemico.y += dy * velocita_nemico
# Ciclo di gioco principale
while gioco_attivo:
   for evento in pygame.event.get():
       if evento.type == pygame.QUIT:
           gioco_attivo = False
       if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
           mouse_x, mouse_y = pygame.mouse.get_pos()
           dx = mouse_x - personaggio.centerx
           dy = mouse_y - personaggio.centery
           distanza = math.hypot(dx, dy)
           if distanza != 0:
               dx, dy = dx / distanza, dy / distanza
               proiettili.append([personaggio.centerx, personaggio.centery, dx, dy])
   # Movimento del personaggio
   tasti = pygame.key.get_pressed()
   if tasti[pygame.K_w]: personaggio.y -= velocita_personaggio
   if tasti[pygame.K_s]: personaggio.y += velocita_personaggio
   if tasti[pygame.K_a]: personaggio.x -= velocita_personaggio
   if tasti[pygame.K_d]: personaggio.x += velocita_personaggio
   # Limiti schermo
   personaggio.x = max(0, min(personaggio.x, LARGHEZZA_SCHERMO - LARGHEZZA_PERSONAGGIO))
   personaggio.y = max(0, min(personaggio.y, ALTEZZA_SCHERMO - ALTEZZA_PERSONAGGIO))
   # Spawn dei nemici ogni X millisecondi
   tempo_corrente = pygame.time.get_ticks()
   if tempo_corrente - ultimo_spawn > tempo_spawn:
       nemici.append(genera_nemico())
       ultimo_spawn = tempo_corrente
   # Movimento nemici verso il giocatore
   for nemico in nemici:
       muovi_nemico(nemico, personaggio)
   # Movimento proiettili
   nuovi_proiettili = []
   for proiettile in proiettili:
       proiettile[0] += proiettile[2] * velocita_proiettile
       proiettile[1] += proiettile[3] * velocita_proiettile
       if 0 < proiettile[0] < LARGHEZZA_SCHERMO and 0 < proiettile[1] < ALTEZZA_SCHERMO:
           nuovi_proiettili.append(proiettile)
   proiettili = nuovi_proiettili
   # Disegno
   schermo.fill(NERO)
   pygame.draw.rect(schermo, BIANCO, personaggio)
   for p in proiettili:
       pygame.draw.circle(schermo, GIALLO, (int(p[0]), int(p[1])), 5)
   for nemico in nemici:
       pygame.draw.rect(schermo, ROSSO, nemico)
   pygame.display.flip()
   orologio.tick(60)
pygame.quit()
