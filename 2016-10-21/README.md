# Workshop_02

[Immagine di ispirazione](http://www.ingegnerianet.it/esempi/edificio-ghersi/edificio-ghersi-big.png)

Questo è il modello a cui mi sono ispirata. Per l'implementazione di questo workshop mi sono appoggiata al workshop01 per creare la facciata e replicarla in modo da ottenere una struttura composta da più telai. 
Ho successivamente sviluppato un metodo (traslaPalazzo) per traslare la struttura in modo da ottenere un palazzo alto e largo a piacimento. 
Il file csv è composto da 4 righe, una per ogni elemento (trave o pilastro); è possibile ingrandire la struttura aggiungendo delle righe.
I campi di ogni riga sono separati da ';' e gli elementi delle liste da ','.
Il primo campo rappresenta i 3 assi, e quindi la traslazione dell'elemento descritto dagli altri campi della riga.
Il secondo campo rappresenta la sezione del pilastro (o della trave).
Il terzo campo, nel caso della trave è composto da due 0, nel caso del pilastro contiene la sezione della trave che dovrà appoggiarsi su di esso.
Il quarto campo contiene la distanza dei pilastri ed infine il quinto le altezze di questi.

Le prime due righe del file.csv rappresentano due facciate composte da 2 pilastri l'una, le utlime due righe contengono le travi che collegano le due facciate fra di loro. 