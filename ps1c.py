

annual_salary = float(input("Enter the starting salary: "))

total_cost = 1000000
down_payment = total_cost * 0.25
rate = 0.04
semi_raise = 0.07
months = 36

low = 0
high = 10000
steps = 0
epsilon = 100

# First check if possible with 100% saving
current_saving = 0
temp_salary = annual_salary
monthly_salary = temp_salary / 12

for i in range(months):
    current_saving += current_saving * rate / 12
    current_saving += monthly_salary
    if (i + 1) % 6 == 0:
        temp_salary += temp_salary * semi_raise
        monthly_salary = temp_salary / 12

if current_saving < down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    while True:
        steps += 1
        mid = (low + high) // 2
        save_percent = mid / 10000
        
        current_saving = 0
        temp_salary = annual_salary
        monthly_salary = temp_salary / 12
        
        for i in range(months):
            current_saving += current_saving * rate / 12
            current_saving += monthly_salary * save_percent
            if (i + 1) % 6 == 0:
                temp_salary += temp_salary * semi_raise
                monthly_salary = temp_salary / 12
        
        if abs(current_saving - down_payment) <= epsilon:
            print("Best savings rate:", round(save_percent,4))
            print("Steps in bisection search:", steps)
            break
        elif current_saving < down_payment:
            low = mid
        else:
            high = mid


