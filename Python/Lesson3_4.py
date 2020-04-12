expected_salaries = {"NY": 70000, "CA": 70000, "FL": 50000, "NC": 50000, "TX": 60000}  # this is a dictionary
valid_states = ("FL", "NY", "CA", "TX", "NC")  # this is a tuple
is_Still_Looping = True
user_lists = []

while is_Still_Looping:
    try:
        user_full_name = input("Please enter your Full Name: \n")
        user_dob = input("Please enter your Date of Birth (MM/DD/YYYY): \n")
        user_country = input("Enter Country:(Use Country Code ex.USA): \n")

        print(valid_states[0])
        print(valid_states[1])
        print(valid_states[2])
        print(valid_states[3])
        print(valid_states[4])

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
                    
        if user_experience == 1:  # if user_experience chosen is 1
            state_salaries = expected_salaries[user_info["State"]]
            new_expected_salaries = state_salaries - 5000    # 70,000 - 5,000 = $65,000        

            if len(user_coding_languages) < 3:
                new_expected_salaries = new_expected_salaries - 10000   # 65,000 - 10,000 = $55,000
                print("learn some more coding languages; deduct $10k from expected salary.")
            elif len(user_coding_languages) > 3:
                new_expected_salaries = new_expected_salaries + 10000
            else:
                new_expected_salaries = new_expected_salaries + 5000         
            
            if int(number_of_education_years) > 3:
                new_expected_salaries = new_expected_salaries + 5000
            else:
                new_expected_salaries = new_expected_salaries - 5000        
                print('Expect $' + str(new_expected_salaries) + " for your level of experience")
            
        elif user_experience == 2:  # if user_experience chosen is 2
            state_salaries = expected_salaries[user_info["State"]]
            new_expected_salaries = state_salaries - 5000        
            
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
            
        elif user_experience == 3:  # if user_experience chosen is 3
            state_salaries = expected_salaries[user_info["State"]]
            new_expected_salaries = state_salaries - 5000    

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
                
        elif user_experience == 4:  # if user_experience chosen is 4
            state_salaries = expected_salaries[user_info["State"]]
            new_expected_salaries = state_salaries - 5000    
        
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
                
        elif user_experience == 5:  # if user_experience chosen is 5
            state_salaries = expected_salaries[user_info["State"]]
            new_expected_salaries = state_salaries - 5000        
            
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
                print("Expect $" + str(new_expected_salaries) + " for your level of experience")#set your salary here

        user_info["Adjusted_Salary"] = new_expected_salaries

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