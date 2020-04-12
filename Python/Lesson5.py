############################
#   Lesson 5 - Custom Functions
#   Author: alexhortdog95
#   Date:  04/12/2020
#   Purpose:  Learn how to create custom functions in Python code.
#############################

expected_salaries = {"NY": 70000, "CA": 70000, "FL": 50000, "NC": 50000, "TX": 60000}  # this is a dictionary
valid_states = ("FL", "NY", "CA", "TX", "NC")  # this is a tuple
is_Still_Looping = True
new_expected_salaries = 0
user_lists = []


def calculate_salary(userinfo, exp, state, langs, edyears):
    state_sals = expected_salaries[state]
    new_expected_salaries = state_sals - 5000    # 70,000 - 5,000 = $65,000        

    if exp == 1:
        new_expected_salaries = state_sals - 5000

        if len(langs) < 3:
            new_expected_salaries = new_expected_salaries - 10000   # 65,000 - 10,000 = $55,000
            print("learn some more coding languages; deduct $10k from expected salary.")
        elif len(langs) > 3:
            new_expected_salaries = new_expected_salaries + 10000
        else:
            new_expected_salaries = new_expected_salaries + 5000         
                
        if int(edyears) > 3:
            new_expected_salaries = new_expected_salaries + 5000
        else:
            new_expected_salaries = new_expected_salaries - 5000        

    elif exp == 2:
            new_expected_salaries = state_sals - 5000        
            
            if len(user_coding_languages) < 3:
                new_expected_salaries = new_expected_salaries - 10000
                print("learn some more coding languages; deduct $10k from expected salary")
            elif len(user_coding_languages) > 3:
                new_expected_salaries = new_expected_salaries + 10000
            else:
                new_expected_salaries = new_expected_salaries + 5000    
            
            if int(number_of_education_years) > 3:
                new_expected_salaries = new_expected_salaries + 5000
            else:
                new_expected_salaries = new_expected_salaries - 5000        
                print("Expect $" + str(new_expected_salaries) + " for your level of experience")

    elif exp == 3:
            new_expected_salaries = state_sals - 5000    

            if len(user_coding_languages) < 3:
                new_expected_salaries = new_expected_salaries - 10000
                print("learn some more coding languages; deduct $10k from expected salary")
            elif len(user_coding_languages) > 3:
                new_expected_salaries = new_expected_salaries + 10000
            else:
                new_expected_salaries = new_expected_salaries + 5000    
            
            if int(number_of_education_years) > 3:
                new_expected_salaries = new_expected_salaries + 5000
            else:
                new_expected_salaries = new_expected_salaries - 5000        
                print("Expect $" + str(new_expected_salaries) + " for your level of experience")

    elif exp == 4:
            new_expected_salaries = state_sals - 5000    
        
            if len(user_coding_languages) < 3:
                new_expected_salaries = new_expected_salaries - 10000
                print("learn some more coding languages; deduct $10k from expected salary")
            elif len(user_coding_languages) > 3:
                new_expected_salaries = new_expected_salaries + 10000
            else:
                new_expected_salaries = new_expected_salaries + 5000    
                
            if int(number_of_education_years) > 3:
                new_expected_salaries = new_expected_salaries + 5000
            else:
                new_expected_salaries = new_expected_salaries - 5000        
                print("Expect $" + str(new_expected_salaries) + " for your level of experience")

    return new_expected_salaries
    

while is_Still_Looping:
    try:
        user_full_name = input("Please enter your Full Name: \n")
        user_dob = input("Please enter your Date of Birth (MM/DD/YYYY): \n")
        user_country = input("Enter Country:(Use Country Code ex.USA): \n")

        for states in valid_states:
            print(states)

        state_salaries = 0

        user_state = input("Choose your State (use the 2 letter abbreviation): \n")

        user_is_active = True

        user_experience = input("How many years experience do you have developing software?\n[1] Less than 1 year"
                                "\n[2] 1-3 years of experience  \n[3] 3-8 years of experience  \n[4]"
                                " 8+ years of experience \n")
        user_experience = int(user_experience)

        number_of_education_years = input("Please enter how many years you have been learning to code:\n")

        user_coding_languages = input("Which coding languages do you know? (seperate each language by commas):\n")

        user_info = {"DOB": user_dob, "Fullname": user_full_name, "Country": user_country, "State": user_state,
                    "is_active": user_is_active, "number_of_education_years": number_of_education_years, "Adjusted_Salary": state_salaries}

        user_info["Adjusted_Salary"] = calculate_salary(user_info, user_experience, user_state, user_coding_languages, number_of_education_years)

        if len(user_full_name) < 5:
            print("Error:Complete Full Name")

        if len(user_state) < 2:
            print("Error: Enter Correct State")
        elif len(user_state) > 2:
            print("Error: Enter Correct State Code")
            
        if len(user_country) > 3:
            print("Error: Enter Correct Country Code")
        elif len(user_country) < 2:
            print("Error: Enter Correct Country Code")

        additional_users = str(input("Do you want to enter more records?")).upper()

        user_lists.append(user_info)

        if additional_users != "Y":
            is_Still_Looping = False
                        
        pass
    except Exception as ex:
        print ("There was an exception in the code.  Please contact support for resolution")
        pass

else:
    for rec in user_lists:
        print(rec)

    pass