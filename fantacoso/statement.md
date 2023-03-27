# Fantacoso (*fantacoso*) (*da modificare*)

Il professor Martino ha deciso di estendere l'invito a partecipare alle fantaolimpiadi alle scuole degli studenti coinvolti. Ogni scuola può selezionare un massimo numero $N$ di ragazzi e sommare i punteggi da loro ottenuti durante le lezioni. La scuola con la somma punti maggiore verrà premiata tramite il conferimento del titolo di *scuola dei chad*.

Per evitare che scuole eccessivamente numerose o con studenti più esperti siano eccessivamente favorite nella competizione, il professor Martino stabilisce che i membri della squadra selezionata dalla scuola possono aver seguito il corso per un massimo di $M$ anni. Ad esempio, se viene stabilito che gli anni totali di esperienza della squadra siano massimo $10$, una scuola potrà scegliere al più due studenti del quinto anno. Se questi ultimi hanno realizzzato rispettivamente un punteggio di $120$ e $100$, il punteggio della scuola sarà di $100+120=220$ punti.

Ogni scuola ambisce a diventare la *scuola dei chad* ed è quindi fondamentale scegliere la squadra adatta al fine di massimizzare il punteggio.

## Dati di input

La prima riga del file di input contiene un intero $T$, il numero di casi di test. Seguono $T$ casi di test, numerati da $1$ a $T$. Ogni caso di test è preceduto da una riga vuota.

Ciascun caso di test è composto da $N+1$ righe. La prima riga contiene due interi separati da uno spazio: il primo intero rappresenta $N$, il numero di studneti della scuola che hanno preso parte alle lezioni, mentre il secondo intero rappresenta $M$, il numero massimo di anni di esperienza che la squadra scelta dovrà avere. Ciascuna delle seguenti $N$ righe contiene due interi $P_i$ e $Q_i$ separati da uno spazio: rispettivamente $P_i$ è il punteggio realizzato dallo studente $i$-esimo, e $Q_i$ sono gli anni di esperienza dello studnete $i$-esimo, per $i$ che va da $1$ a $N$.  

## Dati di output

Il file di output deve contenere la risposta ai casi di test che sei riuscito a risolvere. Per ogni caso di test che hai risolto, il file di output deve contenere una riga con la dicitura

```
Case #t: L
```

dove `t` è il numero del caso di test (a partire da $1$) e `L` rappresenta gli studenti, ordinati in senso crescente considerando i loro punteggi, che forniscono la soluzione: ovvero il sottoinsieme di studenti con punteggio totale massimo e che hanno un massimo di anni di esperienza $M$; gli studenti sono separati da uno spazio.  