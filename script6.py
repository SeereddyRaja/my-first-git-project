income = int(input("Enter your monthly income (in rs): "))
exp1 = int(input("Enter Home Loan EMI (in rs): "))
exp2 = int(input("Enter Credit Card Expenses (in rs): "))
total_exps = exp1 + exp2
remaining_income = income - total_exps
print("Remaining income: ", remaining_income, "rs")
