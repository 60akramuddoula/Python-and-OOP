

class Phone:
    manufactured = 'china'

    def sms(self, phone, sms):
        text= f'sending sms to {phone}: {sms}'
        print(text)

    # Constructor in python named as __int__(self)
    def __init__(self, owner, brand, price):
        self.owner= owner
        self.brand= brand
        self.price= price


bappi= Phone('akramuddoula', 'sumsung',20000)
habib= Phone('habibur', 'nokia',18500)
bappi.sms(1793870240, 'I am so disturbed')

print(bappi.owner, bappi.brand, bappi.price)
print(habib.owner, habib.brand, habib.price)        