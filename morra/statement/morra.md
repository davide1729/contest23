# MORRA
Durante una lezione del Professor Martino si è discusso di un gioco non molto noto alla maggior parte degli studenti presenti in aula: **Morra**.

La *morra* è uno dei giochi più antichi e tradizionali, le cui origini risalgono addirittura all'Antico Egitto: in una tomba di un alto dignitario di corte della XXV dinastia, si vede chiaramente il defunto intento a stendere il braccio con un numero, contrapposto ad un altro giocatore.

Si tratta di un gioco semplice ed intuitivo. Due giocatori si sfidano in un numero *n* di round, e in ciascuno di questi round ogni giocatore deve contemporaneamente dire un numero **compreso tra 2 e 10** a voce alta e tirarne un altro con una sola mano. Ciascun giocatore può tirare un numero **compreso tra 0 e 5** (zero sarà rappresentato da un pugno chiuso). Ad aggiudicarsi un round sarà il giocatore il cui numero annunciato a voce alta risulterà uguale alla somma dei numeri lanciati dai due giocatori.
Consideriamo un esempio:
Mauro e Alberto, due studenti di Management and Computer Science, si sfidano a morra. Insieme optano per sfidarsi su 3 round. Nel primo round Mauro annuncia a voce alta il numero 7 e lancia il numero 3. Alberto, invece, annuncia il numero 5 e lancia il numero 2. La somma dei numeri lanciati è **3+2=5**, pertanto Alberto si aggiudica il primo round. Nel secondo round, Mauro annuncia il numero 2 e lancia il numero 1. Alberto annuncia il numero 3 e lancia il numero 1. La somma dei numeri lanciati è **1+1=2**, quindi ad aggiudicarsi il secondo round è Mauro. Nel round decisivo, Mauro annuncia il numero 4 e lancia il numero 0. Alberto annuncia il numero 5 e lancia il numero 4. Essendo la somma dei numeri lanciati **0+4=4**, Mauro si aggiudicherà anche il terzo round (decisivo). Dunque, vincerà la partita Mauro con un punteggio di 2 a 1.

Il Professor Martino, per stimolare gli studenti con la scrittura di codice creativo, ha proposto una variante della tradizionale *morra*. In particolare, nella versione del Professor Martino il gioco non si limita a due soli giocatori, ma si estende ad un numero variabile *m*. Inoltre, ciascun giocatore potrà ora impiegare entrambe le mani e lanciare un numero **compreso tra 0 e 10**, e potrà annunciare a voce un numero **anche maggiore di 10** (sta alla sua furbizia annunciare un numero non troppo grande e che sia rapportato al numero di giocatori). Infine, segue che ad aggiudicarsi il round, anche nella versione del Professor Martino, sarà il giocatore il cui numero annunciato a voce risulterà uguale alla somma dei numeri lanciati dai giocatori.

## Spiegazione
Riceverai come dati di input due numeri, rispettivamente:
- il numero di round *n* (in una prima riga)
- il numero di giocatori *m* (nella riga successiva)

Lascia che ogni giocatore scelga **in maniera randomica** che numeri tirare e che numeri annunciare a voce alta. Ricorda: ogni giocatore giocherà **in ogni round**.

## Assunzioni
Puoi assumere che ci saranno sempre **almeno 2 giocatori** a disputare una partita, quindi *m* >= 2.
Puoi assumere che ci sarà sempre **almeno un round**, quindi *n* >= 1.

## Esempio
### Dati di Input
3
3

### Output
Player0

Come sopra menzionato, nella prima riga di dati di input trovi il numero di round *n*, mentre nella seconda riga trovi il numero di giocatori *m*. Nell'esempio che abbiamo riportato, i due valori *n* e *m* coincidono.

**NOTA BENE:**
- Nell'output dovrai inserire **solamente** i giocatori vincitori. Se si dovesse verificare un ex aequo, dovrai inserire i nomi di tutti i giocatori che hanno ottenuto il massimo punteggio.
- 
- L'output generato dipende dal caso, essendo i numeri annunciati prima, e tirati poi, randomici. Pertanto, non sempre si avrà un vincitore. Infatti, alla fine dei round si potrebbe verificare la situazione in cui nessun giocatore avrà ottenuto dei punti. In questo caso, dovrei generare il seguente output: **None**.




## Casi di Test
