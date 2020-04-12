##Module: Lesson 1_1.py
## This module is the homework for lesson 1.1 of Unlock Academy's Python Course.

print(
    "Please input your experience level. Choose numbers 1-4.\n "
    "[1] Less than 1 year of Experience\n "
    "[2] 2 - 3 years of Experience\n "
    "[3] 3 - 8 years of Experience\n "
    "[4] Over 8 years of Experience\n"
)

#use a try block to keep the user from inputing garbage into your numeric field.
try:
    #Gather the input from the user
    user_input = int(input("Enter Your Experience Level: "))

    if user_input == 1:
        print("Expect Between $40,000 and $60,000 for your level of experience!")
        pass
    elif user_input == 2:
        print("Expect Between $60,000 and $80,000 for your level of experience!")
        pass
    elif user_input == 3:
        print("Expect Between $80,000 and $100,000 for your level of experience!")
        pass
    elif user_input == 4:
        print("Expect at least $130,000 for your level of experience!")
        pass
    else:
        print("You did not enter a valid selection.")
        pass
except ValueError:
    #This catches entries that the user may enter that will throw an exception :)
    print("You entered an invalid entry!")
    pass
