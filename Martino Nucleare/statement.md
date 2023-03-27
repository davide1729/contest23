
# Martino Nucleare (*nukelessio*)

## Descrizione del problema

In un universo alternativo, l'alter ego cattivo del Professor Alessio Martino è impazzito: dopo una notte tormentata da incubi sulla sua promozione di fine anno, decide di escogitare un piano per far diventare la Luiss Guido Carli l'eccellenza assoluta tra le università italiane. Grazie alle sue doti da programmatore e hacker esperto, accede alle telecamere dell'ufficio del Ministro della Difesa Irene Finocchi. 

Durante una lunga notte di sorveglianza, riesce ad entrare in possesso dei codici di lancio criptati, così da lanciare sui principali atenei d'Italia delle bombe contenenti un gas che dimezza il quoziente intellettivo di chiunque lo respiri. 

C'è però un problema!!!  Le telecamere riprendono la tastiera del Ministro, ma per ovviare a questo, mentre inserisce i codici può spostare il cursore in quattro possibili posizioni: sinistra $[L]$, destra $[R]$, su $[U]$, giù $[D]$, oppure cancellare il carattere con $[C]$.

Se vuole riuscire nella sua impresa, il Professor Martino deve scrivere un codice che ritorni i codici di lancio in una matrice (lista di liste).



![hacker](hacker.jpg)

Aiutalo a ricostruire il testo digitato!

## Dati di input

La prima riga del file di input contiene un intero $T$, il numero di casi di test. Seguono $T$ casi di test, numerati da $1$ a $T$. Ogni caso di test è preceduto da una riga vuota.

Ciascun caso di test è composto da 1 riga contenente una sequenza di lettere, underscore e comandi \[L\], \[R\], \[U\], \[D\] oppure \[C\].

> _Si tenga presente che un comando \[R\] alla fine della sequenza non ha effetto e un comando \[L\] o \[C\] all'inizio della sequenza non ha effetto, stesso vale per un comando \[U\] sulla prima sequenza (quella "sopra") mentre \[D\] sull'ultima (quella "sotto") ._

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

[1 2 3]
[4 5 6]
[7 8 9]



1[D][D]89[L][L]7[U]5[L]4[R]["R"]6[U]23
=
[123]
[456]
[789]

```


**Output:**

```
Case #1: [123]
         [456]
         [789]
```

---

## Spiegazione

- partiamo da una sequenza vuota e indichiamo con una sbarra la posizione del cursore: "|". Il primo comando \[C\] non ha alcun effetto in quanto il cursore è all'inizio della sequenza. 
- i seguenti due comandi (nc) inseriscono due lettere e portano la sequenza nello stato "nc|"
- i seguenti due comandi (\[L\]\[L\]) spostano il cursore di due posizioni a sinistra: "|nc"
- i seguenti due comandi (cb) inseriscono due lettere e portano la sequenza nello stato "cb|nc"
- il seguente comando è una cancellazione \[C\] e porta la sequenza nello stato "c|nc". Dopodichè, "a" viene inserita: "ca|nc"
- i seguenti due comandi (\[R\]\[R\]) spostano il cursore di due posizioni a destra: "canc|"
- i seguenti due comandi (la) inseriscono due lettere e portano la sequenza nello stato "cancla|"
- i seguenti due comandi (\[L\]\[L\]) spostano il cursore di due posizioni a sinistra: "canc|la"
- i seguenti due comandi (el) inseriscono due lettere e portano la sequenza nello stato "cancel|la"
- i seguenti tre comandi (\[R\]\[R\]\[R\]) spostano il cursore di tre posizioni a destra: "cancella|". Si noti che il terzo spostamento non ha effetto in quanto eravamo già giunti alla fine della sequenza.
- i seguenti quattro comandi (_les) inseriscono quattro lettere e portano la sequenza nello stato "cancella_les|"
- i seguenti tre comandi (\[L\]\[L\]\[L\]) spostano il cursore di tre posizioni a simistra: "cancella_|les". 
- infine, gli ultimi due comandi (fi) inseriscono due lettere e portano la sequenza nello stato "cancella_fi|les"


