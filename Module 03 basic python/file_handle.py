# # .csv comma separated value
# .txt text file

# with open('message.txt','w') as file:
#     file.write('I love python')

with open('message.txt','r') as file:
    txt =file.read()
    print(txt)