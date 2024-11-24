from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional

# Decorator for logging function calls
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper


# First-Class Function: Higher-order function (passing lambda)
def filter_valid_accounts(accounts: List[Tuple[str, str]], filter_func) -> List[Tuple[str, str]]:
    return list(filter(filter_func, accounts))

@dataclass
class MerchantProfile:
    name: str = ""
    ship: str = ""
    favorite_potato_dish: str = ""
    alien_partners: List[str] = field(default_factory=list)

# Function to register a new user (potato trader)
@log_function_call
def register(accounts: List[Tuple[str, str]], potato_merchants: Dict[str, MerchantProfile]) -> Tuple[List[Tuple[str, str]], Dict[str, MerchantProfile]]:
    print("=== Register as a Potato Trader ===")
    nim = input("Enter your Trader ID (NIM): ")

    # Check if the Trader ID already exists using higher-order function
    accounts = filter_valid_accounts(accounts, lambda account: account[0] == nim)
    if accounts:
        print("Trader ID already exists!")
        return accounts, potato_merchants

    password = input("Create a password: ")
    accounts.append((nim, password))  # Add new account tuple

    print("Trader registered successfully!")
    
    choice = input("Do you want to fill your merchant profile now? (y/n): ").lower()
    if choice == 'y':
        profile = fill_profile()
        potato_merchants[nim] = profile
        if len(accounts) > 1:
            potato_merchants = add_alien_partners(nim, accounts, potato_merchants)
    else:
        potato_merchants[nim] = MerchantProfile()  # Add empty profile

    print("Registration complete. Welcome to the Intergalactic Potato Trading Network!")
    return accounts, potato_merchants

# Function to login
@log_function_call
def login(accounts: List[Tuple[str, str]], potato_merchants: Dict[str, MerchantProfile]) -> Optional[str]:
    print("=== Login ===")
    nim = input("Enter your Trader ID (NIM): ")
    password = input("Enter your password: ")

    # Validate the login credentials
    if any(nim == account[0] and password == account[1] for account in accounts):
        print("Login successful!")
        return nim
    else:
        print("Invalid Trader ID or password.")
        return None

# Function to fill potato merchant profile
def fill_profile() -> MerchantProfile:
    print("=== Fill Merchant Profile ===")
    name = input("Enter your Merchant Name: ")
    ship = input("Enter your Spaceship Type (e.g., Cosmic Frying Pan, Potato UFO): ")
    fav_dish = input("What’s your favorite potato dish? (e.g., Mashed, Baked, Fries): ")

    return MerchantProfile(name, ship, fav_dish)

# Function to add alien trading partners
@log_function_call
def add_alien_partners(nim: str, accounts: List[Tuple[str, str]], potato_merchants: Dict[str, MerchantProfile]) -> Dict[str, MerchantProfile]:
    if len(accounts) < 2:
        print("You need at least two traders to add alien partners.")
        return potato_merchants

    print("=== Add Alien Trading Partners ===")
    partners = input("Enter Alien Partner NIMs (comma separated): ").split(',')
    valid_partners = [partner.strip() for partner in partners if any(partner.strip() == account[0] for account in accounts)]

    if valid_partners:
        updated_profile = potato_merchants[nim]
        updated_profile.alien_partners.extend(valid_partners)
        potato_merchants[nim] = updated_profile
        print(f"Alien partners added: {', '.join(valid_partners)}")
    else:
        print("No valid alien partners were added.")
    
    return potato_merchants

# Function to show the user menu
@log_function_call
def user_menu(nim: str, accounts: List[Tuple[str, str]], potato_merchants: Dict[str, MerchantProfile]) -> Tuple[List[Tuple[str, str]], Dict[str, MerchantProfile]]:
    while True:
        print("\n=== Potato Trader Menu ===")
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. View Alien Partners")
        print("4. Add Alien Partners")
        print("5. Delete Profile or Alien Partners")
        print("6. Logout")

        choice = input("Choose an option: ")

        if choice == '1':
            view_profile(nim, potato_merchants)
        elif choice == '2':
            potato_merchants[nim] = fill_profile()
        elif choice == '3':
            view_alien_partners(nim, potato_merchants)
        elif choice == '4':
            potato_merchants = add_alien_partners(nim, accounts, potato_merchants)
        elif choice == '5':
            accounts, potato_merchants = delete_data(nim, accounts, potato_merchants)
        elif choice == '6':
            print("Logged out.")
            break
        else:
            print("Invalid option. Please try again.")
    
    return accounts, potato_merchants

# Function to view profile
def view_profile(nim: str, potato_merchants: Dict[str, MerchantProfile]):
    print("=== View Merchant Profile ===")
    profile = potato_merchants.get(nim)
    if profile:
        print(f"Name: {profile.name}")
        print(f"Spaceship: {profile.ship}")
        print(f"Favorite Potato Dish: {profile.favorite_potato_dish}")
    else:
        print("Profile not found.")

# Function to view alien partners
def view_alien_partners(nim: str, potato_merchants: Dict[str, MerchantProfile]):
    print("=== View Alien Trading Partners ===")
    partners = potato_merchants[nim].alien_partners
    if partners:
        print(f"Alien Partners: {', '.join(partners)}")
    else:
        print("No alien partners found.")

# Function to delete profile or alien partners
def delete_data(nim: str, accounts: List[Tuple[str, str]], potato_merchants: Dict[str, MerchantProfile]) -> Tuple[List[Tuple[str, str]], Dict[str, MerchantProfile]]:
    print("=== Delete Data ===")
    print("1. Delete Merchant Profile and Login")
    print("2. Delete Alien Partners List")
    choice = input("Choose what to delete: ")

    if choice == '1':
        potato_merchants.pop(nim, None)
        accounts = [account for account in accounts if account[0] != nim]
        print("Merchant profile and login credentials deleted.")
        main()
    elif choice == '2':
        if nim in potato_merchants:
            potato_merchants[nim].alien_partners.clear()
            print("Alien partners list deleted.")
        else:
            print("No profile found.")
    else:
        print("Invalid choice.")
    
    return accounts, potato_merchants

# Main menu
def main():
    accounts: List[Tuple[str, str]] = []
    potato_merchants: Dict[str, MerchantProfile] = {}
    
    while True:
        print("\n=== Intergalactic Potato Trader Main Menu ===")
        print("1. Register as a Potato Trader")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            accounts, potato_merchants = register(accounts, potato_merchants)
        elif choice == '2':
            nim = login(accounts, potato_merchants)
            if nim:
                accounts, potato_merchants = user_menu(nim, accounts, potato_merchants)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
