# 1 - imports
from base import Session, engine, Base
from models import Employee, Address, Payroll

# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# 4 - create employees
marry_poppins = Employee('Mary Poppins', 'manager')
john_smith = Employee('John Smith', 'secretary')
kevin_bacon = Employee('Kevin Bacon', 'sales')

# 5 - create Payroll policies
marry_poppins_manager = Payroll(
    policy_type="SalaryPolicy",
    weekly_salary=3000,
    employee=marry_poppins,
)
john_smith_secretary = Payroll(
    policy_type="SalaryPolicy",
    weekly_salary=1500,
    employee=john_smith,
)
kevin_bacon_sales = Payroll(
    policy_type="CommissionPolicy",
    weekly_salary=1000,
    commission=100,
    employee=kevin_bacon,
)

# 6 - create addresses
marry_poppins_address = Address(
    street='121 Admin Rd.',
    city='Concord',
    state='NH',
    zipcode='03301',
    employee=marry_poppins,
)
john_smith_address = Address(
    street='67 Paperwork Ave',
    city='Manchester',
    state='NH',
    zipcode='03101',
    employee=john_smith,
)
kevin_bacon_address = Address(
    street='15 Rose St',
    city='Concord',
    state='NH',
    zipcode='03301',
    street_2='Apt. B-1',
    employee=kevin_bacon,
)

# 7 - persists data
session.add(marry_poppins)
session.add(john_smith)
session.add(kevin_bacon)
session.add(marry_poppins_manager)
session.add(john_smith_secretary)
session.add(kevin_bacon_sales)
session.add(marry_poppins_address)
session.add(john_smith_address)
session.add(kevin_bacon_address)

# 8 - commit and close session
session.commit()
session.close()
