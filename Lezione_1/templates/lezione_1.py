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

# TODO: definire i colori, realizza il personaggio e posiziona il personaggio al centro dello schermo 

# --- Orologio ---
orologio = pygame.time.Clock()   # Controlla la velocità del gioco (FPS)

# --- Ciclo principale ---
gioco_attivo = True
while gioco_attivo:

# TODO: creare un ciclo for per leggere gli eventi con pygame.event.get() e riempi di colore lo sfondo e disegna il personaggio 
   
   # --- Aggiornamento dello schermo ---
   # TODO: aggiornare lo schermo e mantenere 60FPS

   # --- Uscita ---
pygame.quit()   # Chiude Pygame
