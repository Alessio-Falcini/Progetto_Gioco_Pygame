# Lezione 5 — Collisioni tra Proiettili e Nemici

## Obiettivo della lezione

In questa lezione finalizziamo il gioco introducendo le **collisioni**: quando un proiettile colpisce un nemico, **entrambi vengono rimossi** dallo schermo. Questo permette di completare la dinamica principale del gioco.

---

## File in questa lezione

- **`lezione_5.py`** — codice eseguibile contenente:
  - Movimento del personaggio
  - Sparo dei proiettili
  - Spawn e movimento dei nemici
  - Rilevamento e gestione delle collisioni proiettile-nemico

---

## Esecuzione

Per eseguire la lezione:

```bash
python lezione_5.py
```

### Comandi durante l'esecuzione

- **W, A, S, D** — Muoviti in tutte le direzioni
- **Tasto sinistro del mouse** — Spara
- **Nemici rossi** — Appariranno ai bordi e si muoveranno verso di te
- **Collisione** — Quando un proiettile colpisce un nemico, entrambi scompariranno

---

## Spiegazione delle funzionalità aggiunte

### 1. Collisione proiettile-nemico

```python
if nemico.colliderect(proiettile_rect):
    nemici_da_rimuovere.append(nemico)
    proiettili_da_rimuovere.append(p)
```

- **`pygame.Rect.colliderect()`** rileva l'intersezione tra due rettangoli
- Se un proiettile colpisce un nemico, entrambi vengono aggiunti a liste temporanee per la rimozione

### 2. Rimozione sicura

```python
for nemico in nemici_da_rimuovere:
    nemici.remove(nemico)
for p in proiettili_da_rimuovere:
    proiettili.remove(p)
```

- Rimuovere gli oggetti dalle liste **dopo** aver controllato tutte le collisioni evita errori di iterazione
- Questo pattern previene crash dovuti alla modifica di liste durante l'iterazione

---
### 3. Creazione della collision rect

```python
battaglia_rect = pygame.Rect(p[0]-DIM_PROIETTILE//2, p[1]-DIM_PROIETTILE//2, 
                             DIM_PROIETTILE, DIM_PROIETTILE)
if nemico.colliderect(battaglia_rect):
```

- I proiettili sono memorizzati come liste `[x, y, dx, dy]` anziché come Rect
- Creiamo un Rect al momento della collisione con le coordinate corrette (sottraiamo `DIM_PROIETTILE//2` perché il proiettile è centrato su `x, y`)
- Questo permette di usare il metodo `colliderect()` per il rilevamento preciso

---
## Concetti chiave

### Normalizzazione vettoriale

Sia nel movimento dei nemici che nello sparo dei proiettili, utilizziamo la **normalizzazione del vettore**:

``` python
distanza = math.hypot(dx, dy)  # Calcola la lunghezza del vettore
if distanza != 0:
    dx, dy = dx / distanza, dy / distanza  # Normalizza
```

Questo garantisce che il movimento avvenga sempre alla stessa velocità, indipendentemente dalla distanza dal target.

### Gestione della iterazione sicura

Un pattern importante è raccogliere gli oggetti da eliminare in liste temporanee e poi rimuoverli **dopo** aver completato i controlli. Questo evita errori come "list changed size during iteration".

---
## Note didattiche

Ora il gioco ha la dinamica completa: movimento, sparo, nemici e collisioni. Tutti gli elementi principali di un semplice gioco sparatutto sono stati implementati e funzionano correttamente insieme.

---

## Prossimi passi

Possibili miglioramenti futuri:
- Sistema di punteggio
- Vite del giocatore
- Difficoltà progressiva
- Effetti sonori e particelle
- Menu principale e schermata di game over
