# Laboratoare SR

### Laborator 1
Dataset-ul ales a fost preluat de pe Kaggle si contine informatii despre cele mai bine vandute carti - titlu, autor, limba, data publicarii, vanzari aproximative (in Milioane) si gen. Din aceste proprietati am ales sa extrag titlul, genul, autorul si numarul de vanzari si le-am adaugat ca proprietati in Recombee, extragand apoi toate cartile si inserandu-le in baza de date. 

### Laborator 2
Pentru acest laborator am extras utilizatorii din fisierul people.csv (continand numele, id-ul, echipa si locatia fiecarui utilizator). Am preluat aceste proprietati si am creat o functie ajutatoare care genereaza o adresa de mail in functie de numele (si compania, daca este cazul) fiecarei persoane. Am folosit apoi aceasta functie pentru a adauga adresa de mail ca o proprietate suplimentara a utilizatorilor. Toate datele au fost apoi trimise in Recombee.

### Laborator 4
Cele mai similare produse identificate:
scor similaritate maxim: 0.9872
Prod 1: Tesco Pink Balloons 15Pk
Prod 2: Tesco Blue Balloons 15Pk
Descriere 1: - Assorted colours - 15 Pack - Material: Latex Add some colour to your celebration with these Pink balloons. Information Warnings Warning! Made of natural rubber latex. Choking hazard - children under...
Descriere 2: - Assorted colours - 15 Pack - Material: Latex Add some colour to your celebration with these Blue balloons. Information Warnings Warning! Made of natural rubber latex. Choking hazard - children under...

Cele doua produse au un scor mare deoarece descrierile lor impartasesc multi termeni specifici (cuvinte cheie), 
indicand ca fac parte din aceeasi categorie sau gama de produse.

### Laborator 5
Matricea User-Item:
                     A Tale of Two Cities  The Little Prince  Harry Potter 1  And Then There Were None  Dream of Red Chamber
Barr Faughny                            5                  0               4                         0                     0
Dennison Crosswaite                     0                  5               0                         3                     0
Gunar Cockshoot                         2                  0               0                         5                     1
Wilone O'Kielt                          0                  4               5                         0                     0
Gigi Bohling                            0                  0               3                         4                     5

Matricea de Similaritate intre Carti:
                          A Tale of Two Cities  The Little Prince  Harry Potter 1  And Then There Were None  Dream of Red Chamber
A Tale of Two Cities                      1.00               0.00            0.53                      0.26                  0.07
The Little Prince                         0.00               1.00            0.44                      0.33                  0.00
Harry Potter 1                            0.53               0.44            1.00                      0.24                  0.42
And Then There Were None                  0.26               0.33            0.24                      1.00                  0.69
Dream of Red Chamber                      0.07               0.00            0.42                      0.69                  1.00

Recomandari pentru Barr Faughny:
- And Then There Were None (Scor: 2.27)
- Dream of Red Chamber (Scor: 2.03)
- The Little Prince (Scor: 1.77)