
import csv
from pathlib import Path


loan_costs = [500, 600, 200, 1000, 450]

#Total number of loans.
len(loan_costs)

print(f"The total number of loans is: {len(loan_costs)}")

# sum of all loans.
sum_result=sum(loan_costs)
print(f"The total of all loans is: {sum_result}")

# average price of loans
total_loan_costs= 2750
total_number_of_loans= 5
average_price = total_loan_costs / total_number_of_loans

print(f"The average loan price is:${average_price}")


loan = {
    "loan_price": 500,
   "remaining_months": 9,
    "repayment_interval": "bullet",
   "future_value": 1000,
}

#Calculation to determine present value of loan
future_value= 1000
discount_rate= .20
remaining_months= 9
present_value = future_value / (1 + discount_rate/12) ** remaining_months
print(f"The present value of the loan is: {present_value}")

# conditional statement to determine if the loan is a fair value.
average_loan_price=550
present_value= 862
future_value=1000
if present_value - future_value:
    print("This a fair deal!")

else:
    print("This is not a fair deal")



new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}


present_value = new_loan["loan_price"] -0.20



print(f"The present value of the loan is:${present_value}")




loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
       "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# list of loans $500 or less
inexpensive_loans=[]


for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)


print(f"Loans $500 or less: {inexpensive_loans}")


import csv



header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]


output_path = Path("inexpensive_loans.csv")
with open(output_path, "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    for loan in inexpensive_loans: 
        csvwriter.writerow(loan.values())
        print(loan.values())