# Calendario Accademico

In una nota scuola superiore, il Professor *Lorenzo Cervellini* deve organizzare il calendario per il suo corso. Il professore, che ha a disposizione una lista (di lunghezza $N$) con il numero di studenti ($S$) che si sono registrati per partecipare alle sue lezioni, vorrebbe poter spiegare nei giorni in cui meno studenti sono presenti e interrogare quando ce ne sono di più, in modo da poter avere il maggior numero di persone impreparate possibili. Ovviamente, il professore, deve prima spiegare un argomento per interrogare gli studenti e non vuole iniziarne uno nuovo prima di aver interrogato sul vecchio. Quindi, tra una spiegazione e un’altra, c’è sempre un’interrogazione in mezzo. Inoltre, essendo il tempo nella giornata troppo poco, non è possibile spiegare ed interrogare nello stesso giorno. Sapendo che il *Professor Lorenzo Cervellini* vuole spiegare $K$ argomenti, che può scegliere di ridurre per incrementare il numero di studenti impreparati, calcola quanti di questi riuscirà a interrogare. 

## Assunzioni

- $N$, $S$ e $K$ interi
- $0 \leq N \leq 10^5$
- $0 \leq S \leq 10^4$
- $1 \leq K \leq \frac{N}{2}+1$.


## Casi di test

- Per il primo gruppo di casi di test $K = 1$, $N \leq 10^2$ e $S \leq 10^2$.
- Per il secondo gruppo di casi di test $K = 2$, $N \leq 10^3$ e $S \leq 10^3$.
- Per il terzo gruppo di casi di test, non ci sono limitazioni rispetto a quanto riportato nella sezione "Assunzioni".

## Dati di input

La prima riga del file di input contiene un intero $T$, il numero di casi di test.  
Seguono $T$ casi di test, numerati da $1$ a $T$. Ogni caso di test è preceduto da una riga vuota.

Ogni caso di test presenta nella prima riga due interi $N$ e $K$ corrispondenti rispettivamente alla lunghezza del calendario accademico e al numero di argomenti. 

Segue una riga con $N$ interi che rappresentano le prenotazioni effettuate per ogni giorno del calendario dal giorno $0$ al giorno $N-1$.

Tutti i numeri sono separati da uno spazio.

## Dati di output

Il file di output deve contenere la risposta ai casi di test che sei riuscito a risolvere. Per ogni caso di test che hai risolto, il file di output deve contenere una riga con la dicitura:

```
Case #t: 
```

dove `t` è il numero del caso di test (a partire da $1$).

Per ogni caso di test deve essere presente un solo intero: il numero massimo di studenti impreparati che il professor Mastronzo riuscirà ad interrogare.


## Esempi di input/output

**Input:**

```
4

6 2
7 4 8 2 9 10

10 1
13 2 4 6 0 15 7 6 5 2

4 2
1 5 2 7

5 1
9 6 4 1 1
```

---

**Output:**

```
Case #1: 12
Case #2: 15
Case #3: 9
Case #4: 0
```

**Spiegazione**

- Nel primo caso di test, il professore spiegherà nel giorno $1$ (ricorda: il primo giorno è il giorno $0$) con $4$ studenti prenotati per poi interrogare nel giorno $2$ con $8$ studenti prenotati. Successivamente spiegherà nel giorno $3$ con $2$ studenti per poi interrogare nel giorno $5$ con $10$ studenti. Dalla prima tornata di interrogazioni riuscirà ad interrogare $8-4=4$ studenti impreparati e dalla seconda tornata $10-2=8$ studenti impreparati. Sommandoli abbiamo: $8+4=12$

- Nel secondo caso di test, il professore spiegherà nel giorno $4$ con $0$ studenti prenotati per poi interrogare nel giorno $5$ con $15$ studenti prenotati. Con questa tornata di interrogazioni riuscirà ad interrogare $15-0=15$ studenti impreparati.

- Nel terzo caso di test, il professore spiegherà nel giorno $0$ con $1$ studente prenotate per poi interrogare nel giorno $1$ con $5$ studenti prenotati. Successivamente spiegherà nel giorno $2$ con $2$ studenti per poi interrogare nel giorno $3$ con $7$ studenti. Dalla prima tornata di interrogazioni riuscirà ad interrogare $5-1=4$ studenti impreparati e dalla seconda tornata $7-2=5$ studenti impreparati. Sommandoli abbiamo: $8+4=12$

- Nell'ultimo caso di test, per il professore è impossibile trovare studenti impreparati durante l'interrogazione, dunque il risultato è $0$.
