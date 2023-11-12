#Kalkulator Walutowy
#Napisz prosty skrypt w Pythonie, który będzie działał jako kalkulator walutowy.
#Skrypt powinien:
#1. Poprosić użytkownika o wprowadzenie kwoty w złotówkach (PLN).
#2. Poprosić użytkownika o wybór waluty, na którą chce wymienić złotówki (USD, EUR, GBP).
#. Poprosić użytkownika o wprowadzenie aktualnego kursu wymiany złotówki na wybraną walutę.
#4. Obliczyć, ile użytkownik otrzyma waluty po wymianie.
#5. Wyświetlić wynik w formacie: "Za [kwota] PLN otrzymasz [wynik] [waluta].", gdzie wynik powinien być zaokrąglony do dwóch
#miejsc po przecinku.
#6. Poprosić użytkownika o wpisanie swojego imienia.
#7. Wyświetlić personalizowane powitanie wraz z wynikiem wymiany:
#"Witaj [imię]! Za [kwota] PLN otrzymasz [wynik] [waluta]."

amount = float(input("Podaj kwotę w PLN ->"))
currency = input('Wybierz walutę: USD, EUR, GBP ->').upper()
exchange_rate =float(input(f'Aktualny kurs waluty PLN na {currency}:  '))

result = amount * exchange_rate
result = round(result, 2)

print(f'Za {amount} PLN otrzymasz {result} {currency}.')

name = input("Podaj swoje imię ->").capitalize()
print(f"Witaj, {name}! Za  ")


#print(amount * 4)
