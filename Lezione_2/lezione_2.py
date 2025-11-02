# Autori: Alessio Falcini, Leonardo Occhirossi, Vittorio Cambiotti 
# Lezione 2: Movimento del personaggio e limiti della finestra
 
import pygame # Libreria per creare videogiochi
 
# Avviamo Pygame - questo è necessario per iniziare a usare Pygame 
pygame.init()
 
# Definiamo le dimensioni della finestra di gioco 
LARGHEZZA_SCHERMO = 800 # Larghezza in pixel 
ALTEZZA_SCHERMO = 600 # Altezza in pixel
 
# Creiamo la finestra di gioco
schermo = pygame.display.set_mode((LARGHEZZA_SCHERMO, ALTEZZA_SCHERMO))
pygame.display.set_caption("Progetto: Alessio Falcini, Leonardo Occhirossi e Vittorio Cambiotti - Lezione 2")
 
# Definiamo i colori che useremo nel gioco (in RGB: Rosso, Verde, Blu) 
BIANCO = (255, 255, 255) # Colore del nostro personaggio 
NERO = (0, 0, 0) # Colore dello sfondo
 
# Dimensioni del nostro personaggio 
LARGHEZZA_PERSONAGGIO = 40 
ALTEZZA_PERSONAGGIO = 80
 
# Quanto velocemente si muove il nostro personaggio 
velocita_personaggio = 5
 
# Posizioniamo il personaggio al centro dello schermo 
posizione_x = (LARGHEZZA_SCHERMO - LARGHEZZA_PERSONAGGIO) // 2 
posizione_y = (ALTEZZA_SCHERMO - ALTEZZA_PERSONAGGIO) // 2
 
# Creiamo il rettangolo del personaggio (serve per muoverlo e controllare le collisioni) 
personaggio = pygame.Rect(posizione_x, posizione_y, LARGHEZZA_PERSONAGGIO, ALTEZZA_PERSONAGGIO)
 
# Creiamo un orologio per controllare la velocità del gioco 
orologio = pygame.time.Clock()
 
# Ciclo principale essenziale: mantiene la finestra attiva e disegna il personaggio 
gioco_attivo = True
 
while gioco_attivo: 
    # Controlliamo gli eventi (click della X, tasti, ecc.) 
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            gioco_attivo = False
 
    # Muoviamo il personaggio con i tasti W, A, S, D 
    tasti = pygame.key.get_pressed() 
    if tasti[pygame.K_w]: # Se premiamo W, va su 
        personaggio.y -= velocita_personaggio 
    if tasti[pygame.K_s]: # Se premiamo S, va giù 
        personaggio.y += velocita_personaggio 
    if tasti[pygame.K_a]: # Se premiamo A, va a sinistra 
        personaggio.x -= velocita_personaggio 
    if tasti[pygame.K_d]: # Se premiamo D, va a destra 
        personaggio.x += velocita_personaggio
 
    # Impedisce al personaggio di uscire dallo schermo 
    personaggio.x = max(0, min(personaggio.x, LARGHEZZA_SCHERMO - LARGHEZZA_PERSONAGGIO))
    personaggio.y = max(0, min(personaggio.y, ALTEZZA_SCHERMO - ALTEZZA_PERSONAGGIO))
 
    # Disegniamo tutto sullo 
    schermo.fill(NERO) # Puliamo lo schermo con il colore nero
 
    # Disegniamo il personaggio (un rettangolo bianco) 
    pygame.draw.rect(schermo, BIANCO, personaggio)
 
    # Agggiorniamo lo schermo per mostrare tutto quello che abbiamo disegnato 
    pygame.display.flip()
 
    # Manteniamo il gioco a 60 fotogrammi al secondo 
    orologio.tick(60)
 
# Quando il gioco finisce, chiudiamo Pygame 
pygame.quit()
