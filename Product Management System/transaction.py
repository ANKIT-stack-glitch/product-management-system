import os
import datetime
from utils import validate_input
from invoice import generate_sales_invoice, generate_purchase_invoice

def process_sale(products):
    """Process a product sale."""
    if not products:
        print("No products available for sale.")
        return None
    
    # Customer information
    customer_name = input("\nEnter customer name: ").strip()
    if not customer_name:
        print("Invalid customer name. Sale cancelled.")
        return None
    
    # Initialize cart
    cart = []
    markup_percentage = 2.0  # 200% markup
    
    # Add products to cart
    while True:
        try:
            product_id = validate_input("\nEnter product number (0 to finish): ", 
                                      lambda x: x == "0" or (x.isdigit() and 1 <= int(x) <= len(products)))
            
            if product_id == "0":
                break
            
            product_id = int(product_id) - 1
            quantity = validate_input("Enter quantity to purchase: ", 
                                    lambda x: x.isdigit() and int(x) > 0)
            quantity = int(quantity)
            
            # Check if enough stock
            if quantity > products[product_id]["quantity"]:
                print(f"Error: Only {products[product_id]['quantity']} items in stock.")
                continue
            
            # Calculate free items based on the "buy 3 get 1 free" policy
            free_items = quantity // 3
            total_items = quantity + free_items
            
            # Don't exceed stock with free items
            if total_items > products[product_id]["quantity"]:
                print(f"Warning: Not enough stock for all free items. Only {products[product_id]['quantity'] - quantity} free items available.")
                free_items = products[product_id]["quantity"] - quantity
                total_items = quantity + free_items
            
            selling_price = products[product_id]["cost_price"] * markup_percentage
            item_total = quantity * selling_price  # Only charge for purchased items, not free ones
            
            cart_item = {
                "product_id": product_id,
                "name": products[product_id]["name"],
                "brand": products[product_id]["brand"],
                "quantity": quantity,
                "free_items": free_items,
                "total_items": total_items,
                "unit_price": selling_price,
                "total": item_total
            }
            
            cart.append(cart_item)
            print(f"Added to cart: {quantity} {products[product_id]['name']} (+ {free_items} free)")
            
        except ValueError:
            print("Invalid input. Please try again.")
    
    # If cart is empty, cancel sale
    if not cart:
        print("Cart is empty. Sale cancelled.")
        return None
    
    # Display cart summary
    print("\n===== CART SUMMARY =====")
    grand_total = 0
    for item in cart:
        print(f"{item['quantity']} {item['name']} (+ {item['free_items']} free) @ NPR{item['unit_price']:.2f} = NPR{item['total']:.2f}")
        grand_total += item['total']
    print(f"\nTotal Amount: NPR{grand_total:.2f}")
    
    # Confirm sale
    confirm = validate_input("\nConfirm sale? (y/n): ", lambda x: x.lower() in ["y", "n"])
    if confirm.lower() != "y":
        print("Sale cancelled.")
        return None
    
    # Update inventory
    for item in cart:
        product_id = item["product_id"]
        products[product_id]["quantity"] -= item["total_items"]  # Reduce by total items (purchased + free)
    
    # Generate invoice
    transaction_date = datetime.datetime.now()
    invoice_filename = generate_sales_invoice(customer_name, cart, transaction_date, grand_total)
    print(f"\nSale completed successfully. Invoice saved as: {invoice_filename}")
    
    return products

def process_restock(products):
    """Process product restocking."""
    if not products:
        print("No products in inventory to restock.")
        return None
    
    # Supplier information
    supplier_name = input("\nEnter supplier name: ").strip()
    if not supplier_name:
        print("Invalid supplier name. Restock cancelled.")
        return None
    
    # Initialize restock items
    restock_items = []
    
    # Add products to restock
    while True:
        try:
            product_id = validate_input("\nEnter product number (0 to finish): ", 
                                      lambda x: x == "0" or (x.isdigit() and 1 <= int(x) <= len(products)))
            
            if product_id == "0":
                break
            
            product_id = int(product_id) - 1
            quantity = validate_input("Enter quantity to restock: ", 
                                    lambda x: x.isdigit() and int(x) > 0)
            quantity = int(quantity)
            
            # Option to update cost price
            current_cost = products[product_id]["cost_price"]
            print(f"Current cost price: NPR{current_cost:.2f}")
            update_price = validate_input("Update cost price? (y/n): ", lambda x: x.lower() in ["y", "n"])
            
            if update_price.lower() == "y":
                new_cost = validate_input("Enter new cost price: ", 
                                        lambda x: x.replace('.', '', 1).isdigit() and float(x) > 0)
                cost_price = float(new_cost)
            else:
                cost_price = current_cost
            
            item_total = quantity * cost_price
            
            restock_item = {
                "product_id": product_id,
                "name": products[product_id]["name"],
                "brand": products[product_id]["brand"],
                "quantity": quantity,
                "unit_cost": cost_price,
                "total": item_total
            }
            
            restock_items.append(restock_item)
            print(f"Added to restock: {quantity} {products[product_id]['name']} @ NPR{cost_price:.2f}")
            
        except ValueError:
            print("Invalid input. Please try again.")
    
    # If no items to restock, cancel
    if not restock_items:
        print("No items to restock. Restock cancelled.")
        return None
    
    # Display restock summary
    print("\n===== RESTOCK SUMMARY =====")
    grand_total = 0
    for item in restock_items:
        print(f"{item['quantity']} {item['name']} @ NPR{item['unit_cost']:.2f} = NPR{item['total']:.2f}")
        grand_total += item['total']
    print(f"\nTotal Cost: NPR{grand_total:.2f}")
    
    # Confirm restock
    confirm = validate_input("\nConfirm restock? (y/n): ", lambda x: x.lower() in ["y", "n"])
    if confirm.lower() != "y":
        print("Restock cancelled.")
        return None
    
    # Update inventory
    for item in restock_items:
        product_id = item["product_id"]
        products[product_id]["quantity"] += item["quantity"]
        products[product_id]["cost_price"] = item["unit_cost"]  # Update cost price
    
    # Generate invoice
    transaction_date = datetime.datetime.now()
    invoice_filename = generate_purchase_invoice(supplier_name, restock_items, transaction_date, grand_total)
    print(f"\nRestock completed successfully. Invoice saved as: {invoice_filename}")
    
    return products
