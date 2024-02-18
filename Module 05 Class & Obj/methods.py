

def call():
    print('calling someone i dont know ')
    return 'call done'

class Phone:
    price =1000
    brand= 'samsung'
    color= 'blue'
    features= ['camera','speaker', 'hammer']

    def call(self):
        print('calling one person')

    def send_sms(self, phone , sms):
        text= f'sending sms to : {phone} and message : {sms}'
        return text


my_phone= Phone() # class er ekta object creat korsi 
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(93870240, 'hey i missed you')
print(result)
