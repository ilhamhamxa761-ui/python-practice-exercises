Resturant_name = input("Enter Resutrant name: ")
Customer_name = input("Enter cutumer name: ")
Membership_Type = input("Membership Type : Gold , Platinum , Regular: ").title()

match Membership_Type:
    case "Regular":
        discount = 0
        print("No Discount available")
    case "Gold":
        discount = 10
        print("you got",discount,"% Discount")
    case "Platinum":
        discount = 20
        print("You got",discount,"% Discount")
    case _:
        print("Invalid Membership")

 
Itmes = int(input("Enter Total Items: "))
total_bill = 0
for i in range(1 , Itmes + 1):
    items_name = input("Item Name: ")
    price = float(input("Price of Item: "))
    print("Item",i,":",items_name)
    print("Rs: ",price)
    total_bill = total_bill + price
    print(total_bill)

Extra_Items = " "

while Extra_Items != "No":

    Extra_Items = input("Want to Add Something Else: Yes Or No: ").title()
    if Extra_Items == "Yes":
        Extra_Item = input("Extra Item Name: ").title()
        Price_of_Extra_Item = int(input("Price of Item: "))
        print("Extra Item",Extra_Item)
        print(Price_of_Extra_Item)
        total_bill = total_bill + Price_of_Extra_Item
        print(total_bill)
        final_bill = total_bill - (total_bill * discount / 100)
    elif Extra_Items == "No":
        print("Order Finalized")
    else:
        print("Invalid Option")
    
print("Resturant Name :",Resturant_name.strip().title().upper())
print("CUstomer Name: ",Customer_name.strip().title())
print("Membership Type: ",Membership_Type)
print("Total Bill :",total_bill)
print("Your Final Bill: ",final_bill)



