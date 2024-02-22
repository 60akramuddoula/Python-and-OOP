
class Shop:

    cart = [] # class attributes which can be accessed from
    # anywhere else of the code  

    def __init__(self, buyer):
        self.buyer= buyer

    def add_to_cart(self, item):
        self.cart.append(item)


person1= Shop('Bappi')
person1.add_to_cart('shoes')
person1.add_to_cart('bike')
person1.add_to_cart('phone')
print(person1.cart)

person2= Shop('akramuddoula')
person1.add_to_cart('car')
person1.add_to_cart('pen')
person1.add_to_cart('cycle')

print(person2.cart)

        