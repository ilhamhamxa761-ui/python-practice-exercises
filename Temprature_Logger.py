Temprature = int(input("Enter days of Temprature: "))
total = 0

for i in range(1 ,Temprature + 1):
    temprature_of_the_day = float(input("Enter Temprature: "))
    print("Day",i,":",temprature_of_the_day,"c")
    total = total + temprature_of_the_day
    print(total)

Total_Days = Temprature
average_temprature = total / Total_Days
print("Total days",Total_Days)
print("Average Temparature are",average_temprature)

if average_temprature >= 40:
    print("Very hot weather")
elif average_temprature >= 25:
    print("Weather is Normal")
elif average_temprature >= 15:
    print("Weather is Warm")
else:
    print("Weather is cold")
