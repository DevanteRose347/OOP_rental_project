# Your Program should have the following (this is not an exhaustive list but just base functionality):

# -  There should be some sort of Driver code for users to choose what to do next 

# -  There should be a way to store multiple users and for users to be able to have multiple different properties (This might be done by creating a User Class & a Property class similarly to how we did it with the Codeflix program)

# -  Properties should be able to store multiple different types of expenses (i.e. taxes, mortgage, insurance, etc) and multiple different types of incomes (i.e. rent, laundry, parking, etc)

# -  The ROI needs to be calculated & displayed to the user and should also be stored for that specific property.

class Customer():
    def __init__(self, name):
        self.property_list = []
        self.name = name

    def add_property(self):
        name = input("what's the name of the property you want to add: ")
        property = Properties(name)
        property.calc_expenses()
        property.calc_income()
        property.calc_cashflow()
        property.calc_roi()
        property.display()
       
        
        self.property_list.append(property)


    def display_property(self):
       for prop in self.property_list:
           print(prop.display())


class Properties():
    def __init__(self, name,):
        self.name = name
        self.income =  0
        self.expenses = 0
        self.cashflow = 0
        self.roi = 0
        
    
    def calc_expenses (self):
        self.tax = int(input("what is tax amount: "))
        self.insurance = int(input("what is insurance amount: "))
        self.utilities = int(input("what is utilities amount: "))
        self.electric = int(input("what is electric amount: "))
        self.water = int(input("what is water amount: "))
        self.sewer = int(input("what is sewer amount: "))
        self.garbadge = int(input("what is garbadge amount: "))
        self.gas = int(input("what is gas amount: "))
        self.hoa = int(input("what is hoa amount: "))
        self.vacancy = int(input("what is vacancy amount: "))
        self.repairs = int(input("what is repairs amount: "))
        self.capex = int(input("what is capex amount: "))
        self.property_Manage = int(input("what is propert_manage amount: "))
        self.mortgage = int(input("what is mortgage amount: "))
        self.expenses = self.tax + self.insurance + self.utilities + self.electric + self.water + self.sewer + self.garbadge + self.gas + self.hoa + self.vacancy + self.repairs + self.capex + self.property_Manage + self.mortgage
        return self.expenses 

    def calc_income (self):
        self.income = int(input(" How much income does the property produce: "))
        return self.income
 

    def calc_cashflow (self):
        self.cashflow = self.income - self.expenses
        return self.cashflow
    
    def calc_roi (self):
        self.down_payment = int(input("what was you down payment: "))
        self.closing_costs = int(input("what was your closing costs: "))
        self.rehab_budget = int(input("what is your rehab budget: "))
        self.roi = self.down_payment + self.closing_costs + self.rehab_budget
        return self.roi


    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print(f"tax: {self.tax}")
        print(f"insurance: {self.insurance}")
        print(f"utilites: {self.utilities}")
        print(f"water: {self.water}")
        print(f"sewer: {self.sewer}") 
        print(f"garbadge: {self.garbadge}") 
        print(f"gas: {self.gas}") 
        print(f"hoa: {self.hoa} ") 
        print(f" vacancy: {self.vacancy}") 
        print(f"repairs: {self.repairs}") 
        print(f"capex {self.capex}") 
        print(f"property_Manage: {self.property_Manage}")
        print(f" mortgage: {self.mortgage}") 
        print(f" Total expenses: {self.expenses}")
        print(f"Property Income: {self.income}")
        print(f"Cash flow: {self.cashflow}")
        print(f"Down payment: {self.down_payment }")
        print(f"Closing cost: {self.closing_costs} ")
        print(f" Rehab budget: {self.rehab_budget}")
        print(f"ROI: {self.roi}")
def run():
    my_custo = Customer('mark') 

    while True:
        response = input("What would you like to do?:add_property, display_property, Exit: ").lower().strip()
        if response == 'add_property':
             my_custo.add_property()
        elif response == 'display_property':
            my_custo.display_property()
        else:
            print("Thank you for Coming!")

run()

