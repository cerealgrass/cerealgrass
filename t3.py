# n = input("whats ur phone number")
# while True:
#     if n.startswith("9" or "8"):
#         print ("phone number recognised")
#         break
#     else:
#         print ("invalid phone number must start with 9 or 8")
# e = input("valid singapore company email address: ")
# while True:
#     if e.endswith(".sg"):
#         print ("email accepted")
#         break
#     else:
#         print ("invalid email must end with .sg")
#cereals = ["froot loops","kelloggs","capn crunch","lucky charms","honeycomb","general millis"]
#               0             1           2              3             4              5
# cereals[2] = "skibidi crunch"
# print (cereals)
# cereals.append("literal rocks")
# print (cereals)
# cereals.insert(0,"32 degree oatmeal")
# print (cereals)
######
# del(cereals[3])
# print (cereals)
#or
#cereals.remove("lucky charms")
#print cereals
######
#pop() removes last item
#cereals.pop()
#len() checks length
#loop thru
#for p in cereals:
#   print ("someday i will eat",p)
#other way 2 loop
# for i in range(len(cereals)):
#     print (cereals[i])
#     cereals[i]= "new " + cereals[i]
#     print (cereals)
# '''
# 2020 - Task 2 [10]
# The following program checks it the personal identification number (PIN) 
# entered for a locker is correct. There are 10 lockers available and the 
# correct PIN for each locker is stored in an array.
# A PIN cannot start with the digit 0.

# The program allows the user to enter the number of the locker they 
# want to open, and a PIN. It checks if the PIN is correct for that locker.
# '''
# # arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# # locker = int(input("Please enter the locker you would like to open: "))
# # pin = int(input("PLease enter the PIN for the locker: "))
# # if pin == arraypins[locker-1]:
# #     print("The locker is open.")
# # else: 
# #     print("Incorrect PIN for that locker")

# '''
# 1.	Edit the program so that it converts the PIN input 
# by the user to an integer.
# Save your program
# [1] 
# '''
# # arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# # locker = int(input("Please enter the locker you would like to open: "))
# # pin = int(input("PLease enter the PIN for the locker: "))
# # if pin == arraypins[locker-1]:
# #     print("The locker is open.")
# # else: 
# #     print("Incorrect PIN for that locker")


# '''
# 2.	Edit the program to only accept a locker number between 1 and 10 
# (inclusive) to be input. A suitable error message must be displayed 
# if the locker number input is not in this range. The program must 
# loop until a valid locker number is input.
# Save your program.
# [3]
# '''
# # arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# # locker = int(input("Please enter the locker you would like to open: "))
# # while True:
# #     if len(locker) >= 1 and len(locker) <= 10:
# #         print ("ok locker number")
# #         break
# #     else:
# #         print ("invalid locker number")
# # pin = int(input("PLease enter the PIN for the locker: "))
# # if pin == arraypins[locker-1]:
# #     print("The locker is open.")
# # else: 
# #     print("Incorrect PIN for that locker")

# '''
# 3.	Edit the program to only accept a PIN of 4 digits to be 
# entered by the user. A suitable error message must be displayed 
# if an incorrect input is given. The program must loop until the PIN 
# input is 4 digits.
# Save your program
# [3]
# '''
# # arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]

# # while True:
# #     locker = int(input("Please enter the locker you would like to open: "))
# #     if locker >= 1 and locker <= 10:
# #         print ("ok locker number")
# #         break
# #     else:
# #         print ("invalid locker number")
# # while True: 
# #     pin = int(input("PLease enter the PIN for the locker: "))
# #     if pin >= 1000 and pin <= 9999:
# #         print ("ok pin size")
# #         break
# #     else:
# #         print ("invalid locker pin size")
# # if pin == arraypins[locker-1]:
# #     print("The locker is open.")
# # else: 
# #     print("Incorrect PIN for that locker")


# '''
# 4.	Edit the program to loop until the user inputs both a 
# correct locker number and the matching PIN for that locker.
# Save your program.
# [3]
# '''
# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]

# while True:
#     while True:
#         locker = int(input("Please enter the locker you would like to open: "))
#         if locker >= 1 and locker <= 10:
#             print ("ok locker number")
#             break
#         else:
#             print ("invalid locker number size")
#     while True: 
#         pin = int(input("PLease enter the PIN for the locker: "))
#         if pin >= 1000 and pin <= 9999:
#             print ("ok pin size")
#             break
#         else:
#             print ("invalid locker pin size")

#     if pin == arraypins[locker-1]:
#         print("The locker is open.")
#         breaks
#         print("Incorrect PIN for that locker")
# sp = {'q':7.5,'w':15,'e':25,'r':30}
# wallet = 100
# while True:
#     b = input("what do you want to buy press k to quit")
#     if money <=0:

#     if b == 'k':
#         print ('ok bai bai')
#         break
#     elif b == 'q' :
#         print ("q costs 7.5")
#         wallet -= 7.5
#         print ("you have",wallet,"left")
#     elif b == 'w':
#         print ('w costs 15')
#         wallet -= 15
#         print ("you have",wallet,"left")
#     elif b == 'e':
#         print ('e costs 25')
#         wallet -= 25
#         print ("you have",wallet,"left")
#     elif b == 'r':
#         print ('r costs 30')
#         wallet -= 30
#         print ("you have",wallet,"left")
#     else:
#         print ("i dont have that.")


































































































































































































































































































































































































































































































3334343333333333333

























































































































































































































































































































































































