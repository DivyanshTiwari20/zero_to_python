#To check whether the num is perfect square and prime or not 

user_input=int(input("Enter your number:\n"))
if user_input>1:
    for i in range(2,int(user_input**0.5)+1):
        if user_input%i==0:
            print("NO! The num is not prime.")
            break
    else:
            print("The num is num is prime.")
else:
    print("The num is prime.")

if user_input**0.5== int(user_input**0.5):
     print("Perfect square")
else:
     print("not a perfect square.")
