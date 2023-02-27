# Giornate di orientamento

Alla LUISS è tempo di orientamento: sono pianificate $N$ giornate di eventi presso la sede di viale Romania, che però, a causa della pandemia, può ospitare un numero massimo di persone ben definito. Per questo motivo, lo share di ogni evento giornaliero non può superare un certo valore $M$.

Quest'anno, per di più, il coordinatore dell'orientamento, che ha il compito di  di massimizzare $S$, lo share cumulativo della serie di eventi, tenterà un'approccio pubblicitario sperimentale. Per il primo giorno, infatti, ha già accumulato uno share pari ad $s_1$ ($\leq M$); mentre di giornata in giornata, fino al penultimo giorno, potrà pubblicizzare o meno l'evento del giorno seguente: a fine evento, se il responsabile chiede di sponsorizzare l'evento del giorno dopo, lo share del giorno successivo sarà maggiore del $x$% rispetto a quello precedente, altrimenti il giorno successivo avrà uno share del $y$% in meno rispetto al giorno precedente. Vale la legge $100x - 100y - xy = 0$.

Dati i numeri interi $N, M, s_1, x$, considera la sequenza di share giornalieri $s_1, s_2,..., s_N$, dove per ogni giorno $i < N$ si scelga se pubblicizzare o meno l'evento successivo di modo tale che $S = \sum_{i=1}^N s_i$ sia massima, sempre rispettando $s_i \leq M$ per ciascun $i$. Calcola quindi, caso per caso, la parte intera dello share complessivo massimo $S$ raggiungibile dalla serie di eventi.


## Assunzioni

- $N, M, s_1, x$ interi.
- $1 \leq N \leq 10^{11}$.
- $1 \leq M \leq 10^6$.
- $s_i \leq M$.
- $2 \leq x \leq 100$.
- ATTENZIONE: $100x - 100y - xy = 0$


## Casi di test

- I primi $10$ casi presentano $N \leq 10^3$, $M \leq 10^3$, $s_1 \leq 10^2$.
- I casi da $11$ a $20$ presentano $N \leq 10^6$, $M \leq 10^4$, $s_1 \leq 10^2$.
- I casi da $21$ a $30$ presentano $N \leq 10^9$, $M \leq 10^5$, $s_1 \leq 10^2$.
- I casi da $31$ a $40$ presentano $N \leq 10^{11}$, $M \leq 10^6$, $s_1 \leq 10^2$.
- I restanti test presentano casi limite.


## Dati di input

Vengono forniti $50$ casi di test, numerati da $1$ a $50$, ognuno preceduto da una riga vuota.

La prima ed unica riga di ogni caso di test contiene quattro numeri interi rappresentanti nell'ordine $N, M, s_1, x$.

## Dati di output

Per ogni caso di test che hai risolto, il file di output deve contenere una riga con la dicitura

```
Case #t: 
```

dove `t` è il numero del caso di test (a partire da $1$).

Deve seguire, sulla stessa riga, preceduta da spazio, la parte intera del massimo $S$ raggiungibile per il caso di test considerato.

## Esempi di input/output

---

**Input:**

```

10 20 1 25

15 30 4 75

...
```

---

**Output:**

```
Case #1: 33 
Case #2: 225
...
```

---
