## This is a Car Dealership simulator. It will simulate a simplified version of purchasing a list of vehicles from a dealership.
## Planned features include:
## V1 Main menu, inventory list, buy car, sell car, balance tracking, profit tracking, exit game
## V2 Random car generation, Customer preferences, Day system, Random events
## V3 Save/load, Repairs, Negotiation, Reputation

import random



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
    
def view_stats(balance, cars_sold, total_profit, day):
    print("\n=== Dealership Stats ===")
    print(f"Current Day: {day}")
    print(f"Current Balance: £{balance}")
    print(f"Cars Sold: {cars_sold}")
    print(f"Total profit: £{total_profit}")
    
def sell_car(inventory, balance, cars_sold, total_profit, day):
    
    while True:
            print("\n=== Sell Car===")
            
            if len(inventory) == 0:
                print("No cars available to sell.")
                return balance, cars_sold, total_profit, day
            
            for index, car in enumerate(inventory, start=1):
                print(f"{index}, {car['brand']} {car['model']} (£{car['sell_price']})")
                
            print("B. Back to menu")
            
            choice = input("Select a car to sell: ")
            
            if choice.lower() == "b":
                return balance, cars_sold, total_profit, day
            
            if choice.isdigit():
                choice = int(choice)
                
                if 1 <= choice <= len(inventory):
                    car = inventory.pop(choice - 1)
                    
                    profit = car["sell_price"] - car["buy_price"]
                    
                    balance += car["sell_price"]
                    cars_sold += 1
                    total_profit += profit
                    day += 1
                    
                    print(f"\nSold {car['brand']} {car['model']} for £{car['sell_price']}")
                    print(f"Profit: £{profit}")
                    
                    return balance, cars_sold, total_profit, day
            print("Invalid choice.")
    
def generate_random_car():
    brands_and_models = {
        "BMW": ["220i", "M235i", "M240i", "M2", "320i", "M340i", "M3", "M3 Competition", "420i", "M440i", "M4", "M4 Competition", "X1", "X2", "X3", "X3M", "X4","X5"],
        "Audi": ["A1", "A2", "A3", "S3", "RS3", "A4", "A5", "A6", "S4", "S5", "S6", "Q2", "Q3", "Q4", "Q5"],
        "Ford": ["Fiesta", "Focus", "Puma"],
        "Mercedes": ["A-Class", "C200", "GLA"],
        "Toyota": ["Yaris", "Prius", "Corolla"],
        "Volkswagen": ["Golf", "Golf R", "Polo", "Tiguan"]
    }
    
    brand = random.choice(list(brands_and_models.keys()))
    model = random.choice(brands_and_models[brand])
    
    year = random.randint(2010, 2026)
    mileage = random.randint(1000, 150000)
    
    buy_price = random.randint(5000, 30000)
    sell_price = buy_price + random.randint(1500, 10000)
    
    car = {
        "brand": brand,
        "model": model,
        "year": year,
        "mileage": mileage,
        "buy_price": buy_price,
        "sell_price": sell_price
    }
    
    return car


def buy_car(inventory, balance, day):
    cars_for_sale = [generate_random_car(), generate_random_car(), generate_random_car()]
    
    while True:
        print("\n=== Buy Car===")
        
        for index, car in enumerate(cars_for_sale, start=1):
                                    print(f"{index}. {car['brand']} {car['model']} | Year: {car['year']} | Mileage: {car['mileage']} | Cost: £{car['buy_price']}")
        print("B. Back to menu")
        
        choice = input("Select a car to buy: ")
        
        if choice.lower() == "b":
            return balance, day
        if choice.isdigit():
            choice = int(choice)
            
            if 1 <= choice <= len(cars_for_sale):
                selected_car = cars_for_sale[choice - 1]
                
                if balance >= selected_car["buy_price"]:
                    inventory.append(selected_car)
                    balance -= selected_car["buy_price"]
                    day += 1
                    
                    print(f"\nBought {selected_car['brand']} {selected_car['model']} for £{selected_car['buy_price']}")
                else:
                    print("You do not have enough money to buy that car.")
            else:
                print("Invalid choice.")
        else:
            print("Invalid Choice.")
            
            
def check_game_state(balance, day):
    if balance >= 100000:
        print("\n You win. You created a successful car dealership")
        print(f"\n Your final balance was £{balance}")
        return False
    
    if day > 15:
        print("\n GAME OVER. You did not create a successful car dealership")
        return False
    
    return True
        
        
        
                    
def main():
    
    balance = 50000
    cars_sold = 0
    total_profit = 0
    day = 1
    
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
                    balance, day = buy_car(inventory, balance, day)
                elif choice == "3":
                    balance, cars_sold, total_profit, day = sell_car(
                        inventory, balance, cars_sold, total_profit, day
                        )
                elif choice == "4":
                    view_stats(balance, cars_sold, total_profit, day)
                elif choice == "5":
                    print("Goodbye!")
                    running = False
                else:
                    print("Invalid choice. Please try again")
                
                if running:
                    running = check_game_state(balance, day)
                
# Main
main()