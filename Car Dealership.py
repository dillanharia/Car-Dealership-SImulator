## This is a Car Dealership simulator. It will simulate a simplified version of purchasing a list of vehicles from a dealership.
## Planned features include:
## V1 Main menu, inventory list, buy car, sell car, balance tracking, profit tracking, exit game
## V2 Random car generation, Customer preferences, Day system, Random events
## V3 Save/load, Repairs, Negotiation, Reputation

# ---Methods---
def show_menu():
    print("/n=== Car Dealership Simulator ===")
    print("1. View Inventory")
    print("2. Buy Car")
    print("3. Sell Car")
    print("4. View Stats")
    print("5. Exit")
    
def main():
    running = True
    
    while running:
        show_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            print("View Inventory selected")
        elif choice == "2":
            print("Buy Car selected")
        elif choice == "3":
            print("Sell Car selected")
        elif choice == "4":
            print("View Stats selected")
        elif choice == "5":
            print("Goodbye!")
            running = False
        else:
            print("Invalid choice. Please try again")
            
# Main
main()