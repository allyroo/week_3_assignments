state_taxes = {
    'AK':0.010, 'AL':0.003, 'AR':0.006, 'AZ':0.006, 'CA':0.007, 'CO':0.005, 'CT':0.024, 'DE':0.005,
    'FL':0.008, 'GA':0.009, 'HI':0.002, 'IA':0.016, 'ID':0.007, 'IL':0.023, 'IN':0.008, 'KS':0.014, 'KY':0.015, 
    'LA':0.006, 'MA':0.001, 'MD':0.010, 'ME':0.014, 'MI':0.002, 'MN':0.013, 'MO':0.010, 'MS':0.008, 'MT':0.008, 
    'NC':0.008, 'ND':0.009, 'NE':0.017, 'NH':0.021, 'NJ':0.025, 'NM':0.008, 'NV':0.006, 'NY':0.017, 'OH':0.015, 
    'OK':0.009, 'OR':0.010, 'PA':0.020, 'RI':0.020, 'SC':0.006, 'SD':0.013, 'TN':0.007, 'TX':0.018, 'UT':0.006, 
    'VA':0.008, 'VT':0.019, 'WA':0.009, 'WI':0.002, 'WV':0.006, 'WY':0.006
}


import time

class ROI():

    def __init__(self,tax_rate,total_income={},expenses = 0,price = 0):
        self.expenses = expenses
        self.total_income = total_income 
        self.tax_rate = tax_rate
        self.price = price
        

    def calculateIncome(self):  
        bsr = int(input("What is your base rental income? $"))
        print(f"Base rental income: {bsr}")
        while True:
            add_income = input("\nDo you have any additional income to add? yes/no ")
            if add_income.lower() == 'yes':
                type_income = input("What type of income? ")
                value_income = int(input(f"What is the monthly value of your {type_income}? $"))
                self.total_income[type_income.title()] = value_income
            elif add_income.lower() == 'no':
                self.total_income = sum(self.total_income.values()) + bsr
                print(f"Your Total Monthly Income: ${self.total_income}")
                break
            else:
                print("Invalid entry")
        

    def calculateExpenses(self):
        print(self.total_income) #will print dictionary of values
        property_taxes = int(input("Please input your property's value to calculate your monthly average tax rate: $")) * self.tax_rate // 12
        print(f"Monthly Tax Rate: {property_taxes}")

        print("Please input what you would pay in a month on average: ")
        
        insurance = int(input("Enter property insurance: $")) 
        
        hoa = input("Are there any HOA fees? yes/no ")
        while True:
            if hoa.lower() == "yes":
                hoa_fee = int(input("Please input HOA cost: $"))
                break
            elif hoa.lower() == "no":
                hoa_fee = 0
                break
            else:
                print("Invalid response. Try again.")
        
        
        print("""   Utility Costs
         - - - - - - - - -
        """)
        water = int(input("Enter Water: $"))
        sewer = int(input("Enter Sewer: $"))
        garbage = int(input("Enter Garbage: $"))
        electrical = int(input("Enter Electrical: $"))
        gas = int(input("Enter Gas: $"))
        utilities = water + sewer + garbage + electrical + gas
        print(f"Total Utilities Cost: ${utilities}")
        
        vacancy = int(input("Vacancy rate: $"))
        management = int(input("Property Management rate: $"))
        mortgage = int(input("Enter mortgage: $"))
        
        self.expenses = hoa_fee + utilities + insurance + vacancy + management + mortgage + property_taxes
        print(f"Your Total Expenses: ${self.expenses}")
        


    def calculateCashFlow(self):
        if self.total_income == {}:
            print("\nPlease calculate your income first.")
        elif self.expenses == 0:
            print("\nPlease calculate your expenses first.")
        else:
            print("\nCalculating your monthly cash flow...")
            self.price = self.total_income - self.expenses
            time.sleep(5)
            print(f"TOTAL CASH FLOW: ${self.price}")


    def cashOnCashROI(self):
        if self.total_income == {}:
            print("\nPlease calculate your income first.")
        elif self.expenses == 0:
            print("\nPlease calculate your expenses first.")
        elif self.price == 0:
            print("\nPlease calculate your cash flow first.")
        else:
            down = int(input("Enter down payment on property: $"))
            closing = int(input("Enter closing costs $"))
            rehab = int(input("Enter rehab fees $"))
            misc = int(input("Enter miscellaneous costs $"))
            investment = down + closing + rehab + misc
            print(f"TOTAL INVESTMENT: ${investment}")
            print("Calculating your property's return on investment...")
            time.sleep(5)
            roi = self.price / investment * 100
            print(f"Your ROI is {roi}%")

    

# blueHouse = ROI(state_taxes[state])
def run():
    state = input("Please input the two-letter abbreviation of the state your property resides: ")
    property = ROI(state_taxes[state]) 
    while True:
              
        print("""Return On Investment Calculator - 
        - - - - - - - - -
        1. Calculate Income
        2. Calculate Expenses
        3. Calculate Cash Flow
        4. Calculate Return on Investment
        5. Quit
         - - - - - - - - -
        """)
        response = input("Please input a number: ")
        if response == '1':
            property.calculateIncome()
        elif response == '2':
            property.calculateExpenses()
        elif response == '3':
            property.calculateCashFlow()
        elif response == '4':
            property.cashOnCashROI()
        elif response == '5':
            print("Shutting down... Thank you!")
            break
        else:
            print("Invalid entry.")
        
       
run()    



