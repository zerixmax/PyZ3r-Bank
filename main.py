# ░█▀█░█░█░▀▀█░▀▀█░█▀▄  
# ░█▀▀░░█░░▄▀░░░▀▄░█▀▄  
# ░▀░░░░▀░░▀▀▀░▀▀░░▀░▀
#region Imports
import os   
import sys
from datetime import datetime
#endregion

#region Init Data
company = {
    'id': 1,
    'name': 'PyZer j.d.o.o.',
    'tax_id': '12345678901',
    'hq': {
        'address': 'Ulica 19',
        'city': 'Vela Luka',
        'postal_code': '20270',
        'country': 'Croatia',
        'email': 'info@pyzer.hr'
    }
}

bank = {
    'id': 1,
    'name': 'Zagrebačka banka',
    'address': 'Trg bana Josipa Jelačića 1',
    'city': 'Zagreb',
    'postal_code': '10000',
    'country': 'Croatia',
    'email': 'info@zb.hr'
}   

currency = {
    'id': 1,
    'name': 'Euro',
    'symbol': 'EUR',
    'code': 'EUR'       
}

MIN_DEPOSIT = 500.00

transaction = []

bank_accounts = []
#endregion

#region Functions
def clear_screen():
    """Očisti ekran konzole."""
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter():
    """Čekaj na unos korisnika."""
    input("\nPritisnite Enter za nastavak...")

#endregion

#region New Account
def create_account():
    """Kreiraj novi bankovni račun."""
    global bank_accounts
    clear_screen()
    print("Kreiranje novog bankovnog računa")
    print("------------------------------\n")
    
    iban = input("Unesite IBAN: ").strip()

    #Unos minimalnog depozita
    while True:
        try:
            deposit = float(input(f"Unesite početni depozit (minimalno {MIN_DEPOSIT:.2f} {currency['code']}): ").strip())
        except ValueError:
            print("Neispravan unos. Molimo unesite brojčanu vrijednost.")
            continue

        if deposit < MIN_DEPOSIT:
            print(f"Početni depozit mora biti najmanje {MIN_DEPOSIT:.2f} {currency['code']}. Pokušajte ponovo.")
        else:
            break
        
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_account = {
        'id': len(bank_accounts) + 1,
        'company': company['name'],
        'iban': iban,
        'bank': bank,
        'balance': deposit,
        'currency': currency['code'],
        'created_at': today,
        'transactions': [],
        'owner': company
    }
    # Dodaj početni depozit kao transakciju
    add_transaction(new_account, 'deposit', deposit, today, "Početni depozit")
    bank_accounts.append(new_account)
    print("\nNovi bankovni račun uspješno je kreiran.")
    press_enter()
#endregion
#region Transactions
def add_transaction(account, t_type, amount, t_date, description=""):
    """Dodaj transakciju u bankovni račun."""
    txn = {
        'type': t_type,
        'amount': amount,
        'date': t_date,
        'description': description
    }
    account['transactions'].append(txn)
#endregion

#region Show Account Details
def show_account_details(bank_account):
    """Prikaži detalje bankovnog računa."""
    clear_screen()
    print("Detalji bankovnog računa")
    print("-----------------------\n")
    if bank_account:
        print(f"IBAN: {bank_account['iban']}")
        print(f"Vlasnik računa: {bank_account['company']}")
        print(f"Banka: {bank_account['bank']['name']}")
        print(f"Stanje računa: {bank_account['balance']:.2f} {bank_account['currency']}")
        print(f"Datum kreiranja: {bank_account['created_at']}")
    else:
        print("Nema kreiranog bankovnog računa.")
    press_enter()

#endregion
#region Acount transactions
def show_transactions(bank_account):
    """prikaži transakcije bankovnog računa."""    
    clear_screen()
    print("Transakcije bankovnog računa")
    print("---------------------------\n")
    if bank_account and bank_account['transactions']:
        for idx, txn in enumerate(bank_account['transactions'], 1): # type: ignore
            znak = "+" if txn['type'] == "deposit" else "-"
            opis = txn['description'] if txn.get('description') else ""
            print(f"{idx}. {txn['date']} | {txn['type'].upper()} | {znak}{txn['amount']:.2f} {bank_account['currency']} | {opis}")
    else:
        print("Nema zabilježenih transakcija.")
    press_enter()
#endregion
#region Deposit
def deposit(bank_account):
    """Uplata na bankovni račun."""
    clear_screen()
    print("Uplata na bankovni račun")
    print("-----------------------\n")
    
    while True:
        try:
            amount_str = input(f"Unesite iznos uplate (minimalno {MIN_DEPOSIT:.2f} {currency['code']}): ").strip()
            if not amount_str: # Ako je unos prazan
                print("Unos ne može biti prazan.")
                continue
            amount = float(amount_str)
            break
        except ValueError:
            print("Neispravan iznos. Pokušajte ponovo.")

    if amount < MIN_DEPOSIT:
        print(f"Iznos uplate mora biti najmanje {MIN_DEPOSIT:.2f} {currency['code']}. Uplata nije izvršena.")
        press_enter()
        return

    description = input("Unesite opis uplate: ").strip()
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bank_account['balance'] += amount
    add_transaction(bank_account, 'deposit', amount, today, description)  
    print(f"\nUplata od {amount:.2f} {currency['code']} uspješno izvršena.")
    print(f"Novo stanje računa: {bank_account['balance']:.2f} {bank_account['currency']}")
    press_enter()
#endregion
#region Withdraw
def withdraw(bank_account):
    """Isplata s bankovnog računa."""
    clear_screen()
    print("Isplata s bankovnog računa")
    print("-------------------------\n")
    try:
        amount = float(input("Unesite iznos isplate: ").strip())
    except ValueError:
        print("Neispravan iznos. Pokušajte ponovo.")
        press_enter()
        return
    if amount <= 0:
        print("Iznos isplate mora biti pozitivan. Pokušajte ponovo.")
        press_enter()
        return
    if amount > bank_account['balance']:
        print("Nedovoljno sredstava na računu za ovu isplatu.")
        press_enter()
        return
    description = input("Unesite opis isplate: ").strip()
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bank_account['balance'] -= amount
    add_transaction(bank_account, 'withdraw', amount, today, description)
    print(f"\nIsplata od {amount:.2f} {currency['code']} uspješno izvršena.")
    print(f"Novo stanje računa: {bank_account['balance']:.2f} {bank_account['currency']}")
    press_enter()
#endregion
#region owner info
"""Prikaži informacije o vlasniku računa."""
def show_owner_info(bank_account):
    clear_screen()
    print("Informacije o vlasniku računa")
    print("------------------------------\n")
    if bank_account:
        owner = bank_account['owner']
        print(f"Naziv: {owner['name']}")
        print(f"Porezni ID: {owner['tax_id']}")
        print(f"Adresa: {owner['hq']['address']}, {owner['hq']['postal_code']} {owner['hq']['city']}, {owner['hq']['country']}")
        print(f"Email: {owner['hq']['email']}")
    else:
        print("Nema kreiranog bankovnog računa.")
    press_enter()
#endregion
#region Account Selection
def select_account():
    """Omogućuje korisniku odabir računa za rad."""
    if not bank_accounts:
        print("Nema kreiranih bankovnih računa. Molimo prvo kreirajte račun.")
        press_enter()
        return None

    if len(bank_accounts) == 1:
        return bank_accounts[0]

    while True:
        clear_screen()
        print("Odaberite račun")
        print("----------------\n")
        for account in bank_accounts:
            print(f"{account['id']}. {account['iban']} ({account['balance']:.2f} {account['currency']})")
        
        try:
            choice = input("\nUnesite redni broj računa: ").strip()
            if not choice:
                continue
            choice_id = int(choice)
            
            for account in bank_accounts:
                if account['id'] == choice_id:
                    return account
            
            print("Neispravan odabir. Račun s tim brojem ne postoji.")
            press_enter()
        except ValueError:
            print("Neispravan unos. Molimo unesite broj.")
            press_enter()
#endregion
#region Main Menu
"""Glavni meni aplikacije."""
def main_menu():
    while True:
        clear_screen()
        print("Dobrodošli u Bankovni Sustav")
        print("----------------------------\n")
        print("1. Kreiraj novi bankovni račun")
        print("2. Prikaži detalje bankovnog računa")
        print("3. Prikaži transakcije bankovnog računa")
        print("4. Uplata na bankovni račun")
        print("5. Isplata s bankovnog računa")
        print("6. Prikaži informacije o vlasniku računa")
        print("7. Izlaz iz aplikacije\n")
        
        choice = input("Odaberite opciju (1-7): ").strip()
        
        if choice == '1':
            create_account()
        elif choice == '2':
            selected = select_account()
            if selected:
                show_account_details(selected)
        elif choice == '3':
            selected = select_account()
            if selected:
                show_transactions(selected)
        elif choice == '4':
            selected = select_account()
            if selected:
                deposit(selected)
        elif choice == '5':
            selected = select_account()
            if selected:
                withdraw(selected)
        elif choice == '6':
            selected = select_account()
            if selected:
                show_owner_info(selected)
        elif choice == '7':
            print("Izlaz iz aplikacije. Doviđenja!")
            sys.exit()
        else:
            print("Neispravan odabir. Pokušajte ponovo.")
            press_enter()   
if __name__ == "__main__":
    main_menu()
#endregion
