# **Breaking into LOFT** (*loft*)

> **Attenzione**: Questo task ha un tempo limite di 10 minuti per l'invio della soluzione. Una volta richiesto un input, il timer partirà in automatico, e dopo la scadenza non sarà più possibile inviare una soluzione per quell'input.
> *È sempre possibile richiedere un nuovo input*, per cui non preoccuparti se il timer scade: dovrai semplicemente richiedere e scaricare un nuovo input.

Dopo una lunga giornata trascorsa tra lezioni e call di dipartimento, il Professor Martino decide di riposarsi un po' registrando un pezzo inedito con la sua chitarra, e per fare ciò sale al LOFT (Laboratory Of Fabulous Things), il laboratorio polifunzionale più moderno e tecnologico della LUISS, gestito dal Professor Marco Iecher.

Tuttavia, una volta scalati gli interminabili **sei piani di scale** per arrivare al LOFT, scopre che è impossibile accedervi poiché all'interno sono contenute le soluzioni del contest finale del nostro Corso. Per aprire la porta è infatti necessario inserire un codice che solamente il Professor Laura conosce.

Dopo svariati tentativi, il Professor Martino riesce ad accedere alle registrazioni della telecamera di sicurezza che si trova all'interno dell'ufficio del Professor Laura, ma scopre un problema che sperava di non incontrare: le telecamere riprendono solo i movimenti sulla tastiera del Professore e non lo schermo. Quindi, per ottenere il codice di sblocco, il Professor Martino deve creare un programma che prenda in input una stringa composta da numeri e comandi di spostamento del cursore (freccette direzionali).

Il programma deve essere in grado di decodificare i movimenti del cursore, rappresentati dalle direzioni sinistra ${<}$, destra ${>}$, su "^", giù "_", e inserire i numeri corrispondenti nella matrice (una lista di liste). Solo così il Professor Martino potrà ottenere il codice di sblocco per il Luiss LOFT e potrà registrare il suo nuovo inedito.

N.B. 
Quando il cursore viene mosso alla riga (lista) dopo o a quella prima, verrà posizionato dopo l'ultimo elemento della lista.

![hacker](hacker.jpg)

*Aiutalo a ricostruire il testo digitato!*

---
## Dati di input

La prima riga del file di input contiene un intero $T$, il numero di casi di test. Seguono $T$ casi di test, numerati da $1$ a $T$. Ogni caso di test è preceduto da una riga vuota.

Ciascun caso di test è composto da 1 riga contenente una sequenza di lettere, underscore e comandi \{<\} (sinistra), \{>\} (destra), \{^\} (su), \{_\} (giù).

> _Si tenga presente che un comando  \{>\} (destra) alla fine della sequenza non ha effetto e un comando \{<\} (sinistra) all'inizio della sequenza non ha effetto, stesso vale per un comando \{^\} (su) sulla prima sequenza (quella "sopra") (aggiunti esempi sotto*)._

## Dati di output

Il file di output deve contenere la risposta ai casi di test che sei riuscito a risolvere. Per ogni caso di test che hai risolto, il file di output deve contenere tante righe quante le liste (o righe della matrice) di codice con la dicitura

```
Case #t: x
```

dove `t` è il numero del caso di test (a partire da $1$) e `x` è la sequenza di lettere (a-z) o underscore ricostruita. 

## Assunzioni

- le sequenze in input sono lunghe al più 25,000,000 caratteri
- $1 \le T \le 25$.


## Esempi di input/output


**Input:**

```

"1{_}{_}89{<}{<}7{^}5{<}4{>}{>}6{^}23"

```


**Output:**

```
Case #1: [[123],[456],[789]]
```

---

## Spiegazione

Analizziamo passo per passo la stringa di input "1{_}{_}89{<}{<}7{^}5{<}4{>}{>}6{^}23" e come essa viene tradotta nella matrice desiderata:

Iniziamo con una matrice vuota e indichiamo con una sbarra la posizione del cursore: "|".
```
[|]
```
Il primo comando "1" inserisce il numero 1 nella matrice e sposta il cursore a destra:
```
[1|]
```
I seguenti due comandi ({_}{_}) spostano il cursore di due posizioni in giù, creando due nuove righe vuote:
```
riga 1: [1]
riga 2: []
riga 3: [|]
```
I seguenti due comandi (89) inseriscono i numeri 8 e 9 nella riga corrente e spostano il cursore a destra:
```
riga 1: [1]
riga 2: []
riga 3: [89|]
```
I seguenti due comandi ({<}{<}) spostano il cursore di due posizioni a sinistra:
```
riga 1: [1]
riga 2: []
riga 3: [|89]
```
Il seguente comando (7) inserisce il numero 7 nella riga corrente e sposta il cursore a destra:
```
riga 1: [1]
riga 2: []
riga 3: [7|89]
```
Il seguente comando ({^}) sposta il cursore di una posizione in su:
```
riga 1: [1]
riga 2: [|]
riga 3: [789]
```
Il seguente comando (5) inserisce il numero 5 nella riga corrente e sposta il cursore a destra:
```
riga 1: [1]
riga 2: [5|]
riga 3: [789]
```
Il seguente comando ({<}) sposta il cursore di una posizione a sinistra:
```
riga 1: [1]
riga 2: [|5]
riga 3: [789]
```
Il seguente comando (4) inserisce il numero 4 nella riga corrente e sposta il cursore a destra:
```
riga 1: [1]
riga 2: [4|5]
riga 3: [789]
```
Il seguente comando ({>}) sposta il cursore di una posizione a destra:
```
riga 1: [1]
riga 2: [45|]
riga 3: [789]
```
Il seguente comando ({>}) sposta il cursore di una posizione a destra, ma poiché si trova già all'estremo, non succede nulla:
```
riga 1: [1]
riga 2: [45|]
riga 3: [789]
```
Il seguente comando (6) inserisce il numero 4 nella riga corrente e sposta il cursore a destra:
```
riga 1: [1]
riga 2: [456|]
riga 3: [789]
```
Il seguente comando ({^}) sposta il cursore di una posizione in su:
```
riga 1: [1|]
riga 2: [456]
riga 3: [789]
```
I seguenti due comandi (23) inseriscono i numeri 2 e 3 nella riga corrente e spostano il cursore a destra, completando la matrice:
```
riga 1: [123|]
riga 2: [456]
riga 3: [789]
```
Attraverso questa sequenza di comandi, il programma riesce a decodificare i movimenti del cursore e a inserire i numeri appropriati nella matrice.

## * Altri esempi:
### Input:
```
"{<}{<}{<}{<}"
"{>}{>}{>}{>}"
"{_}6"
```
### Output:
```
[]
[]
[[], [6]]
```

