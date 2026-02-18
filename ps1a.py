
annual_salary = float(input("Enter your annual salary: "))
save_percent = float(input("Enter the percent of your salary to save, as a decimal: "))
house_cost = float(input("Enter the cost of your dream home: "))

current_saving = 0.0 
month = 0
rate = 0.04
down_payment = house_cost * 0.25
monthly_salary = annual_salary / 12

while current_saving < down_payment:
    current_saving = current_saving + (current_saving * rate / 12)
    current_saving = current_saving + (monthly_salary * save_percent)
    month = month + 1

print("Number of months:", month) 
