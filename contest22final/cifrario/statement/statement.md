# Café Cypher (*cifrario*)

Il Cifrario di Cesare, impiegato nel campo della crittografia, è un algoritmo che si compone di una serie di step sistematici mirati a rendere oscuro, ovvero semanticamente non leggibile, il testo di un messaggio. In particolare, il cifrario in questione sposta ciascuna lettera del messaggio di un numero fisso di posizioni lungo l'alfabeto (shifting). Per esempio, se lo spostamento è 1, allora a -> b e b -> c. Se lo spostamento è 2, allora a -> c e b -> d. Tuttavia, se il cifrario fosse così semplice, il nemico potrebbe scoprire il meccanismo di shifting che regola l'algoritmo e, quindi, decifrare il messaggio senza problemi. Di conseguenza, è fondamentale assicurarsi che, verificata una condizione, il meccanismo di shifting cambi. 

Nel campus LUISS di Viale Romania si trova il Language Café, un luogo nel quale è vietato parlare la propria lingua madre per favorire lo scambio linguistico internazionale. Il prof. Martino ha pensato di utilizzare un cifrario per scoraggiare l'utilizzo della macchina del caffè, sempre affollata, ponendo sul muro dei Post-it del Café una password giornaliera e la chiave per lo shifting.
Davide e Demetrio, tuttavia, hanno trovato un modo per avere un vantaggio sui loro compagni di università: pertanto hanno suggerito al prof. Martino di complicare la password apportando qualche modifica al Cifrario di Cesare. In particolare, l'algoritmo che regola lo shifting dovrà funzionare come spiegato di seguito.

![Particolare del LUISS Language Café](language.webp)  
*Particolare del LUISS Language Café*

Innanzitutto, viene fornito il numero di casi di test $T$.
Successivamente, viene fornita la lunghezza $N$ della stringa di input $S$. Accanto a $N$, troverai il numero di chiavi $K$ del Cifrario: ciascuna chiave è il fattore di shifting, dunque ti indica di quante lettere dell'alfabeto la lettera della stringa verrà shiftata. Ma quali lettere bisogna shiftare? 

In un'altra riga troverai la stringa di input $S$. Nella successiva riga troverai le $K$ chiavi (per convenzione chiamiamo ogni singola chiave $k$). Infine, in un'ultima riga troverai una serie di interi, chiamati $c$, ciascuno rappresentante il numero di caratteri che verrà shiftato da ogni chiave. Segue intuitivamente che il numero di chiavi $K$ è uguale al numero di interi che trovi nell'ultima riga. 

Una volta terminati i caratteri da shiftare nella stringa, bisogna riapplicare lo shifting in maniera ciclica, fino a ottenere una stringa completamente cifrata.
Ti proponiamo un esempio esplicativo:

## Esempio esplicativo
**Input:**

```
1

5 3
abcde
0 2 1
1 1 2
```
Ovvero:
- 1 (numero di casi di test)
- 5 (lunghezza della stringa)    3 (numero di chiavi)
- abcde (stringa di input)
- 0 2 1 (3 chiavi: si tratta di 3 fattori di shifting)
- 1 1 2 (numero di caratteri che ogni chiave shifta)

---

**Output:**

```
Case #1: addee
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