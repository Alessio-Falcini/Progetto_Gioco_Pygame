# Lezione 1: Introduzione e impostazione dell'ambiente di gioco
import pygame   # Libreria per creare videogiochi
# --- Inizializzazione ---
pygame.init()   # Avvio di Pygame
# --- Costanti ---
LARGHEZZA_SCHERMO = 800   # Larghezza finestra in pixel
ALTEZZA_SCHERMO = 600     # Altezza finestra in pixel
# Creazione della finestra di gioco
schermo = pygame.display.set_mode((LARGHEZZA_SCHERMO, ALTEZZA_SCHERMO))
pygame.display.set_caption("Progetto: Alessio Falcini, Leonardo Occhirossi e Vittorio Cambiotti - Lezione 1")
# --- Colori (in RGB) ---
# TODO: definire i colori BIANCO e NERO come tuple RGB
# Es: BIANCO = (255, 255, 255)
# --- Personaggio ---
# TODO: definire LARGHEZZA_PERSONAGGIO e ALTEZZA_PERSONAGGIO
# TODO: calcolare posizione_x e posizione_y in modo che il personaggio sia al centro dello schermo
# TODO: creare il rettangolo "personaggio" con pygame.Rect(posizione_x, posizione_y, LARGHEZZA_PERSONAGGIO, ALTEZZA_PERSONAGGIO)
# --- Orologio ---
orologio = pygame.time.Clock()   # Controlla la velocità del gioco (FPS)
# --- Ciclo principale ---
gioco_attivo = True
while gioco_attivo:
   # --- Gestione eventi ---
   # TODO: creare un ciclo for per leggere gli eventi con pygame.event.get()
   # Se l’evento è pygame.QUIT → impostare gioco_attivo = False
   # --- Logica di gioco ---
   # (non necessaria per questa lezione)
   # --- Disegno ---
   # TODO: riempire lo schermo con il colore NERO
   # TODO: disegnare il personaggio (rettangolo bianco) con pygame.draw.rect
   # --- Aggiornamento dello schermo ---
   # TODO: aggiornare lo schermo con pygame.display.flip()
   # TODO: mantenere 60 FPS con orologio.tick(60)
# --- Uscita ---
pygame.quit()   # Chiude Pygame
