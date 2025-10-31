# Lezione 3 — Aggiunta della meccanica di sparo

## Obiettivo della lezione

In questa terza lezione introduciamo la possibilità per il giocatore di **sparare proiettili** cliccando con il mouse.
I proiettili vengono diretti verso il punto cliccato e si muovono con velocità costante.

---

## File in questa lezione

- `lezione_3.py` — codice sorgente contenente:
  - meccanica di sparo con il mouse;
  - lista per la gestione dei proiettili;
  - calcolo della direzione e movimento dei proiettili;
  - disegno dinamico dei proiettili sullo schermo.

---

## Esecuzione

Per avviare la lezione, eseguire dalla cartella del progetto:

```bash
python lezione_3.py
```

**Durante l’esecuzione:**
* Il personaggio può muoversi con i tasti W, A, S, D;
* Cliccando il tasto sinistro del mouse, vengono sparati proiettili gialli in direzione del cursore;
* I proiettili spariti dallo schermo vengono rimossi automaticamente.

## Spiegazione passo-passo delle nuove funzionalità

### 1. Importazione della libreria random

```python
import random
```

Sebbene in questa fase non sia ancora usata per i nemici, la libreria viene importata in previsione delle prossime lezioni (creazione dei nemici casuali).

---

### 2. Gestione dell’input del mouse

```python
elif evento.type == pygame.MOUSEBUTTONDOWN:
    if evento.button == 1:
        mouse_x, mouse_y = pygame.mouse.get_pos()
```

* Viene rilevato il **click sinistro del mouse** (\`button == 1\`);
* Con \`pygame.mouse.get_pos()\` otteniamo la **posizione del cursore**.
