# Lezione 5 — Collisioni tra proiettili e nemici

## Obiettivo della lezione

In questa lezione finalizziamo il gioco introducendo le **collisioni** : quando una vittoria colpisce un nemico, **entrambi vengono rimossi** dallo schermo.

Questo permette di completare la dinamica principale del gioco.

---

## File in questa lezione

- `lezione\_5.py` — codice eseguibile contenente:
- movimento del personaggio;
- sparo dei proiettili;
- spawn e movimento dei nemici;
- rilevamento e gestione delle collisioni-nemico.

---

## Esecuzione

Per eseguire la lezione:

```bash

python lezione\_5.py
```
Durante l'esecuzione:

- Muoviti con W, A, S, D
- Spara con il tasto sinistro del mouse
- I nemici rossi appariranno ai bordi e si muoveranno verso di te;
- Quando una competizione li colpisce, scompariranno.

⸻

Spiegazione funzionalità aggiunte

1. Collisione competizione-nemico

if nemico.colliderect(proiettile_rect):

nemici_da_rimuovere.append(nemico)

proiettili_da_rimuovere.append(p)

- pygame.Rect.colliderect() rileva l'intersezione tra due rettangoli.
- Se un successo colpisce un nemico, entrambi vengono aggiunti alla lista temporanea per la rimozione.

2. Rimozione sicura

per nemico in nemici_da_rimuovere: nemici.remove(nemico)

for p in proiettili_da_rimuovere: proiettili.remove(p)

- Rimuovere gli oggetti dalle liste dopo aver controllato tutte le collisioni evita errori di iterazione.

⸻

Note didattiche

- Ora il gioco ha la dinamica completa: movimento, sparo, nemici e collisione
