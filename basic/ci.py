p=int(input("enter the principal amount"))
n=int(input("enter compound interest rate(daily, monthly, quarterly, half-year, yearly"))
r=float(input("enter the rate of interest"))
t=int(input("enter the time"))
si=p*(((1+(r/n))**(n*t)))
print(si)






