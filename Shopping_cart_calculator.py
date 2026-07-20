Items  = int(input("How many items?: "))
total = 0

for i in range (1,Items):
    Item_name = input("Enter your item: ")
    price = float(input("Enter Item price: "))
    total = total + price
    print("item",i,":",Item_name)
    print(total)

print("toal itme is: ",Items)
print("Total price is: ",total)

if total >= 1000:
    discount = 20
elif total >= 700:
    discount = 10
elif total >= 500:
    discount = 5
else:
    discount = 0 
    print("No discount available")

    final_amount = total - (total * discount/100)
    print("you got",discount,"%" "discount")
    print("your final amount is: ",final_amount) 

     
