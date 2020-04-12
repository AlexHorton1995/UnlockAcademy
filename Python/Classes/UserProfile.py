#UserProfile.py
'''
        user_info = {"DOB": user_dob, "Fullname": user_full_name, "Country": user_country, "State": user_state,
                    "is_active": user_is_active, "number_of_education_years": number_of_education_years, "Adjusted_Salary": state_salaries}

'''


class UserProfile:
    #constructor
    def __init__(self, pPass, pName, pAdd1, pAdd2, pCity, pState, pZip, pEmail, pDOB, pCountry, pStatus, pEdYears):
        #use super().__init__() when you are inheriting from a base class.
        #PCI Info
        self.Password = pPass

        #PII Info
        self.FullName = pName
        self.Address1 = pAdd1
        self.Address2 = pAdd2
        self.City = pCity
        self.State = pState
        self.ZipCode = pZip

        self.Email = pEmail
        self.DOB = pDOB
        self.Country = pCountry
        self.IsActive = pStatus

        self.EduYears = pEdYears
        self.AdjSalary = 0

    def UpdateInfo(self):
        pass

    def addStuff(self):
        pass


    