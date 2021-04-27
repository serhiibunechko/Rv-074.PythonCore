#The amount of moneamount is known. 
#Exchange it with 200, 100, 10 banknotes and 1 UAH coin, if possible

amount = int(input('Enter money amount:'))

print ("200:", amount // 200)
amount -= ((amount // 200)*200)
print ("100:", amount // 100)
amount -= ((amount // 100)*100)
print ("50:", amount // 50)
amount -= ((amount // 50)*50)
print ("10:", amount // 10)
amount -= ((amount // 10)*10)
print ("1:", amount // 1)