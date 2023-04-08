
---

## Descrizione del problema

Il prof. Italiano è improvvisamente diventato un appassionato di meme, e da un po' di tempo a questa parte non riesce a fare lezione senza inserire dei meme nelle sue slide. Come si sa, i boomer sono molto lenti e il prof. Italiano non è da meno: infatti passa sempre un tempo esagerato a creare i meme per le sue lezioni! 

Nel preparare la prossima lezione, il prof. Italiano ha pensato a $N$ meme tra cui deve scegliere i migliori da inserire nelle sue slide. Ogni meme è caratterizzato da un tempo stimato per la sua preparazione, espresso in minuti, e da un indice di qualità, un numero intero compreso tra $1$ a $100$, che indica quanto è sgravato (divertente) il meme.

![Un meme sgravato (grazie ad Alessandro Adem)](picture.png)

*Un meme sgravato (grazie ad Alessandro Adem)*

Passando tutti gli $N$ meme in rassegna, il prof. Italiano si convince che il meme $i$ richiederà un tempo di preparazione pari a $P_i$ minuti e avrà un indice di qualità pari a $Q_i$, per $i$ che va da $1$ a $N$. Dato un insieme di meme, la sua **qualità totale** è data dalla somma degli indici di qualità dei singoli meme. Ad esempio, se il meme $1$ e il meme $3$ hanno rispettivamente indici di qualità $19$ e $23$, la qualità totale dell'insieme {$1,3$} sarà pari a $19+23=42$. 

Purtroppo il prof. Italiano, oltre a essere molto lento, si riduce sempre a fare le cose all'ultimo minuto, e si accorge improvvisamente che sono rimasti soltanto pochi minuti prima della sua lezione. Di conseguenza, deve decidere molto velocemente quali meme inserire nelle slide e cominciare a prepararli.  Visto che i suoi studenti hanno grandi aspettative, vuole selezione l'insieme di meme di **qualità totale massima** che riesce a preparare entro il tempo disponibile.

Aiuta il prof. Italiano a scegliere i meme più divertenti da preparare nel poco tempo rimasto!



## Dati di input

La prima riga del file di input contiene un intero $T$, il numero di casi di test. Seguono $T$ casi di test, numerati da $1$ a $T$. Ogni caso di test è preceduto da una riga vuota.

Ciascun caso di test è composto da $N+1$ righe. La prima riga contiene due interi separati da uno spazio: il primo intero rappresenta $N$, il numero di meme da cui scegliere, mentre il secondo intero rappresenta $M$, il numero di minuti rimasto prima dell'inizio della lezione. Ciascuna delle seguenti $N$ righe contiene due interi $P_i$ e $Q_i$ separati da uno spazio: rispettivamente $P_i$ è il tempo richiesto per preparare il meme $i$-esimo, e $Q_i$ è l'indicatore di qualità del meme $i$-esimo, per $i$ che va da $1$ a $N$.  

## Dati di output

Il file di output deve contenere la risposta ai casi di test che sei riuscito a risolvere. Per ogni caso di test che hai risolto, il file di output deve contenere una riga con la dicitura

```
Case #t: L
```

dove `t` è il numero del caso di test (a partire da $1$) e `L` rappresenta i meme, ordinati in senso crescente, che forniscono la soluzione: ovvero il sottoinsieme di meme di qualità totale massima che possono essere preparati entro il tempo $M$; i meme sono separati da uno spazio.  

## Assunzioni

- $1 \le N \le 1\,000$.
- $1 \le M \le 1\,000$.
- $1 \le P_i \le 1\,000$.
- $1 \le Q_i \le 100$.
- Almeno un $P_i$ è $\leq M$.


## Esempi di input/output

---

**Input:**

```
2

4 10
6 30
5 10
3 50
4 40

5 11
5 19
2 6
1 1
6 23
7 28
```

---

**Output:**

```
Case #1: 3 4
Case #2: 1 4
```

---

## Spiegazione

Nel **primo caso d'esempio** abbiamo 4 meme tra cui scegliere, da preparare al più in 10 minuti. La soluzione di qualità totale massima è data dai meme 3 e 4, che hanno qualità totale 90 e richiedono 7 minuti.  


---

Nel **secondo caso d'esempio** abbiamo 5 meme tra cui scegliere, da preparare al più in 11 minuti. La soluzione di qualità totale massima è data dai meme 1 e 4, che hanno qualità totale 42 e richiedono 11 minuti. 
