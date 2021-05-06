# 1 - imports
from base import Session
from models import Employee, Payroll, Address

# 2 - extract a session
session = Session()

# 3 - extract all movies
employees = session.query(Employee).all()  # All employees
salary_policies = session.query(Payroll).filter(Payroll.weekly_salary != None).filter(Payroll.weekly_salary > 1500)  # All salary policies with weekly salary grater than 1500
addresses = session.query(Address).join(Employee).filter(Employee.role == "secretary").all()  # All addresses of secretaries

# 4 - print details
print('\n### All employees:')
for employee in employees:
    print(f'{employee.name} work on me as {employee.role}')
print('')

for sp in salary_policies:
    print(f"{sp.policy_type}: {sp.weekly_salary}")

for address in addresses:
    print(f"{address.employee.name}: {address.street}: {address.state}")
