# pas = "froot loops"
# gp = input("whats the password ")
#     if gp == pas:
#         print ('yeah ok')
#     else:
#         print ("nuh uh")
# import random
# score = random.randint(1,100)
# print ("your score is", score)
# elif score >= 80:
# print ("should have gotten 90")
# elif score >= 70:
#     print ("A for average")
# elif score >= 60:
#     print ("B for ur a bum")
# elif score >= 50:
#     print ("C deez nuts")
# elif score <= 49:
#     print ("stoning in the town square ")
# pn = int(input("how many pens "))
# if pn >= 100:
#     print ("whatchu gonna do with",pn,"pens bruh")
#     print ("ur total is",pn*5*0.9)
# else:
#     print ("ur total is",pn*5)
# import random
# an = random.randint(1,100)
# print(an)
# for i in range (6):
#     pn = int(input("what number do you choose "))
#     if pn > an:
#         print ("too big")
#     elif pn < an:
#         print ("too small")
#     else:
#         print ("huh you got it somehow")
#         break
#     if i == 5:
#         print ("heres a chance")
#         if (an % 2) == 0:
#             print ("The number is even")
#         else:
#             print ("The provided number is odd")
#         fn = int(input("last chance kid "))
#         if fn == an:
#             print ("bro needed help lol correct ")
#         else:
#             print("oh my god you suck")
#             print("the number was",an)
# a1 = input ("enter animal ")
# a2 = input ("enter animal ")
# a3 = input ("enter animal ")
# if a1 == "monkey"  or a2 == "monkey" or a3 == "monkey":
#     print ("go bananas")
# else:
#     print ("boring ahh zoo")
# while true:
#     t = input("wdy to spit on that thang")
#     if t == "exit" :
#         print ("that will be your first edge sesh")
#         break 
#     else:
#         print("added",t)
# import random
# for i in range (3):
#     n1 = random.randint(30,70)
#     n2 = random.randint(30,70)
#     while True:
#         ui = int(input("what is {} + {}? ".format(n1,n2)))
#         if ui == n1 + n2:
#             print ("correct")
#             break
#         else:
#             print("skill issue")
# while True:
#     otp = input("What is the otp ")
#     if len(otp) != 4:
#         print("otp must be 4 digits bro")
#     else:
#         print("otp correct")
#         break

'''
Question 3 (Range Check):
Write the input entry and validation code for a program 
that needs to accept a secondary student's age.

The age must be between 13 and 16 inclusive.

If the input is invalid, your code should keep trying 
by asking for the input to be entered again.

Sample output:
Enter age: 12
Invalid input. Age must be between 13 and 16.
Enter age: 20
Invalid input. Age must be between 13 and 16.
Enter age: 16
Age accepted.
'''
# while True:
#      otp = input("What is age ")
#      if otp in range (13,16):
#         ("kid accepted")
#         break
#      else:
#          print("kid must be 13-16")
while True:
    n = input("input user {must be lowercase}")
    if n.islower():
        print ("user accepted")
        break
    else:
        print ("user not accepted try again it gotta be lowercase")



















































































