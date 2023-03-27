# Fantacoso (*fantacoso*) (*da modificare*)

Il professor Martino ha deciso di estendere l'invito a partecipare alle fantaolimpiadi alle scuole degli studenti coinvolti. Ogni scuola può selezionare un massimo numero $N$ di ragazzi e sommare i punteggi da loro ottenuti durante le lezioni. La scuola con la somma punti maggiore verrà premiata tramite il conferimento del titolo di *scuola dei chad*.

Per evitare che scuole eccessivamente numerose o con studenti più esperti siano eccessivamente favorite nella competizione, il professor Martino stabilisce che i membri della squadra selezionata dalla scuola possono aver seguito il corso per un massimo di $M$ anni. Ad esempio, se viene stabilito che gli anni totali di esperienza della squadra siano massimo $10$, una scuola potrà scegliere al più due studenti del quinto anno. Se questi ultimi hanno realizzzato rispettivamente un punteggio di $120$ e $100$, il punteggio della scuola sarà di $100+120=220$ punti.

Ogni scuola ambisce a diventare la *scuola dei chad* ed è quindi fondamentale scegliere la squadra adatta al fine di massimizzare il punteggio.

## Dati di input

La prima riga del file di input contiene un intero $T$, il numero di casi di test. Seguono $T$ casi di test, numerati da $1$ a $T$. Ogni caso di test è preceduto da una riga vuota.

Ciascun caso di test è composto da $N+1$ righe. La prima riga contiene due interi separati da uno spazio: il primo intero rappresenta $N$, il numero di studneti della scuola che hanno preso parte alle lezioni, mentre il secondo intero rappresenta $M$, il numero massimo di anni di esperienza che la squadra scelta dovrà avere. Ciascuna delle seguenti $N$ righe contiene due interi $P_i$ e $E_i$ separati da uno spazio: rispettivamente $P_i$ è il punteggio realizzato dallo studente $i$-esimo, e $E_i$ sono gli anni di esperienza dello studente $i$-esimo, per $i$ che va da $1$ a $N$.  

## Dati di output

Il file di output deve contenere la risposta ai casi di test che sei riuscito a risolvere. Per ogni caso di test che hai risolto, il file di output deve contenere una riga con la dicitura

```
Case #t: L
```

dove `t` è il numero del caso di test (a partire da $1$) e `L` rappresenta gli studenti, ordinati in senso crescente considerando i loro punteggi, che forniscono la soluzione: ovvero il sottoinsieme di studenti con punteggio totale massimo e che hanno un massimo di anni di esperienza $M$; gli studenti sono separati da uno spazio.  

## Assunzioni

- $1 \le N \le 1\,000$.
- $1 \le M \le 1\,000$.
- $1 \le P_i \le 1\,000$.
- $1 \le E_i \le 5$.


## Esempi di input/output

---

**Input:**

```
2

4 4
160 4
85 1
90 2
70 4

5 6
45 2
40 1
50 1
90 4
100 4
```

---

**Output:**

```
Case #1: 3 2
Case #2: 4 3 2
```

---

## Spiegazione

Nel **primo caso d'esempio** abbiamo 4 studenti tra cui scegliere, con esperienza totale di massimo 10 anni. La soluzione di puntegggio totale massimo è dato dagli studenti 3 e 2, che hanno punteggio totale 175 ed esperienza di 3 anni  


---

Nel **secondo caso d'esempio** abbiamo 5 studenti tra cui scegliere, con esperienza totale di massimo 10 anni. La soluzione di punteggio totale massimo è data dagli studenti 4 3 e 2, che hanno punteggio totale 190 ed esperienza di 6 anni.