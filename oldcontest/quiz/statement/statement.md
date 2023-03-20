## Descrizione del problema

Alla Luiss si sta organizzando un quiz a squadre!
Gli studenti vengono divisi in due gruppi ed il gruppo che risponde a più domande vince.

Purtroppo non tutti gli studenti vanno d'accordo, quindi sappiamo che uno studente può stare in squadra solo con studenti che considera "simpatici".
In input ti vengono date $M$ coppie di interi $A$ $B$, che indicano che lo studente $A$ considera "simpatico" lo studente $B$ e viceversa.
Devi trovare un modo per dividere gli $N$ studenti in due gruppi in modo che per ogni coppia di studenti appartenenti allo stesso gruppo questi si considerino "simpatici" a vicenda.
Se non esiste un modo per dividere gli studenti in due gruppi stampa -1, altrimenti stampa il numero di componenti del primo gruppo, i componenti del primo gruppo, il numero di componenti del secondo gruppo e i componenti del secondo gruppo.

![teams](team.jpg)

## Dati di input

La prima riga del file di input contiene un intero $T$, il numero di casi di test. Seguono $T$ casi di test, numerati da $1$ a $T$. Ogni caso di test è preceduto da una riga vuota.

Ciascun caso di test è composto da $M+1$ righe: la prima contiene due numeri interi $N$ , $M$, rispettivamente il numero di studenti ed il numero di coppie di studenti che si considerano reciprocamente "simpatici".
Ciascuna delle seguenti $M$ righe contiene due interi $A$ e $B$ separati da uno spazio che indicano che gli studenti $A$ e $B$ si considerano "simpatici" a vicenda.

## Dati di output

Il file di output deve contenere la risposta ai casi di test che sei riuscito a risolvere. Per ogni caso di test che hai risolto, il file di output deve contenere: 

Se non esiste un modo per dividere i due gruppi stampa -1
```
Case #t: -1
```

Altrimenti stampa in ordine:
- il numero di componenti del primo gruppo
- i componenti del primo gruppo
- il numero di componenti del secondo gruppo
- i componenti del secondo gruppo
Su un'unica riga e separati da uno spazio.
```
Case #t: N1 G1[0] G1[1] . . . G1[N1-1] N2 G2[0] G2[1] . . . G2[N2-1]

``` 

dove `t` è il numero del caso di test (a partire da $1$).

> _NOTA: Nessun gruppo può essere composto da zero studenti_

## Assunzioni

- $2 \le N \le 1\,000$.
- $0 \le M \le N*(N-1)/2$
- $0 \le A,B \le N-1$.
- $1 \le T \le 20$.

## Esempi di input/output

**Input:**

```
2

3 2
0 1
0 2

5 4
0 1
1 2 
0 3 
0 4


```

---

**Output:**

```
Case #1: 2 0 1 1 2
Case #2: -1
```

## Spiegazione

Nel **primo caso d'esempio** ci sono 3 studenti, una possibile suddivisione in gruppi è:

Squadra 1: {0, 1}

Squadra 2: {2}


Nel **secondo caso d'esempio** non è possibile dividere gli studenti in 2 squadre. 
