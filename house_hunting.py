total_cost = float(input("House Price: "))
annual_salary = float(input("Annual Salary: "))
portion_saved = float(input("How much to save each month: "))
r = float(input("How high of a return on investments: "))
downpay_percent = float(input("Percent of total house price for Down-payment: "))

# portion_down_payment = float(total_cost * 0.25)
portion_down_payment = float(total_cost * downpay_percent)

current_savings = float(0)

i = float(0)

monthly_salary = float(annual_salary / 12)
monthly_savings = float(monthly_salary * portion_saved)


while current_savings <= portion_down_payment:
    i += 1
    current_savings += (((current_savings * r) /12) + monthly_savings)
    
    # print(monthly_savings)
    # print(current_savings)
    
    # print("Number of months: " + str(i))

print(current_savings)
print("Number of months: " + str(i))
    


















