topic = ("GYM MEMBERSHIP")
topic = topic.center(50)
print(topic)

Member_name = (input("Enter Your Name: " ))
Email = (input("Enter your email: "))
Member_ship_type = (input("Basic , Premium , elite: "))
Member_ship_type = Member_ship_type.lower()
    
match Member_ship_type:
    case "basic":
        print("basic Fee is Rs.2000/month")
    case "premium":
        print("Premium Fee is Rs.3500/ month")
    case "elite":
        print("Elite Fee is Rs.5000/month")
    case _:
        print("Invalid Membership Type")
Workout_Days = int(input("Number of workout days: "))


for i in range(Workout_Days):
    excercise_type = (input("Enter you excercise type (cardio/yoga/weight traning): "))
    duaration = (input("Enter durantion: "))
    print("day", i, excercise_type,"=", duaration, "minutes")
     
     


