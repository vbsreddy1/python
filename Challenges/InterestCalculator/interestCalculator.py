principalAmt = int(input("Enter Priciple Amount:"))
interest = float(input("Enter interest for Rs.100/- :"))

years = int(input("Enter number of years:"))
months = int(input("Enter number of months:"))
days = int(input("Enter number of days:"))

while True:
    if years>= 3:
        numOfHuns = principalAmt/100
        principalAmt = principalAmt+(numOfHuns*interest*36)
        print(principalAmt)
        years=years-3
    else:
        break

numOfHuns = principalAmt/100
monthlyInterest = numOfHuns*interest
print("Monthly Interest:"+str(monthlyInterest))
dailyInterest = monthlyInterest/30
print("Daily Interest:"+str(dailyInterest))
yearlyInterest = monthlyInterest*12
print("Yearly Interest:"+str(yearlyInterest))
finalInterest = (yearlyInterest*years) + (monthlyInterest*months) + (dailyInterest*days)
print("Final Interest:"+str(finalInterest))
finalAmount = principalAmt+finalInterest
print("Final Amount:"+str(finalAmount))
