from math import prod
from numpy import append


class shopping:

    def __init__(self, name):
        self.name= name
        self.cart=[]


    def add_to_cart(self, item, price, quantity):

        product= {'item': item, 'price': price, 'quantity': quantity}
        # ekhon  cart a rakhbo jinis gula  
        self.cart.append(product)
        
    def remove_from_cart(self, item):
        for product in self.cart:
            if product['item']== item:
                self.cart.remove(product)
                print(f'Remove the item successfully from the cart')    
    def checkout(self, ammount):
        total=0
        for item in self.cart:
            # print(item)
            total+= item['price']* item['quantity']
            print('Total price is:', total)

            # now check korbo amr taka onujayi ami 
            # kinte parbo kina product ,
            if total>ammount:
                 print(f'Please provide an additional amount of {total - ammount}')
            else:
                extra= ammount- total
                print(f'Here is your extra money: {extra}')

        


bappi = shopping('akramuddoula')
bappi.add_to_cart('alu', 50,6)
bappi.add_to_cart('dim', 60,5)
bappi.add_to_cart('rice', 70,6)
# print(bappi.cart)


bappi.remove_from_cart('alu')
print(bappi.cart)
bappi.checkout(500)