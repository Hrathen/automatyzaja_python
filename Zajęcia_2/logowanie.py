activated = input("Czy masz aktywne konto? (Tak/Nie): ").lower() == "tak"
loggedin = input("Czy jesteś zalogowany? (Tak/Nie): ").lower() == "tak"
policy_accepted = input("Czy zaakceptowałeś regulamin? (Tak/Nie): ").lower() == "tak"
access = activated and loggedin and policy_accepted
print("Czy ma dostęp?", access)