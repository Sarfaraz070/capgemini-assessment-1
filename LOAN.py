def customer(Salary,age,credit):
    min_salary=400000
    min_age=21
    credit_score=750
    if Salary<min_salary or age<min_age or credit_score<750:
        return f" REJECTED ! Loan cannot be proceesed"
    return f"ACCEPTED! Loan can be processed"
a=int(input("Enter the salary per annum : "))
b=int(input("Enter your age : "))
c=int(input("Enter your Credit score : "))
print(customer(a,b,c))