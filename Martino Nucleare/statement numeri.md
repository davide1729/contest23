
# Martino Nucleare (*nukelessio*)

## Descrizione del problema

Dopo una lunga giornata trascorsa tra lezioni e call di dipartimento, il Professor Martino decide di riposarsi un po' registrando un pezzo inedito con la sua chitarra, e per fare ciò sale al Loft, rispettivamente il laboratorio più moderno e tecnologico della LUISS, gestito dal Professor Marco Iecher.

Tuttavia, una volta scalati gli interminabili **sei piani di scale** per arrivare al Loft, scopre che è impossibile accedervi poiché all'interno sono contenute le soluzioni del contest finale del Corso di preparazione alle Olimpiadi Italiane di Informatica. Per aprire la porta è infatti necessario inserire un codice che solamente la Professoressa Finocchi conosce, essendo la Direttrice del Corso di Laurea Triennale in Management and Computer Science.

Dopo svariati tentativi, il Professor Martino riesce ad accedere alle registrazioni della telecamera di sicurezza che si trova all'interno dell'ufficio della Professoressa Finocchi, ma scopre un problema che sperava di non incontrare: le telecamere riprendono solo i movimenti sulla tastiera della Professoressa e non lo schermo. Quindi, per ottenere i codici di lancio, il Professor Martino deve creare un programma che prenda in input una stringa composta da numeri e comandi di spostamento del cursore (freccette direzionali).

Il programma deve essere in grado di decodificare i movimenti del cursore, rappresentati dalle direzioni sinistra ${1}$, destra ${2}$, su ${3}$, giù ${4}$, e inserire i numeri corrispondenti nella matrice (una lista di liste). Solo così il Professor Martino potrà ottenere il codice di sblocco per il Luiss Loft e potrà registrare il suo nuovo inedito.


![hacker](hacker.jpg)

*Aiutalo a ricostruire il testo digitato!*

---
## Dati di input

La prima riga del file di input contiene un intero $T$, il numero di casi di test. Seguono $T$ casi di test, numerati da $1$ a $T$. Ogni caso di test è preceduto da una riga vuota.

Ciascun caso di test è composto da 1 riga contenente una sequenza di lettere, underscore e comandi \{1\} (sinistra), \{2\} (destra), \{3\} (su), \{4\} (giù).

> _Si tenga presente che un comando  \{2\} (destra) alla fine della sequenza non ha effetto e un comando \{1\} (sinistra) all'inizio della sequenza non ha effetto, stesso vale per un comando \{3\} (su) sulla prima sequenza (quella "sopra") e \{4\} (giù) sull'ultima sequenza (quella "sotto")._

## Dati di output

Il file di output deve contenere la risposta ai casi di test che sei riuscito a risolvere. Per ogni caso di test che hai risolto, il file di output deve contenere tante righe quante le liste (o righe della matrice) di codice con la dicitura

```
Case #t: x
```

dove `t` è il numero del caso di test (a partire da $1$) e `x` è la sequenza di lettere (a-z) o underscore ricostruita. 

## Assunzioni

- le sequenze in input sono lunghe al più 25,000,000 caratteri
- $1 \le T \le 10$.


## Esempi di input/output


**Input:**

```

"1{4}{4}89{1}{1}7{3}5{1}4{2}{2}6{3}23"

```


**Output:**

```
Case #1: [123]
         [456]
         [789]
```

---

## Spiegazione

Analizziamo passo per passo la stringa di input "1{4}{4}89{1}{1}7{3}5{1}4{2}{2}6{3}23" e come essa viene tradotta nella matrice desiderata:

Iniziamo con una matrice vuota e indichiamo con una sbarra la posizione del cursore: "|".
```
[|]
```
Il primo comando "1" inserisce il numero 1 nella matrice e sposta il cursore a destra:
```
[1|]
```
I seguenti due comandi ({4}{4}) spostano il cursore di due posizioni in giù, creando due nuove righe vuote:
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
I seguenti due comandi ({1}{1}) spostano il cursore di due posizioni a sinistra:
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
Il seguente comando ({3}) sposta il cursore di una posizione in su:
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
Il seguente comando ({1}) sposta il cursore di una posizione a sinistra:
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
Il seguente comando ({2}) sposta il cursore di una posizione a destra:
```
riga 1: [1]
riga 2: [45|]
riga 3: [789]
```
Il seguente comando ({2}) sposta il cursore di una posizione a destra, ma poiché si trova già all'estremo, non succede nulla:
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
Il seguente comando ({3}) sposta il cursore di una posizione in su:
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

