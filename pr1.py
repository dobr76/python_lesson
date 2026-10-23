#receipt calculator
count1=4
name1="coffee1"
price1=4.9
count2=3
name2="pie"
price2=2.4
count3=5
name3="penne"
price3=3.9

a1=count1*price1
a2=count2*price2
a3=count3*price3
tax=13/100
subtotal=a1+a2+a3
discount =5
subtotal=subtotal-discount
tax_am=subtotal*tax
total=subtotal+tax_am


print("---RECEIPT---")
print("Coffee     x"+str(count1)+"   "+str(a1))
print("Pie     x"+str(count2)+"   "+str(a2))
print("Penne     x"+str(count13)+"   "+str(a3))
print("Subtotal:   "+str(subtotal))
print("Tax(13%):   "+str(tax_am))
print("Total:    "+str(total))




