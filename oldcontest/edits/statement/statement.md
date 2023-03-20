
---

## Descrizione del problema

Durante la notte un malintenzionato è riuscito ad accedere alle sale computer della Luiss e ha digitato diversi comandi su una tastiera! E' fondamentale riuscire a capire esattamente cosa ha scritto, ma purtroppo non ha lasciato tracce... tranne una: la telecamera installata sul soffitto ha registrato tutti i suoi movimenti sulla tastiera (ma non è riuscita ad inquadrare lo schermo). Dal video riusciamo a capire ogni tasto premuto dal malintenzionato; questo include:

- lettere a-z o spazi, indicati con il carattere underscore ("_")
- spostamenti del cursore a destra o sinistra, indicati con \[R\] e \[L\]
- cancellazione del carattere che precede il cursore, indicato con \[C\].

![tastiera](picture.png)

Aiutaci a ricostruire il testo digitato!

## Dati di input

La prima riga del file di input contiene un intero $T$, il numero di casi di test. Seguono $T$ casi di test, numerati da $1$ a $T$. Ogni caso di test è preceduto da una riga vuota.

Ciascun caso di test è composto da 1 riga contenente una sequenza di lettere, underscore e comandi \[L\], \[R\] oppure \[C\].

> _Si tenga presente che un comando \[R\] alla fine della sequenza non ha effetto e un comando \[L\] o \[C\] all'inizio della sequenza non ha effetto._

## Dati di output

Il file di output deve contenere la risposta ai casi di test che sei riuscito a risolvere. Per ogni caso di test che hai risolto, il file di output deve contenere una riga con la dicitura

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
1

[C]nc[L][L]cb[C]a[R][R]la[L][L]el[R][R][R]_les[L][L][L]fi

```


**Output:**

```
Case #1: cancella_files
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


