PyBank
Jednostavna proceduralna Python aplikacija za upravljanje poslovnim računom u banci

📋 Opis
PyBank je edukativna konzolna aplikacija koja omogućuje vođenje i nadzor poslovnog bankovnog računa jedne firme.
Svi podaci drže se u rječnicima i listama (bez klasa), a program nudi potpuno tekstualno sučelje s izbornikom.

🚀 Funkcionalnosti
Otvaranje računa s minimalnim pologom

Prikaz IBAN-a, stanja i osnovnih informacija o računu, valuti i banci

Evidencija uplata i isplata uz opis transakcije

Prikaz svih transakcija (uplata/isplata) u povijesti

Prikaz podataka o vlasniku računa

Validacija svih korisničkih unosa (iznos, polog, isplata, IBAN)

Mogućnost jednostavnog proširenja

🗄️ Struktura podataka
company — podaci o firmi (naziv, OIB, adresa, email)

bank — podaci o banci (naziv, adresa)

currency — opis valute (naziv, šifra, simbol)

bank_account — podaci o računu: IBAN, stanje, valuta, banka, povijest transakcija

transactions — lista rječnika (tip, iznos, datum, opis)

⚙️ Tehnička logika
Sve funkcije su proceduralne

Podaci su u rječnicima i listama

Glavna petlja prikazuje izbornik i poziva odgovarajuće funkcije

Nema klasa ni objektne paradigme

Po potrebi se može spremati/podizati podatke u datoteku (JSON)

📑 Kako koristiti
Pokreni aplikaciju:

bash
python pybank.py
Slijedi izbornik:

Prvo kreiraj račun (ako ne postoji)

Odaberi željenu opciju iz glavnog menija

📝 Primjer izbornika
text
=== PY BANK ===
Račun: HR123... | Saldo: 500.00 EUR
1. Prikaz informacija o računu
2. Prikaz svih transakcija
3. Uplata novca
4. Isplata novca
5. Podaci o vlasniku
0. Izlaz
👨‍💻 Primjer transakcije (rječnik)
python
{
    'date': '2025-09-30 09:30:23',
    'amount': 700.00,
    'type': 'UPLATA',      # ili 'ISPLATA'
    'desc': 'Plaćanje usluge'
}
🛠️ Ovisnosti
Python 3.x

Standardne biblioteke: os, datetime

🏁 Namjena
Projekt kreiran u svrhu edukacije i vježbe na tečaju Python Developer Algebra
Praktična vježba proceduralnog programiranja za buduće aplikacije s kompleksnijim poslovnim logikama.

By 

# ░█▀█░█░█░▀▀█░▀▀█░█▀▄  
# ░█▀▀░░█░░▄▀░░░▀▄░█▀▄  
# ░▀░░░░▀░░▀▀▀░▀▀░░▀░▀

Algebra, 2025.
