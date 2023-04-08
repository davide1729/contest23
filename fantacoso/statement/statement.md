# Fantacoso (*fantacoso*) (*da modificare*)

Il professor Martino ha deciso di estendere l'invito a partecipare alle fantaolimpiadi alle scuole degli studenti coinvolti. Ogni scuola può selezionare un massimo numero $N$ di ragazzi e sommare i punteggi da loro ottenuti durante le lezioni. La scuola con la somma punti maggiore verrà premiata tramite il conferimento del titolo di *scuola dei chad*.

Per evitare che scuole con studenti più esperti siano eccessivamente favorite nella competizione, il professor Martino stabilisce che la media degli anni di esperienza (anni di frequentazione del corso) dei componenti della squadra (approssimata alla prima cifra intera) deve essere minore o uguale alla stessa $M$ per tutte le scuole. Ad esempio, se viene stabilito che la media degli anni di esperienza della squadra sia $4$, una scuola potrà scegliere uno studente del quinto ed uno del terzo anno (M=4) ma anche uno studente del quinto ed uno del primo anno (M=3).
Inoltre, al fine di coinvolgere tutti gli studenti, una squadra non può avere una componente maschile superiore ad una prestabilita percentuale $P$. Se la percentuale scelta è 80%, una squadra di 10 studenti non può essere composta da più di 8 ragazzi.

Ogni scuola ambisce a diventare la *scuola dei chad* ed è quindi fondamentale scegliere la squadra adatta al fine di massimizzare il punteggio.

## Dati di input

La prima riga del file di input contiene un intero $T$, il numero di casi di test. Seguono $T$ casi di test, numerati da $1$ a $T$. Ogni caso di test è preceduto da una riga vuota.

Ciascun caso di test è composto da $N+1$ righe. La prima riga contiene quattro interi separati da uno spazio: il primo intero rappresenta $K$ il numero di studenti della scuola che hanno preso parte alle lezioni, il secondo rappresenta $N$, il massimo numero di studenti selezionabili, il terzo rappresenta $M$, l'esperienza massima degli studenti da selezionare per la gara ed il quarto $P$, la percentuale massima di ragazzi che possono essere inseriti in squadra. Ciascuna delle seguenti $N$ righe contiene tre interi $P_i$ e $E_i$ $G_i$ separati da uno spazio: rispettivamente $P_i$ è il punteggio realizzato dallo studente $i$-esimo, $E_i$ sono gli anni di esperienza dello studente $i$-esimo, $G-i$ stabilisce se lo studente $i$-esimo è maschio (1) o femmina (0) per $i$ che va da $1$ a $N$.  

## Dati di output

Il file di output deve contenere la risposta ai casi di test che sei riuscito a risolvere. Per ogni caso di test che hai risolto, il file di output deve contenere una riga con la dicitura

```
Case #t: L
```

dove `t` è il numero del caso di test (a partire da $1$) e `L` rappresenta gli studenti, ordinati in senso crescente considerando i loro punteggi, che forniscono la soluzione: ovvero il sottoinsieme di studenti con punteggio totale massimo e che hanno un massimo di anni di esperienza $M$; gli studenti sono separati da uno spazio.  

## Assunzioni

- $1 \le K \le 1\,000$.
- $1 \le N \le 1\,000$.
- $1 \le M \le 5\,000$.
- $0 \le P \le 100$.
- $1 \le P_i \le 1\,000$.
- $1 \le E_i \le 5$.
- $0 \le G_i \le 1$.


## Esempi di input/output

---

**Input:**

```
2

4 2 4 90
160 4 1
85 1 1
90 2 1
70 4 2

5 3 3 70
45 2 1
40 1 1
50 1 2
90 4 1
100 4 2
```

---

**Output:**

```
Case #1: 1 4
Case #2: 5 4 3
```

---

## Spiegazione

Nel **primo caso d'esempio** abbiamo da scegliere due studenti, con esperienza media di 4 anni ed una percentuale massima di ragazzi o ragazze nella squadra inferiore o uguale al 60%. La soluzione di puntegggio totale massimo è dato dagli studenti 1 e 4, che hanno punteggio totale di 230 ed esperienza media di 4 anni. Inoltre la percentuale di ragazzi(50%) e quella di ragazze (50%) non supera quella prestabilita (60%)


---

Nel **secondo caso d'esempio** abbiamo da scegliere tre studenti, con esperienza media di 3 anni ed una percentuale massima di ragazzi o ragazze nella squadra inferiore o uguale al 70%. La soluzione di punteggio totale massimo è data dagli studenti 5 4 e 3, che hanno punteggio totale 240 ed esperienza media di 3 anni. Inoltre la percentuale di ragazzi(33%) e quella di ragazze (67%) non supera quella prestabilita (70%)
