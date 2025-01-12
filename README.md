a. All’avvio del programma, si crei un grafo semplice, pesato e orientato i cui vertici siano tutti i cromosomi
(tabella genes, colonna chromosome, considerando solo i valori diversi da 0).
b. Un arco collega due cromosomi diversi solo se i due cromosomi contengono due geni (uno per cromosoma) che compaiono
(nello stesso ordine) nella tabella interactions. Si noti che, per ciascun cromosoma, possono esistere più geni, 
e ciascuno di essi potrebbe essere presente più volte (associato a function diverse).
c. Il peso di ciascun arco dovrà essere calcolato come la somma algebrica della correlazione (tabella interactions, 
campo Expression_Corr), facendo attenzione a contare ogni coppia di geni una sola volta. Nell’esempio seguente, 
il peso dell’arco tra il cromosoma 5 ed il cromosoma 11 sarà pari a 2,468455212.
d. Si visualizzi il numero di vertici ed archi del grafo, ed i valori minimo e massimo dei pesi degli archi.
e. Permettere all’utente di inserire un valore soglia (S), verificando che tale valore sia compreso nell’intervallo
minimo-massimo calcolato al punto d.
f. Alla pressione del bottone “Conta archi” stampare il numero di archi il cui peso è <S, ed il numero di archi il
cui peso è >S.
