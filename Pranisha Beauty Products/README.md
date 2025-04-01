# Pranisha Beauty Products Management System

A simple inventory management and invoicing system for Pranisha Beauty Products store.

## Features

- View available products with selling prices (200% markup from cost price)
- Process sales with "buy 3 get 1 free" promotion
- Generate sales invoices as text files
- Restock products and update inventory
- Generate purchase invoices for restocking
- Update inventory after each transaction

## Usage

Run the program with Python:

```
python main.py
```

The system will load product information from `products.txt` and present a menu with options to:
1. View Available Products
2. Process a Sale
3. Restock Products
4. Exit

### Sales Process

When processing a sale:
1. Enter customer name
2. Select products by their number
3. Specify quantities to purchase
4. Free items will be calculated automatically (1 free item for every 3 purchased)
5. Confirm the sale to generate an invoice and update inventory

### Restocking Process

When restocking:
1. Enter supplier name
2. Select products by their number
3. Specify quantities to restock
4. Optionally update the cost price
5. Confirm the restock to generate a purchase invoice and update inventory

## Data Structure

Products are stored in a text file with the following format:
```
Name, Brand, Quantity, Cost Price, Origin
```

Example:
```
Kumkumadi Oil, Aroma Magic, 150, 1200, Nepal
```

## Invoices

Invoices are generated as text files in the `invoices` directory with unique filenames based on the transaction type, customer/supplier name, and timestamp.
