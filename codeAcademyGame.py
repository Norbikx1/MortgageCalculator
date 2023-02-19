#Mortgage Calculator by Norbert





def getData():
    
    print ("How much money do you need?") 
    amount = input()
    print("What is the perecentage of the loan?")
    perecentage = input()
    print("For how many year do you want to take the loan?")
    years = input()
    return int(amount), int(perecentage), int(years) 

def calculatePerecentage():
    amount, perecentage, years = getData()
    loanCost = amount * (perecentage /100)
    loanCostOverYears = loanCost * years 
    months = years * 12
    r = perecentage/(100*12)

    monthly_payment = amount*((r*((r+1)**months))/(((r+1)**months)-1)) #formula for 


    totalCost = monthly_payment * months
    print("The monthly repayment will be: " + str(monthly_payment))
    print("With the " + str(perecentage) + "% interest rate")
    print("You will pay back " + str(round(totalCost, 1)) + " if you borrow " + str(amount))
    return monthly_payment





calculatePerecentage( )