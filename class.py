class Smartphone:
    def __init__(self, brand, model, price):
        """
        Constructor to initialize a Smartphone object.
        """
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        """
        Method to display the smartphone's details.
        """
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")

    def apply_discount(self, discount_percent):
        """
        Method to apply a discount to the smartphone's price.
        """
        if 0 <= discount_percent <= 100:
            discount_amount = self.price * (discount_percent / 100)
            self.price -= discount_amount
            print(f"Discount of {discount_percent}% applied. New price: ${self.price:.2f}")
        else:
            print("Invalid discount percentage!")

# Inheritance Example: GamingSmartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, ram, battery_capacity):
        """
        Constructor to initialize a GamingSmartphone object.
        """
        super().__init__(brand, model, price)
        self.ram = ram
        self.battery_capacity = battery_capacity

    def display_gaming_info(self):
        """
        Method to display additional gaming-specific details.
        """
        self.display_info()
        print(f"RAM: {self.ram}GB, Battery: {self.battery_capacity}mAh")

# Example usage
smartphone = Smartphone("Apple", "iPhone 14", 999)
smartphone.display_info()
smartphone.apply_discount(10)

gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 1299, 16, 6000)
gaming_phone.display_gaming_info()
gaming_phone.apply_discount(15)
