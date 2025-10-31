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

* Viene rilevato il **click sinistro del mouse** (`button == 1`);
* Con `pygame.mouse.get_pos()` otteniamo la **posizione del cursore**.
---

### 3. Calcolo della direzione del proiettile

```python
direzione_x = mouse_x - personaggio.centerx
direzione_y = mouse_y - personaggio.centery
distanza = (direzione_x**2 + direzione_y**2)**0.5

if distanza != 0:
    direzione_x /= distanza
    direzione_y /= distanza
```

* Si calcola la **direzione normalizzata (versore)** dal centro del personaggio al punto cliccato;
* Questo permette ai proiettili di muoversi sempre alla **stessa velocità**, indipendentemente dalla distanza del bersaglio.

---

### 4. Creazione e memorizzazione del proiettile

```python
proiettile = pygame.Rect(...)
lista_proiettili.append({'rect': proiettile, 'dx': direzione_x, 'dy': direzione_y})
```

* Ogni proiettile viene rappresentato come un rettangolo (`pygame.Rect`);
* Viene salvato in una lista con la sua direzione (`dx`, `dy`).
---

### 5. Movimento e rimozione dei proiettili

```python
for proiettile in lista_proiettili[:]:
    proiettile['rect'].x += proiettile['dx'] * VELOCITA_PROIETTILE
    proiettile['rect'].y += proiettile['dy'] * VELOCITA_PROIETTILE
```

* I proiettili vengono **spostati** ad ogni frame;
* Se un proiettile esce dallo schermo, viene **rimosso** dalla lista per evitare spreco di memoria.

---

### 6. Disegno dei proiettili

```python
pygame.draw.circle(schermo, GIALLO, proiettile['rect'].center, DIMENSIONE_PROIETTILE // 2)
```

* Ogni proiettile viene rappresentato come un **cerchio giallo**;
* Il centro del cerchio è quello del rettangolo associato.

***

## Note didattiche 📝

* I concetti di **direzione normalizzata** e **liste di oggetti dinamici** sono fondamentali nei videogiochi;
* Questa lezione prepara le basi per la prossima fase, dove verranno introdotti nemici e collisioni tra proiettili e nemici.
