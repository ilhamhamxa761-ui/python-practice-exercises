topic = ("Student card generator")
print(topic.center(50,))

Name = input("Enter your name: ")
Name = Name.strip()
Name = Name.title()
Roll_no = int(input("Enter your roll number: "))
print("Enter your marks: ")
Maths = int(input("Maths: "))
English = int(input("English: "))
Science = int(input("Science: "))
Attendace_percentage = float(input("Enter your attendance percentage: "))
Email = input("Enter your Email: ")
Email = Email.strip()
Email = Email.lower()
if "@" in Email and "." in Email:
    print("Valid Email")
else:
    print("Invalid Email")

total_marks = Maths + English + Science
percentage =total_marks / 3
print("Total marks: ", total_marks)
print("Percentage: ",  percentage)

if percentage >= 90:
    Grade = "A+"
    print("Grade: A+")
elif percentage >= 80:
    Grade = "A"
    print("Grade: A")
elif percentage >= 70:
    Grade = "B"
    print("Grade: B")
elif percentage >= 60:
    Grade = "C"
    print("Grade: C")
elif percentage >= 50:
    Grade = "D"
    print("Grade: D")
else:
    Grade = "Fail"
    print("Grade: Fail")

if Attendace_percentage < 60:
    print("""Sorry you are not Eligible for Stident ID generation""")
else:
    print("Warning : your are elible but maintain your attendance")

match Grade:
    case "A+" | "A":
        print("Fabolous")
    case "B" | "C":
        print ("Excelent")
    case "D":
        print("Work Hard")
    case _:
        print("Fail")
