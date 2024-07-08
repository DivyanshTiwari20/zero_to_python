#checking the given year is leap or not!

user_input=int(input("Enter your desire year:\n"))
if user_input%4==0 and (user_input%100!=0 or user_input%400==0):
    print("leap")
else:
    print("not")
    

        