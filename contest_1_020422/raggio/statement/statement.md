# Raggio Hackerante 

Michele, con la saggia guida del Prof. Martino, ha ideato un `raggio hackerante` in grado di penetrare in ogni dispositivo elettronico che entri nello spazio aereo Luiss.  
Il raggio consuma una notevole quantità di energia, e per funzionare in modo ottimale ha bisogno di una determinata potenza $P$.  
Per fortuna nel campus Luiss di Viale Romania è presente il Vehicle Sharing Luiss Green Mobility, che dispone di una flotta di auto elettriche. Come è risaputo, ciascuna auto elettrica è dotata di una potente batteria agli ioni di litio, e quindi costituisce un'ottima fonte di energia per un apparato energivoro come il `raggio hackerante`.  
Avendo deciso di usare le batterie delle auto per il raggio, Michele ha ora una serie di $N$ batterie, indicizzate da $0$ a $N-1$.  
Ogni batteria eroga una determinata potenza $p_i$. Il raggio può sfruttare un numero arbitrario di batterie, purché formino una sottosequenza continua (la potenza totale in tal caso è la somma delle potenze delle singole batterie). Se la potenza fosse troppo bassa il raggio non sarebbe in grado di hackerare nulla, mentre se fosse troppo alta rischierebbe di friggere la scheda madre. Aiuta Michele a trovare $i$ e $j$  tali che la suddetta sommatoria sia il più vicino possibile a $P$.  

**NOTA: Se ci sono più soluzioni accettabili, puoi fornirne una qualsiasi**

![raggio_hackerante](raggio.webp)  
*Il raggio hackerante*

## Dati di input

La prima riga del file di input contiene un intero $T$: il numero di casi di test. Seguono $T$ casi di test, numerati da $1$ a $T$. Ogni caso di test è preceduto da una riga vuota.

Ciascun caso di test è composto da $2$ righe: la prima contiene due numeri, $N$ e $P$, rispettivamente il numero di batterie disponibili e la potenza ottimale del raggio hackerante.  
La riga seguente contiene le $N$ potenze $p_i$ erogate da ogni batteria, separate da uno spazio.  

## Dati di output

Il file di output deve contenere la risposta ai casi di test che sei riuscito a risolvere.  
Per ogni caso di test che hai risolto, il file di output deve contenere una riga con la dicitura:  

```
Case #t: 
```

dove `t` è il numero del caso di test (a partire da $1$).  
Per ogni caso di test deve essere presente una singola riga con $i$ e $j$ identificate separate da spazio.

## Assunzioni

- $T \leq 50$.
- $N \leq 10^7$.
- $P \leq 10^{12}$.
- $p_i \leq 10^{12}$.
- $0 \leq i \leq j \leq N-1$.

## Esempi di input/output

---

**Input:**

```
3

3 26
93 2 24

6 47
94 80 89 1 45 45

4 5
2 3 5 2

```
---

**Output:**

```
Case #1: 1 2
Case #2: 3 4
Case #3: 0 1
```

---
