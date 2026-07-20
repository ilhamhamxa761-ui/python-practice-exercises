Total_grocerry_item = int(input("Enter Total number of grocerry item: "))

grand_total = 0

for i in range(1,Total_grocerry_item+1):
    Item_name = input("Enter Item name: ")
    Item_Quantity = int(input("Enter item Quantity: "))
    Price_per_unit = float(input("Enter price per unit of item: "))
    subtotal = Item_Quantity * Price_per_unit
    print("item",i,":",Item_name.upper())
    print("Qty: ",Item_Quantity)
    print("RS: ",Price_per_unit)  
    print("SUbtotal: ",subtotal)
    grand_total = grand_total + subtotal

print("total Item is:",Total_grocerry_item)
print("Grande Total is:",grand_total)

if grand_total >= 1500:
    discount = 15
elif grand_total >= 1000:
    discount = 10
elif grand_total >= 700:
    discount = 5
else:
    discount = 0
    print("NO discount")
final_bil_amout = grand_total - (grand_total * discount / 100)
print("you got",discount,"% Discount")
print("your final bill after Discount is:",final_bil_amout)