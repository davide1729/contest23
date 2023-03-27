# PageRank (*pagerank*)

La professoressa Finocchi ha sfidato i tutor: devono riuscire a calcolare quanto sia facile trovare la pagina del Corso di preparazione alle Olimpiadi a partire da vari URL, come quello del sito della LUISS.

La LUISS ha fornito una serie di grafi non orientati che rappresentano i collegamenti tra vari siti web legati all'ateneo – per esempio, sport.luiss.it oppure impresaemanagement.luiss.it – tra cui è sempre presente il suddetto sito del nostro Corso.

Demetrio ha scoperto una cosa: all'interno di questi grafi, il sito più "raggiunto" è proprio quello del Corso. Per questo motivo, ha chiesto a Davide di verificare questa ipotesi tramite l'algoritmo PageRank.

![I tutor nel Loft](1.jpeg)  
*I tutor nel Loft*
---
PageRank ($PR$) assegna un valore numerico a ogni pagina all'interno del World Wide Web che ne quantifica l'importanza o il prestigio relativi all'interno di questa rete. Fu introdotto nel 1998 da Sergey Brin e Larry Page come ingrediente fondamentale di Google.

Nell'algoritmo in questione, bisogna descrivere il comportamento di un utente che naviga nelle reti rappresentate dai grafi forniti in input, cliccando in maniera randomica sui link che collegano le pagine. L'assunzione iniziale è che ogni pagina ha la stessa probabilità iniziale di essere raggiunta, ma le pagine con una centralità maggiore o presenti in aree più dense del grafo saranno quelle più facilmente raggiungibili.

In particolare, si procede come segue:
- ogni nodo viene inizializzato con un valore di $PR$ iniziale $R_0=1/N$, dove $N$ è il numero di nodi del grafo;
- a ogni iterazione $t$, si itera su $N$ nodi $i$ per aggiornare il loro valore di $PR$:
$R_t(i)= \frac \alpha N+(1-\alpha)\sum_{j\in pred(i)} \frac {R_{t-1}(j)} {k_{out}(j)}$ 
    - $\alpha$ rappresenta il **fattore di teletrasporto** o di smorzamento, ossia la probabilità che l'utente interrompa la navigazione e ricominci un nuovo percorso partendo da una nuova pagina randomica.
    - $pred(i)$ è l'insieme dei predecessori $j$ del nodo $i$: ossia l'insieme dei nodi (le pagine) direttamente collegati al nodo $i$.
    - $k_{out}(j)$ rappresenta il numero di collegamenti uscenti dal predecessore $j$, ossia il numero di $pred(j)$, poiché, in un grafo non orientato, $length(pred(i))=k_{in}(i)=k_{out}(i)$.

In parole povere, il $PR$ iniziale di ogni nodo viene aggiornato con ogni iterazione a un valore che dipende dal numero dei collegamenti del nodo, dal numero dei collegamenti dei nodi collegati e così via. In base al coefficiente $\alpha$, il $PR$ convergerà a un valore costante.

---
Aiuta Demetrio e Davide a scoprire la posizione della pagina con il PageRank più alto, altrimenti la professoressa Finocchi troverà presto due nuovi tutor per rimpiazzarli!

---

## Esempio esplicativo
**Input:**

```
5

0  1 3 4
1  0 2 3 4
2  1 4
3  0 1 4
4  0 1 2 3
```
Ovvero:
- 5, il numero di nodi (compresi i nodi isolati)
- 0, ossia il primo nodo, seguito da due spazi dai nodi con cui è connesso: 1, 3 e 4.


---

**Output:**

```
Case #1: 
```

---

Immagina di entrare nel Language Café e trovare, ogni giorno, un post-it contenente un input del genere. Cerca di trovare una soluzione rapida per trovare le password corrette (l'output), prima che Davide e Demetrio prendano d'assalto la macchina del caffè!


## Spiegazione

Ti viene fornita una stringa di lunghezza 5, ovvero "abcde". Hai tre chiavi, ovvero tre fattori di shifting, a cui sono associati 3 interi, ciascuno rappresentante il numero di caratteri soggetti al fattore di shifting associato. Ecco come si ottiene l'output riportato sopra:
- Si comincia con il primo carattere della stringa. Dall'ultima riga dell'input sapiamo che un solo carattere ha fattore di shifting 0, dunque il carattere $a$ non è soggetto a shift.
- Si prosegue iterando nella stringa, è il turno del carattere $b$. Sappiamo dall'ultima riga dell'input che un solo carattere ha fattore di shifting 2, dunque $b$ viene shiftato di 2 e diventa $d$.
- Tocca al terzo carattere della stringa $S$ di input. Sappiamo che due caratteri hanno fattore di shifting 1, quindi il terzo carattere $c$ diventa $d$ ed il quarto carattere $d$ diventa $e$.
- Infine è il turno dell'ultimo carattere della stringa di input: $e$. Visto che abbiamo terminato la sequenza "indice" (nota infatti che 1+1+2 = 4, mentre la lunghezza di $S$ è 5), riportata nell'ultima riga dell'input, la eseguiamo da capo. Pertanto $e$ avrà fattore di shifting 0 e, di conseguenza, non subirà alcuna modifica.
Ecco che otteniamo la stringa di output "addee".

## Dati di Input
Il tuo input sarà dato da:
- Un valore $N$ che rappresenta la lunghezza della stringa, con accanto un numero $K$ di chiavi $k$.
- La stringa di input $S$.
- La sequenza contenente le chiavi ($K$ chiavi in totale).
- La sequenza contenente il numero di caratteri associati ad ogni chiave.

## Assunzioni
- $T$, $N$, e $K$ interi;
- $0 \leq N \leq 10^4$;
- $0 \leq K \leq\ N$;
- $0 \leq k \leq 10^3$;
- $0 \leq c \leq\ N$;
- $S$ non potrà contenere, tuttavia, caratteri speciali. Immagina dunque una stringa di **sole lettere** tra le 26 dell'alfabeto (minuscole e maiuscole).
- La stringa di input non contiene spazi.

## Casi di Test

### Input

```
4

5 2
Luiss
3 1
1 2

9 5
OlimpiADE
3 4 7 2 1
1 3 0 2 1

6 5
CESARE
1 2 1 3 0
1 1 1 2 1

7 3
TheDome
26 3 2
2 3 1
```

### Output

```
Case #1: Ovjvt
Case #2: RpmqrkBGI
Case #3: DGTDUE
Case #4: ThhGroe
```