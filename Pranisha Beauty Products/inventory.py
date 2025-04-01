import datetime

def load_inventory(filename):
    """Load the product inventory from a file."""
    products = []
    try:
        with open(filename, "r") as file:
            for line in file:
                # Strip whitespace and split by comma
                parts = [part.strip() for part in line.strip().split(",")]
                if len(parts) >= 5:
                    product = {
                        "name": parts[0],
                        "brand": parts[1],
                        "quantity": int(parts[2]),
                        "cost_price": float(parts[3]),
                        "origin": parts[4]
                    }
                    products.append(product)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"Error loading inventory: {e}")
    
    return products

def save_inventory(products, filename):
    """Save the product inventory to a file."""
    try:
        with open(filename, "w") as file:
            for product in products:
                line = f"{product['name']}, {product['brand']}, {product['quantity']}, {product['cost_price']}, {product['origin']}\n"
                file.write(line)
        print("Inventory updated successfully.")
    except Exception as e:
        print(f"Error saving inventory: {e}")

def display_products(products):
    """Display the products with selling price (markup)."""
    if not products:
        print("No products available in inventory.")
        return
    
    # Calculate markup price (200% of cost price)
    markup_percentage = 2.0  # 200% markup
    
    print("\n===== AVAILABLE PRODUCTS =====")
    print(f"{'No.':<4}{'Product':<20}{'Brand':<15}{'Stock':<10}{'Price (NPR)':<15}{'Origin':<15}")
    print("-" * 75)
    
    for i, product in enumerate(products, 1):
        selling_price = product['cost_price'] * markup_percentage
        print(f"{i:<4}{product['name']:<20}{product['brand']:<15}{product['quantity']:<10}{selling_price:<15.2f}{product['origin']:<15}")
    
    print("-" * 75)
