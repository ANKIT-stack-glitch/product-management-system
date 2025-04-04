import os
import sys
from inventory import load_inventory, save_inventory, display_products
from transaction import process_sale, process_restock
from utils import clear_screen, validate_input

def main():
    inventory_file = "products.txt"
    
    if not os.path.exists(inventory_file):
        with open(inventory_file, "w") as f:
            f.write("Kumkumadi Oil, Aroma Magic, 150, 1200, Nepal\n")
            f.write("Herbal Face Pack, Himalaya, 200, 350, Nepal\n")
            f.write("Aloe Vera Gel, Patanjali, 120, 180, Nepal\n")
    
    while True:
        clear_screen()
        print("\n===== PRANISHA BEAUTY PRODUCTS MANAGEMENT SYSTEM =====")
        print("1. View Available Products")
        print("2. Process a Sale")
        print("3. Restock Products")
        print("4. Exit")
        
        choice = validate_input("Enter your choice (1-4): ", lambda x: x in ["1", "2", "3", "4"])
        
        if choice == "1":
            products = load_inventory(inventory_file)
            display_products(products)
            input("\nPress Enter to continue...")
            
        elif choice == "2":
            products = load_inventory(inventory_file)
            if not products:
                print("No products available for sale.")
                input("\nPress Enter to continue...")
                continue
            
            display_products(products)
            updated_products = process_sale(products)
            if updated_products:
                save_inventory(updated_products, inventory_file)
            input("\nPress Enter to continue...")
            
        elif choice == "3":
            products = load_inventory(inventory_file)
            display_products(products)
            updated_products = process_restock(products)
            if updated_products:
                save_inventory(updated_products, inventory_file)
            input("\nPress Enter to continue...")
            
        elif choice == "4":
            print("\nThank you for using the Pranisha Beauty Products Management System. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user. Goodbye!")
        sys.exit(0)
