# lezione_3.py
# Autori: Alessio Falcini, Leonardo Occhirossi, Vittorio Cambiotti
# Lezione 3: Aggiunta della meccanica di sparo
import pygame  # Libreria per creare videogiochi
import random  # Libreria per generare numeri casuali
# Avviamo Pygame - questo è necessario per iniziare a usare Pygame
pygame.init()
# Definiamo le dimensioni della finestra di gioco
LARGHEZZA_SCHERMO = 800  # Larghezza in pixel
ALTEZZA_SCHERMO = 600   # Altezza in pixel
# Creiamo la finestra di gioco
schermo = pygame.display.set_mode((LARGHEZZA_SCHERMO, ALTEZZA_SCHERMO))
pygame.display.set_caption("Progetto: Alessio Falcini, Leonardo Occhirossi e Vittorio Cambiotti - Lezione 3")
# Definiamo i colori che useremo nel gioco (in RGB: Rosso, Verde, Blu)
BIANCO = (255, 255, 255)   # Colore del nostro personaggio
NERO = (0, 0, 0)           # Colore dello sfondo
GIALLO = (255, 255, 0)     # Colore dei proiettili
# Dimensioni del nostro personaggio
LARGHEZZA_PERSONAGGIO = 40
ALTEZZA_PERSONAGGIO = 80
velocita_personaggio = 5
# Posizioniamo il personaggio al centro dello schermo
posizione_x = (LARGHEZZA_SCHERMO - LARGHEZZA_PERSONAGGIO) // 2
posizione_y = (ALTEZZA_SCHERMO - ALTEZZA_PERSONAGGIO) // 2
# Creiamo il rettangolo del personaggio
personaggio = pygame.Rect(posizione_x, posizione_y, LARGHEZZA_PERSONAGGIO, ALTEZZA_PERSONAGGIO)
# Lista per i proiettili
lista_proiettili = []
DIMENSIONE_PROIETTILE = 10
VELOCITA_PROIETTILE = 10
# Creiamo un orologio per controllare la velocità del gioco
orologio = pygame.time.Clock()
# Ciclo principale del gioco
gioco_attivo = True
while gioco_attivo:
   # Controlliamo gli eventi
   for evento in pygame.event.get():
       if evento.type == pygame.QUIT:
           gioco_attivo = False
       # Se il giocatore clicca con il tasto sinistro del mouse, spara
       elif evento.type == pygame.MOUSEBUTTONDOWN:
           if evento.button == 1:  # 1 = tasto sinistro
               mouse_x, mouse_y = pygame.mouse.get_pos()
               # Calcoliamo la direzione del proiettile
               direzione_x = mouse_x - personaggio.centerx
               direzione_y = mouse_y - personaggio.centery
               # Normalizziamo la direzione
               distanza = (direzione_x**2 + direzione_y**2)**0.5
               if distanza != 0:
                   direzione_x /= distanza
                   direzione_y /= distanza
               # Creiamo il proiettile
               proiettile = pygame.Rect(
                   personaggio.centerx - DIMENSIONE_PROIETTILE // 2,
                   personaggio.centery - DIMENSIONE_PROIETTILE // 2,
                   DIMENSIONE_PROIETTILE,
                   DIMENSIONE_PROIETTILE
               )
               lista_proiettili.append({
                   'rect': proiettile,
                   'dx': direzione_x,
                   'dy': direzione_y
               })
   # Movimento del personaggio con i tasti W, A, S, D
   tasti = pygame.key.get_pressed()
   if tasti[pygame.K_w]:
       personaggio.y -= velocita_personaggio
   if tasti[pygame.K_s]:
       personaggio.y += velocita_personaggio
   if tasti[pygame.K_a]:
       personaggio.x -= velocita_personaggio
   if tasti[pygame.K_d]:
       personaggio.x += velocita_personaggio
   # Impedisce al personaggio di uscire dallo schermo
   personaggio.x = max(0, min(personaggio.x, LARGHEZZA_SCHERMO - LARGHEZZA_PERSONAGGIO))
   personaggio.y = max(0, min(personaggio.y, ALTEZZA_SCHERMO - ALTEZZA_PERSONAGGIO))
   # Muoviamo i proiettili
   for proiettile in lista_proiettili[:]:
       proiettile['rect'].x += proiettile['dx'] * VELOCITA_PROIETTILE
       proiettile['rect'].y += proiettile['dy'] * VELOCITA_PROIETTILE
       # Rimuoviamo i proiettili usciti dallo schermo
       if (proiettile['rect'].x < 0 or proiettile['rect'].x > LARGHEZZA_SCHERMO or
           proiettile['rect'].y < 0 or proiettile['rect'].y > ALTEZZA_SCHERMO):
           lista_proiettili.remove(proiettile)
   # Disegniamo tutti gli elementi
   schermo.fill(NERO)
   pygame.draw.rect(schermo, BIANCO, personaggio)
   # Disegniamo i proiettili (cerchi gialli)
   for proiettile in lista_proiettili:
       pygame.draw.circle(schermo, GIALLO, proiettile['rect'].center, DIMENSIONE_PROIETTILE // 2)
   pygame.display.flip()
   orologio.tick(60)
pygame.quit()
