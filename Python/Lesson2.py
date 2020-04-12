##Module: Lesson 2.py
## This module is the homework for lesson 2 of Unlock Academy's Python Course.
try:
    #Information Collection Section
    user_input = int(input("Please input your experience level. Choose numbers 1-4.\n "
        "[1] Less than 1 year of Experience\n "
        "[2] 2 - 3 years of Experience\n "
        "[3] 3 - 8 years of Experience\n "
        "[4] Over 8 years of Experience\n\n"
        "Enter Your Experience Level: "))

    user_languages = input("And, what development langauges do you have experience in?\n"
        "Seperate your answers with commas: ").split()


    #Logic checks
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

