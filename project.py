class Toy:
    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def validate_price(self, price):
        try:
            price = float(price)
            if price > 0:
                return True
            else:
                return False
        except ValueError:
            return False

class Customer:
    def __init__(self, name, email, is_premium=False):
        self.name = name
        self.email = email
        self.is_premium = is_premium

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.total = 0

    def add_item(self, toy, quantity):
        if toy.stock >= quantity:
            self.items.append((toy, quantity))
            self.total += toy.price * quantity
            toy.stock -= quantity
            return True
        else:
            return False

class Store:
    def __init__(self):
        self.toys = []
        self.customers = []

    def add_toy(self, name, category, price, stock):
        toy = Toy(name, category, price, stock)
        self.toys.append(toy)

    def list_toys(self):
        print("Catalog:")
        for i, toy in enumerate(self.toys, 1):
            print(f"{i}. {toy.name} - {toy.price}$ ({toy.stock} available)")

    def edit_toy(self, index, name, category, price, stock):
        if 0 <= index < len(self.toys):
            if self.toys[index].validate_price(price):
                self.toys[index].name = name
                self.toys[index].category = category
                self.toys[index].price = float(price)
                self.toys[index].stock = stock
                return True
            else:
                return False
        else:
            return False

    def delete_toy(self, index):
        if 0 <= index < len(self.toys):
            del self.toys[index]
            return True
        else:
            return False

    def add_customer(self, customer):
        self.customers.append(customer)

    def list_customers(self):
        print("Customers:")
        for customer in self.customers:
            print(customer.name, customer.email)

    def validate_order(self, order):
        for item, quantity in order.items:
            if item.stock < quantity:
                return False
        return True

    def process_order(self, order):
        if self.validate_order(order):
            if order.customer.is_premium:
                order.total *= 0.9  # 10% discount for premium customers
            print(f"Processing order for {order.customer.name}. Total amount: {order.total}$")
            # Here you would typically handle payment processing, shipping, etc.
            for item, quantity in order.items:
                item.stock -= quantity
        else:
            print("Insufficient stock for one or more items in the order.")

# Приклад використання:
store = Store()
store.add_toy("LEGO Set", "Building Blocks", 29.99, 100)
store.add_toy("Barbie Doll", "Dolls", 19.99, 50)

store.list_toys()

# Редагуємо товар
store.edit_toy(1, "Barbie Doll", "Dolls", "24.99", 30)

# Видаляємо товар
store.delete_toy(1)

store.list_toys()

customer = Customer("John Doe", "john@example.com", is_premium=True)
store.add_customer(customer)

order = Order(customer)
order.add_item(store.toys[0], 2)

store.process_order(order)
