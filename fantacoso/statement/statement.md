# Fantacoso (*fantacoso*)

> **Attenzione**: Questo task ha un tempo limite di 10 minuti per l'invio della soluzione. Una volta richiesto un input, il timer partirà in automatico, e dopo la scadenza non sarà più possibile inviare una soluzione per quell'input.
> *È sempre possibile richiedere un nuovo input*, per cui non preoccuparti se il timer scade: dovrai semplicemente richiedere e scaricare un nuovo input.

Il professor Martino ha deciso di estendere l'invito a partecipare alle fantaolimpiadi alle scuole degli studenti coinvolti. Ogni scuola può selezionare un massimo numero $N$ di ragazzi e sommare i punteggi da loro ottenuti durante le lezioni. La scuola con la somma punti maggiore verrà premiata tramite il conferimento del titolo di *scuola dei chad*.

Per evitare che scuole con studenti più esperti siano eccessivamente favorite nella competizione, il professor Martino stabilisce che la somma degli anni di esperienza (anni di frequentazione del corso) dei componenti della squadra deve essere minore o uguale alla stessa $E$ per tutte le scuole. Ad esempio, se viene stabilita un'esperienza massima di 10, una squadra di 3 studenti potrà essere formata da uno studente con 5 anni di esperienza e due studenti con 2 anni di esperienza (9 anni di esperienza totale), ma non da tre ragazzi con 4 anni di esperienza (12 anni di esperinza totale). 
Inoltre, al fine di coinvolgere tutti gli studenti, una squadra non può avere una componente maschile superiore ad un numero prestabilito $P$.
Ad esempio, se viene stabilita un numero massimo di 8, una squadra di 10 studenti non può essere composta da più di 8 ragazzi.

Ogni scuola ambisce a diventare la *scuola dei chad* ed è quindi fondamentale scegliere la squadra adatta al fine di massimizzare il punteggio.

## Dati di input

La prima riga del file di input contiene un intero $T$, il numero di casi di test. Seguono $T$ casi di test, numerati da $1$ a $T$. Ogni caso di test è preceduto da una riga vuota.

Ciascun caso di test è composto da $K+1$ righe. La prima riga contiene quattro interi separati da uno spazio: il primo intero rappresenta $K$, il numero di studenti della scuola che hanno preso parte alle lezioni; il secondo rappresenta $N$, il massimo numero di studenti selezionabili; il terzo rappresenta $E$, la massima esperienza della squadra ed il quarto $P$, il massimo numero di ragazzi che possono essere inseriti nella squadra. Ciascuna delle seguenti $K$ righe contiene tre interi $P_i$ e $E_i$ $G_i$ separati da uno spazio: rispettivamente $P_i$ è il punteggio realizzato dallo studente $i$-esimo, $E_i$ sono gli anni di esperienza dello studente $i$-esimo, $G_i$ stabilisce se lo studente $i$-esimo è maschio (1) o femmina (0) per $i$ che va da $1$ a $K$.  

## Dati di output

Il file di output deve contenere la risposta ai casi di test che sei riuscito a risolvere. Per ogni caso di test che hai risolto, il file di output deve contenere una riga con la dicitura

```
Case #t: L
```

dove `t` è il numero del caso di test (a partire da $1$) e `L` rappresenta il punteggio totale massimo che può essere ottenuto selezionando un massimo di $N$ studenti, con massimo numero $P$ di ragazzi e con esperienza totale massima $E$.

## Assunzioni

- $1 \le K \le 13$.
- $1 \le N \le K$.
- $1 \le E \le 5*K$.
- $0 \le P \le N$.
- $1 \le P_i \le 200$.
- $1 \le E_i \le 5$.
- $0 \le G_i \le 1$.


## Esempi di input/output

---

**Input:**

```
1

4 3 20 3
100 3 1
90 4 0
60 5 0
30 4 1

```

---

**Output:**

```
Case #1: 250
```

---

## Spiegazione

Nel **caso d'esempio** abbiamo da scegliere tre studenti, con esperienza totale uguale o inferiore a 20 anni e numero di ragazzi in squadra uguale o inferiore a 3. Il punteggio totale massimo è 250, dato dal primo, secondo e terzo studente (100+90+60=250) che presentano un'esperienza massima di 12, quindi minore di 20, e un numero di ragazzi pari a 1, quindi minore 3


