# Laboratoare SR

### Laborator 1
Dataset-ul ales a fost preluat de pe Kaggle si contine informatii despre cele mai bine vandute carti - titlu, autor, limba, data publicarii, vanzari aproximative (in Milioane) si gen. Din aceste proprietati am ales sa extrag titlul, genul, autorul si numarul de vanzari si le-am adaugat ca proprietati in Recombee, extragand apoi toate cartile si inserandu-le in baza de date. 

### Laborator 2
Pentru acest laborator am extras utilizatorii din fisierul people.csv (continand numele, id-ul, echipa si locatia fiecarui utilizator). Am preluat aceste proprietati si am creat o functie ajutatoare care genereaza o adresa de mail in functie de numele (si compania, daca este cazul) fiecarei persoane. Am folosit apoi aceasta functie pentru a adauga adresa de mail ca o proprietate suplimentara a utilizatorilor. Toate datele au fost apoi trimise in Recombee.

### Laborator 4
Cele mai similare produse identificate:
1. Unibond Sealant Re-New
2. Unibond Sealant Re-New
Scor Cosine Similarity: 1.0000

Cele doua produse au un scor mare deoarece descrierile lor impartasesc multi termeni specifici (cuvinte cheie), 
indicand ca fac parte din aceeasi categorie sau gama de produse.

### Laborator 5
Pentru acest laborator, am implementat algoritmul Item-Based Collaborative Filtering. Deoarece setul de date inițial nu conținea istoricul acțiunilor, am generat o serie de interacțiuni simulate (rating-uri de la 1 la 5) între utilizatorii și cărțile importate anterior. Pe baza acestor date, am construit matricea User-Item și am calculat matricea de similaritate dintre cărți folosind Cosinus Similarity. În final, am creat logica de recomandare care prezice scorul unui utilizator pentru o carte necitită, calculând o medie ponderată a rating-urilor date de acesta itemilor similari din istoric.

Rezultate recomandari pentru userul SP01:

1. Dune | Scor estimat: 5.0
2. Where the Crawdads Sing | Scor estimat: 5.0
3. Becoming | Scor estimat: 5.0
4. Ronia, the Robber's Daughter | Scor estimat: 5.0
5. The Cat in the Hat | Scor estimat: 5.0

Observatie:
Scorurile sunt estimate pe baza mediei ponderate a rating-urilor date de user cartilor similare. 
Deoarece datele sunt generate aleatoriu, este posibil ca unele carti sa aiba similaritate doar cu cartile de 5 stele ale userului, rezultand o predictie perfecta de 5.0.