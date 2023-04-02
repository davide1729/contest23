
# Martino Nucleare (*nukelessio*)

## Descrizione del problema

In un universo parallelo al nostro, il malvagio Professor Alessio Martino, ha sviluppato un piano per far diventare la LUISS Guido Carli l'eccellenza assoluta tra le università italiane. Utilizzando le sue abilità di programmazione e hacking, ha accesso alle telecamere dell'ufficio della Ministra della Difesa, Irene Finocchi, e scopre i codici di lancio criptati di alcuni ordigni carichi di un gas che riduce il quoziente intellettivo di chiunque li respiri. Il professore malvagio ha quindi l'idea di utilizzare questi ordigni per colpire le principali università d'Italia, in modo da garantire la supremazia della LUISS Guido Carli.

Il Professor Martino deve creare un programma che prenda in input una stringa di comandi di spostamento del cursore e numeri, rappresentati dalle direzioni sinistra $L$, destra $R$, su $U$, giù $D$, e inserire i numeri corrispondenti nella matrice. Solo così potrà ottenere i codici di lancio per i suoi ordigni e portare avanti il suo piano malvagio di assicurare la supremazia della LUISS Guido Carli sul panorama universitario italiano.


![hacker](hacker.jpg)

*Aiutalo a ricostruire il testo digitato!*

---
## Dati di input

La prima riga del file di input contiene un intero $T$, il numero di casi di test. Seguono $T$ casi di test, numerati da $1$ a $T$. Ogni caso di test è preceduto da una riga vuota.

Ciascun caso di test è composto da 1 riga contenente una sequenza di lettere, underscore e comandi \[L\] (sinistra), \[R\] (destra), \[U\] (su), \[D\] (giù).

> _Si tenga presente che un comando  \[R\] (destra) alla fine della sequenza non ha effetto e un comando \[L\] (sinistra) all'inizio della sequenza non ha effetto, stesso vale per un comando \[U\] (su) sulla prima sequenza (quella "sopra") e \[D\] (giù) sull'ultima sequenza (quella "sotto")._

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

1[D][D]89[L][L]7[U]5[L]4[R][R]6[U]23

```


**Output:**

```
Case #1: [123]
         [456]
         [789]
```

---

## Spiegazione

Analizziamo passo per passo la stringa di input "1[D][D]89[L][L]7[U]5[L]4[R]6[U]23" e come essa viene tradotta nella matrice desiderata:

Iniziamo con una matrice vuota e indichiamo con una sbarra la posizione del cursore: "|".
```
[|]
```
Il primo comando "1" inserisce il numero 1 nella matrice e sposta il cursore a destra:
```
[1|]
```
I seguenti due comandi (\[D\] \[D\]) spostano il cursore di due posizioni in giù, creando due nuove righe vuote:
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
I seguenti due comandi ([L][L]) spostano il cursore di due posizioni a sinistra:
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
Il seguente comando ([U]) sposta il cursore di una posizione in su:
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
Il seguente comando ([L]) sposta il cursore di una posizione a sinistra:
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
Il seguente comando ([R]) sposta il cursore di una posizione a destra:
```
riga 1: [1]
riga 2: [45|]
riga 3: [789]
```
Il seguente comando ([R]) sposta il cursore di una posizione a destra, ma poiché si trova già all'estremo, non succede nulla:
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
Il seguente comando ([U]) sposta il cursore di una posizione in su:
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

