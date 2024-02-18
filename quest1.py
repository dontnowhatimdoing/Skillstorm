import csv


class Expense:
    dept_name: str
    expense_amount: float

    def __init__(self, dept_name, expense_amount):
        self.dept_name = dept_name
        self.expense_amount = expense_amount


with open("city-of-seattle-2012-expenditures-dollars.csv") as file:
    reader = csv.reader(file, delimiter=",")
    expense_list = []
    row_number = 1
    for list in reader:
        if row_number !=1:
            expense = Expense(list[0], list[3])
            expense_list.append(expense)
            row_number += 1
        else:
            row_number += 1


expense_dict = {}
for item in expense_list:
    if item.expense_amount == '':
        continue

    temp_amt = int(item.expense_amount)

    if not(item.dept_name in expense_dict):
        expense_dict[item.dept_name] = [temp_amt]
    else:
        expenses = expense_dict[item.dept_name]
        expenses.append(temp_amt)
        expense_dict[item.dept_name] = expenses


for department in expense_dict.keys():
    total_expenses = sum(expense_dict.get(department))
    print("department: " + department + " spent $" + str(total_expenses))