import os
import datetime

def generate_sales_invoice(customer_name, cart_items, transaction_date, total_amount):
    """Generate a sales invoice and save it to a file."""
    # Create invoices directory if it doesn't exist
    os.makedirs("invoices", exist_ok=True)
    
    # Generate a unique filename based on date and customer name
    timestamp = transaction_date.strftime("%Y%m%d_%H%M%S")
    sanitized_name = "".join(c if c.isalnum() else "_" for c in customer_name)
    filename = f"invoices/SALE_{sanitized_name}_{timestamp}.txt"
    
    # Format the date for display
    formatted_date = transaction_date.strftime("%d-%m-%Y %H:%M:%S")
    
    with open(filename, "w") as file:
        file.write("=" * 60 + "\n")
        file.write(f"{'PRANISHA BEAUTY PRODUCTS':^60}\n")
        file.write(f"{'SALES INVOICE':^60}\n")
        file.write("=" * 60 + "\n\n")
        
        file.write(f"Invoice No: SALE_{timestamp}\n")
        file.write(f"Date: {formatted_date}\n")
        file.write(f"Customer: {customer_name}\n\n")
        
        file.write("-" * 60 + "\n")
        file.write(f"{'Item':<20}{'Brand':<15}{'Qty':<8}{'Free':<8}{'Price':<10}{'Amount':<10}\n")
        file.write("-" * 60 + "\n")
        
        for item in cart_items:
            file.write(f"{item['name']:<20}{item['brand']:<15}{item['quantity']:<8}{item['free_items']:<8}NPR{item['unit_price']:<9.2f}NPR{item['total']:<9.2f}\n")
        
        file.write("-" * 60 + "\n")
        file.write(f"{'TOTAL AMOUNT:':<51}NPR{total_amount:<9.2f}\n")
        file.write("-" * 60 + "\n\n")
        
        file.write("Buy 3 Get 1 Free Promotion Applied\n\n")
        file.write("Thank you for shopping with Pranisha Beauty Products!\n")
        file.write("=" * 60 + "\n")
    
    return filename

def generate_purchase_invoice(supplier_name, restock_items, transaction_date, total_amount):
    """Generate a purchase invoice and save it to a file."""
    # Create invoices directory if it doesn't exist
    os.makedirs("invoices", exist_ok=True)
    
    # Generate a unique filename based on date and supplier name
    timestamp = transaction_date.strftime("%Y%m%d_%H%M%S")
    sanitized_name = "".join(c if c.isalnum() else "_" for c in supplier_name)
    filename = f"invoices/PURCHASE_{sanitized_name}_{timestamp}.txt"
    
    # Format the date for display
    formatted_date = transaction_date.strftime("%d-%m-%Y %H:%M:%S")
    
    with open(filename, "w") as file:
        file.write("=" * 60 + "\n")
        file.write(f"{'PRANISHA BEAUTY PRODUCTS':^60}\n")
        file.write(f"{'PURCHASE INVOICE':^60}\n")
        file.write("=" * 60 + "\n\n")
        
        file.write(f"Invoice No: PURCH_{timestamp}\n")
        file.write(f"Date: {formatted_date}\n")
        file.write(f"Supplier: {supplier_name}\n\n")
        
        file.write("-" * 60 + "\n")
        file.write(f"{'Item':<20}{'Brand':<15}{'Qty':<10}{'Cost':<10}{'Amount':<10}\n")
        file.write("-" * 60 + "\n")
        
        for item in restock_items:
            file.write(f"{item['name']:<20}{item['brand']:<15}{item['quantity']:<10}NPR{item['unit_cost']:<9.2f}NPR{item['total']:<9.2f}\n")
        
        file.write("-" * 60 + "\n")
        file.write(f"{'TOTAL COST:':<45}NPR{total_amount:<9.2f}\n")
        file.write("-" * 60 + "\n\n")
        
        file.write("Inventory has been updated with these items.\n\n")
        file.write("=" * 60 + "\n")
    
    return filename
