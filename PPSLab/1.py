print("Enter basic salary: ")
basic=float(input())
HRA=(basic*10)/100
TA=(basic *5)/100
gross_salary=basic+HRA+TA
print("Gross Salary is: ",gross_salary)
PTax=(gross_salary*2)/100
net_salary=gross_salary-PTax
print("Net Salary is:",net_salary)