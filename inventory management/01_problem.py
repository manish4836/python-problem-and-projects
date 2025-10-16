products = {}

def add_product():
    print("\n--- Add New Product ---")
    id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    
    products[id] = {
        'name': name,
        'price': price, 
        'quantity': quantity
    }
    print(f"✅ {name} added successfully!")

def show_products():
    print("\n--- All Products ---")
    for id, details in products.items():
        print(f"ID: {id} | {details['name']} | ₹{details['price']} | Qty: {details['quantity']}")

while True:
    print("\n" + "="*30)
    print("Inventory Management System")
    print("="*30)
    print("1. Add Product")
    print("2. Show Products") 
    print("3. Exit")

    choice = input("Choose an option: ")
    if choice == '1':
        add_product()
    elif choice == '2':
        show_products()
    elif choice == '3':
        print("System closed.")
        break
    else:
        print("Invalid choice. Please try again.")

        