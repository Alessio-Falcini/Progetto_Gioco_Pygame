# Lezione 2: Movimento del personaggio e limiti della finestra

import pygame  # Libreria per creare videogiochi

# --- Inizializzazione ---
pygame.init()

# --- Costanti ---
LARGHEZZA_SCHERMO = 800   # Larghezza in pixel
ALTEZZA_SCHERMO = 600     # Altezza in pixel

# Creiamo la finestra di gioco
schermo = pygame.display.set_mode((LARGHEZZA_SCHERMO, ALTEZZA_SCHERMO))
pygame.display.set_caption("Progetto: Alessio Falcini, Leonardo Occhirossi e Vittorio Cambiotti - Lezione 2")

# --- Colori ---
BIANCO = (255, 255, 255)   # Colore del nostro personaggio
NERO = (0, 0, 0)           # Colore dello sfondo

# --- Personaggio ---
LARGHEZZA_PERSONAGGIO = 40
ALTEZZA_PERSONAGGIO = 80

# Velocità del personaggio
velocita_personaggio = 5

# Posizione iniziale (centrata)
posizione_x = (LARGHEZZA_SCHERMO - LARGHEZZA_PERSONAGGIO) // 2
posizione_y = (ALTEZZA_SCHERMO - ALTEZZA_PERSONAGGIO) // 2

# Rettangolo del personaggio
personaggio = pygame.Rect(posizione_x, posizione_y, LARGHEZZA_PERSONAGGIO, ALTEZZA_PERSONAGGIO)

# --- Orologio ---
orologio = pygame.time.Clock()

# --- Ciclo principale ---
gioco_attivo = True
while gioco_attivo:
   # --- Gestione eventi ---
   for evento in pygame.event.get():
       if evento.type == pygame.QUIT:
           gioco_attivo = False
          
# TODO: realizzare il movimento del personaggio e calcolare i limiti di schermo 

   schermo.fill(NERO)  # Puliamo lo schermo con il colore nero
    # Disegniamo il personaggio (un rettangolo bianco)
   pygame.draw.rect(schermo, BIANCO, personaggio)
    # Aggiorniamo lo schermo per mostrare tutto quello che abbiamo disegnato
   pygame.display.flip()
    # Manteniamo il gioco a 60 fotogrammi al secondo
   orologio.tick(60)

# --- Uscita ---
pygame.quit()
