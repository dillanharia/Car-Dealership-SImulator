## This is a Car Dealership simulator. It will simulate a simplified version of purchasing a list of vehicles from a dealership.
## Planned features include:
## V1 Main menu, inventory list, buy car, sell car, balance tracking, profit tracking, exit game
## V2 Random car generation, Customer preferences, Day system, Random events
## V3 Save/load, Repairs, Negotiation, Reputation

# ---Methods---
def show_menu():
    print("\n=== Car Dealership Simulator ===")
    print("1. View Inventory")
    print("2. Buy Car")
    print("3. Sell Car")
    print("4. View Stats")
    print("5. Exit")
    
def view_inventory(inventory):
    print("\n=== Current Inventory ==")
    
    if len(inventory) == 0:
        print("No cars in stock.")
    else:
        for index, car in enumerate(inventory, start=1):
            print(f"{index}, {car['brand']} {car['model']} | Year: {car['year']} | Mileage: {car['mileage']} | Buy Price: £{car['buy_price']} | Sell Price: £{car['sell_price']}")
    
def view_stats(balance, cars_sold, total_profit):
    print("\n=== Dealership Stats ===")
    print(f"Current Balance: £{balance}")
    print(f"Cars Sold: {cars_sold}")
    print(f"Total profit: £{total_profit}")
    
def sell_car(inventory, balance, cars_sold, total_profit):
    
    while True:
            print("\n=== Sell Car===")
            
            if len(inventory) == 0:
                print("No cars available to sell.")
                return balance, cars_sold, total_profit
            
            for index, car in enumerate(inventory, start=1):
                print(f"{index}, {car['brand']} {car['model']} (£{car['sell_price']})")
                
            print("B. Back to menu")
            
            choice = input("Select a car to sell: ")
            
            if choice.lower() == "b":
                return balance, cars_sold, total_profit
            
            if choice.isdigit():
                choice = int(choice)
                
                if 1 <= choice <= len(inventory):
                    car = inventory.pop(choice - 1)
                    
                    profit = car["sell_price"] - car["buy_price"]
                    
                    balance += car["sell_price"]
                    cars_sold += 1
                    total_profit += profit
                    
                    print(f"\nSold {car['brand']} {car['model']} for £{car['sell_price']}")
                    print(f"Profit: £{profit}")
                    
                    return balance, cars_sold, total_profit
            print("Invalid choice.")
    

def main():
    
    balance = 50000
    cars_sold = 0
    total_profit = 0
    
    
    inventory = [
        {"brand": "BMW", "model": "320d", "year": 2018, "mileage": 54000, "buy_price": 12000, "sell_price": 14500},
        {"brand": "Audi", "model": "A1", "year": 2021, "mileage": 12304, "buy_price": 18000, "sell_price": 20150},
        {"brand": "Ford", "model": "Focus", "year": 2015, "mileage": 35034, "buy_price": 12300, "sell_price": 14020},
        {"brand": "Toyota", "model": "Prius", "year": 2025, "mileage": 300, "buy_price": 16000, "sell_price": 18000},
        {"brand": "Volkswagen", "model": "Golf", "year": 2010, "mileage": 76004, "buy_price": 7500, "sell_price": 9200}
        ]
                  
                  
                  
    running = True
    
    while running:
 
                show_menu()
                choice = input("Choose an option: ")
                
                if choice == "1":
                    print("View Inventory selected")
                    view_inventory(inventory)
                elif choice == "2":
                    print("Buy Car selected")
                elif choice == "3":
                    balance, cars_sold, total_profit = sell_car(
                        inventory, balance, cars_sold, total_profit
                        )
                elif choice == "4":
                    view_stats(balance, cars_sold, total_profit)
                elif choice == "5":
                    print("Goodbye!")
                    running = False
                else:
                    print("Invalid choice. Please try again")
                
# Main
main()