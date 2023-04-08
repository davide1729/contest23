## Descrizione del problema

Marco deve sistemare $n$ computer al LOFT Luiss. I computer saranno disposti in una sola fila, dal numero $1$ al numero $N$, da sinistra a destra. L'$i$-esimo computer è nella posizione $x_i$.

Purtroppo per Marco, solamente alcuni computer sono in corrispondenza di prese di corrente (in effetti Marco, sagace come sempre, si è assicurato di mettere un computer davanti a ogni presa di corrente disponibile).

Per gli altri computer la soluzione è quella di costruire delle prolunghe opportune che possano portare la corrente. Marco come al solito tiene molto all'ordine del LOFT e decide di minimizzare la lunghezza dei cavi necessari a portare la corrente a tutti i computer.

Ogni prolunga può partire da un computer dove è presente una presa di corrente e termina su un computer dove non è presente una presa di corrente. Non è possibile _concatenare_ le prolunghe per collegare i computer intermedi (se una prolunga attraversa un computer sprovvisto di corrente ma non vi termina il computer _NON_ può considerarsi collegato).

![Luiss_loft](loft1.jpg)

Riuscite ad aiutare Marco a capire quale sia la **lunghezza minima complessiva** dei cavi necessari a portare la corrente a tutti i computer?


## Dati di input

La prima riga del file di input contiene un intero $T$, il numero di casi di
test. Seguono $T$ casi di test.

Ciascun caso di test è composto da $3$ righe: la prima contiene un numero 
intero $n$, il numero di computer.
La seconda riga contiene una stringa di lunghezza $n$ che contiene solo `0` o `1`. Se l'$i$-esimo carattere della stringa è un `1`, allora l'$i$-esimo computer ha la presa di corrente; se l'$i$-esimo carattera della stringa è uno `0`, allora l'$i$-esimo computer non ha la presa di corrente.
La terza riga contiene $n$ interi (separati da uno spazio): l'$i$-esimo intero rappresenta la posizione $x_i$ dell'$i$-esimo computer.

## Dati di output

Il file di output deve contenere la risposta ai casi di test che sei riuscito a risolvere. Per ogni caso di test che hai risolto, il file di output deve contenere una riga con la dicitura

```
Case #t: L
```

dove `t` è il numero del caso di test (a partire da $1$) e `L` è un solo numero intero: la **lunghezza minima complessiva** dei cavi necessari per portare la corrente a tutti i computer.  


## Assunzioni

- $1 \le T \le 80$.
- $1 \le N \le 2\,000$.
- $1 \le x_i \le 200\,000$ per ogni $i$.

## Esempi di input/output

**Input:**

```
4
2
01
1 2
3
100
1 5 6
3
101
1 5 6
4
1010
1 2 5 7
```

---

**Output:**

```
Case #1: 1
Case #2: 9
Case #3: 1
Case #4: 3
```

## Spiegazione

Nel **primo caso d'esempio** sono presenti $2$ computer, nelle posizioni $1$ e $2$, di cui uno ha la presa di corrente. In questo caso basta un cavo che li colleghi, di lunghezza $2-1=1$.

Nel **secondo caso d'esempio** sono presenti $3$ computer, nelle posizioni $1$, $5$ e $6$. Solo il primo computer ha la presa di corrente, quindi serve un cavo dal terzo al primo, e uno dal secondo al primo, di lunghezza complessiva $6-1+5-1=9$.

Nel **terzo caso d'esempio** sono presenti $3$ computer, nelle posizioni $1$, $5$ e $6$. Il primo e il terzo computer hanno la presa di corrente, quindi serve solo collegare il secondo computer e la scelta più conveniente è farlo con il terzo: serve quindi un cavo dal terzo al secondo, di lunghezza complessiva $6-5=1$.

Nel **quarto caso d'esempio** sono presenti $4$ computer, nelle posizioni $1$, $2$, $5$ e $7$. Il primo e il terzo computer hanno la presa di corrente. La soluzione ottima è quella di collegare il primo al secondo computer (cavo di lunghezza $2-1=1$) e il terzo al quarto (cavo di lunghezza $7-5=2$). La lunghezza minima necessaria è la somma delle lunghezze dei due cavi, quindi $1+2=3$.

