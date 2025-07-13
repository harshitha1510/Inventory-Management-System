inventory = {}

def welcome():
    print("\n📦📋 Welcome to the Simple Inventory Manager 📋📦")
    print("-" * 55)

def menu():
    print("\nChoose an option:")
    print("1. ➕ Add Product")
    print("2. 🔄 Update Product")
    print("3. ❌ Delete Product")
    print("4. 📦 View All Products")
    print("5. 🚪 Exit")

def add_product():
    print("\n➕ Add New Product")
    name = input("📝 Enter product name: ").strip().title()
    if not name:
        print("⚠️ Product name cannot be empty.")
        return
    if name in inventory:
        print("⚠️ Product already exists. Try updating it instead.")
        return
    try:
        quantity = int(input("📦 Enter quantity: "))
        price = float(input("💰 Enter price per unit: ₹"))
        if quantity < 0 or price < 0:
            print("⚠️ Quantity and price must be non-negative.")
            return
        inventory[name] = {'quantity': quantity, 'price': price}
        print(f"✅ '{name}' added successfully to inventory.")
    except ValueError:
        print("⚠️ Invalid input! Please enter numbers only.")

def update_product():
    print("\n🔄 Update Product")
    name = input("📝 Enter product name to update: ").strip().title()
    if name not in inventory:
        print("❌ Product not found.")
        return
    try:
        quantity = int(input("📦 Enter new quantity: "))
        price = float(input("💰 Enter new price per unit: ₹"))
        if quantity < 0 or price < 0:
            print("⚠️ Quantity and price must be non-negative.")
            return
        inventory[name]['quantity'] = quantity
        inventory[name]['price'] = price
        print(f"✅ '{name}' updated successfully.")
    except ValueError:
        print("⚠️ Invalid input. Please enter valid numbers.")

def delete_product():
    print("\n❌ Delete Product")
    name = input("📝 Enter product name to delete: ").strip().title()
    if name in inventory:
        del inventory[name]
        print(f"🗑️ '{name}' has been removed from inventory.")
    else:
        print("❌ Product not found.")

def view_products():
    print("\n📦 Current Inventory")
    if not inventory:
        print("🚫 No products in inventory.")
        return
    print("-" * 45)
    for name, info in inventory.items():
        print(f"🔹 {name}: {info['quantity']} units | ₹{info['price']:.2f} per unit")
    print("-" * 45)

def start():
    welcome()
    while True:
        menu()
        choice = input("👉 Enter your choice (1-5): ").strip()
        if choice == '1':
            add_product()
        elif choice == '2':
            update_product()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            view_products()
        elif choice == '5':
            print("\n👋 Thank you for using the Inventory Manager. Stay organized!\n")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    start()
