# Midterm USA 2026 — diretta

Pagina per seguire le elezioni di metà mandato del 3 novembre 2026: Senato, Camera e governatori, prima del voto (sondaggi e proiezioni) e durante lo spoglio (risultati in diretta). Orari in ora italiana.

- `index.html` — la pagina, autonoma (nessuna dipendenza esterna)
- `dati/` — dati di Senato, Camera e governatori (`mode`: `pre` o `live`)
- `tools/` — modello della pagina, geometrie degli stati (us-atlas) e `build.py` per ricostruire `index.html`

Per aggiornare: modificare i file in `dati/` e lanciare `python3 tools/build.py`.
