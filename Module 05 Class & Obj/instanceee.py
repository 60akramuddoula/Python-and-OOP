class Shop:
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []  # instance attribute to store items in the cart

    def add_to_cart(self, item):
        self.cart.append(item)

# Creating instances of the Shop class and adding items to their carts
person1 = Shop('akramuddoula')
person1.add_to_cart('bike')
person1.add_to_cart('car')
person1.add_to_cart('pen')

person2 = Shop('bappi')
person2.add_to_cart('shoe')
person2.add_to_cart('phone')
person2.add_to_cart('watch')

print(person1.cart)
print(person2.cart)