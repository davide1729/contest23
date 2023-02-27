## Descrizione del problema

Carlo si è trasferito a Roma per frequentare la Luiss, e avendo la domenica libera, vuole visitare in un giorno, tutte le meravigliose attrazioni della città (un compito veramente arduo, considerando che la città ne è piena). Per fortuna, Carlo è aiutato nei suoi spostamenti dal fedele taxista Chad che però, essendo molto bravo nel suo lavoro, vorrebbe fargli spendere un mucchio di soldi (proporzionali al numero di corse). Carlo ha quindi chiesto aiuto a Michele, cui ha fornito le seguenti istruzioni:

- Roma è rappresenta da una matrice binaria di dimensioni $N\times M$, in cui $1$ denota un'attrazione turistica e $0$ indica un luogo non interessante.

- In corrispondenza di ogni $1$ si trova un'attrazione, e le attrazioni vanno tutte visitate.

- Ogni cella della matrice può essere connessa fino a $8$ celle, quelle a nord, sud, est, ovest, nord-est, sud-est, nord-ovest, sud-ovest. Le celle vicine potrebbero essere in numero inferiore se la cella si trova agli estremi confini della città (cioè sul bordo della matrice).

- Da ogni cella corrispondente a un'attrazione, ci si può spostare a piedi a una qualunque delle al più $8$ celle vicine, a patto che in quest'ultima contenga un'attrazione.

- Carlo, per risparmiare tempo, non camminerà mai in un luogo che non sia un'attrazione turistica.

- Carlo si sposterà sempre a piedi, tra le attrazioni fin dove possibile, e poi effettuerà una corsa sul taxi di Chad per raggiungere un nuova attrazione ancora non visitata.

Aiuta Michele a capire qual è il minimo numero di corse richiesti a Carlo per poter visitare tutte le attrazioni.

> ![roma](./roma.jpg "Roma")

## Dati di input

La prima riga del file di input contiene un intero $T$, il numero di casi di test. Seguono $T$ casi di test, numerati da $1$ a $T$. Ogni caso di test è preceduto da una riga vuota.

Ciascun caso di test è composto da $N+1$ righe:

- la prima riga contiene $i$ numeri $N$ e $M$
- le successive $N$ righe contengono ciascuna $M$ valori $0$ o $1$ separati da spazi.

## Dati di output

Il file di output deve contenere la risposta ai casi di test che sei riuscito a risolvere. Per ogni caso di test che hai risolto, il file di output deve contenere una riga con la dicitura

```
Case #t: x
```

dove $t$ è il numero del caso di test (a partire da $1$) e $x$ è il minimo numero di corse che Carlo deve effettuare per visitare tutte le attrazioni nella mappa corrispondente al caso di test $t$.

## Assunzioni

- $1\leq N,M\leq 300$.

## Esempi di input/output

---

**Input:**

```
2

5 5
1 1 0 0 0
0 1 0 0 1
1 0 0 1 1
0 0 0 0 0
1 0 1 0 1 

3 4
1 0 0 1
0 1 0 0
0 0 1 0
```

---

**Output:**

```
Case #1: 4
Case #2: 1
```

---

## Spiegazione

Indichiamo le zone della mappa che possono essere visitate a piedi con la stessa lettera.

---

Nel **primo caso d'esempio**, le zone sono $5$:

```
X X 0 0 0
0 X 0 0 Y
X 0 0 Y Y
0 0 0 0 0
Z 0 V 0 W 
```

Sarà pertanto necessario effettuare $4$ corse, ad esempio da $X$ a $Y$, da $Y$ a $W$, da $W$ a $V$, e da $V$ a $Z$.

---

Nel **secondo caso d'esempio**, le zone sono $2$:

```
X 0 0 Y
0 X 0 0
0 0 X 0
```

Sarà pertanto necessario effettuare una sola corsa, da $X$ a $Y$ o viceversa.


 
