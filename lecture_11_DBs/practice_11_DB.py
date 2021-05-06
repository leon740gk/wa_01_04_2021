# RDBMS basics ================================================================

# https://www.tutorialspoint.com/sql/sql-rdbms-concepts.htm
# https://habr.com/ru/company/mailru/blog/266811/

# RDBMS commands ==============================================================

# https://www.tutorialspoint.com/postgresql/postgresql_environment.htm

# SQLAlchemy =================================================================

# https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/

# NoSQL ======================================================================

# https://www.guru99.com/nosql-tutorial.html
# https://www.trustradius.com/nosql-databases



# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
# Install PostgreSQL https://www.postgresqltutorial.com/install-postgresql/
# psql ("\l" - list DBs, "\c" - Connect to DB, "\dt" - list of relations, "\d table_name" - list table schema)

# CREATE TABLE Employee (ID INT PRIMARY KEY NOT NULL, NAME CHAR(50) NOT NULL, ROLE CHAR(100));
# CREATE TABLE Payroll (ID INT PRIMARY KEY NOT NULL, POLICY_TYPE CHAR(100) NOT NULL, WEEKLY_SALARY REAL, HOURLY_RATE REAL, COMMISSION REAL, EMP_ID INT references EMPLOYEE(ID));
# CREATE TABLE Address (ID INT PRIMARY KEY NOT NULL, STREET CHAR(50) NOT NULL, STREET_2 CHAR(50), CITY CHAR(50) NOT NULL, STATE CHAR(50) NOT NULL, ZIPCODE CHAR(50) NOT NULL);

# INSERT INTO Employee (ID, NAME, ROLE) VALUES (1, 'Mary Poppins', 'manager');
# INSERT INTO Employee (ID, NAME, ROLE) VALUES (2, 'John Smith', 'secretary');
# SELECT * FROM employee;
# INSERT INTO Employee VALUES (3, 'Kevin Bacon', 'sales'), (4, 'Jane Doe', 'factory'), (5, 'Robin Williams', 'secretary');

# Forgot FK? NP :)
# UPDATE Payroll SET emp_id = 1 WHERE ID = 1;
# INSERT INTO Payroll VALUES (2, 'SalaryPolicy', 1500, NULL, NULL, 2), (3, 'CommissionPolicy', 1000, NULL, 100, 3), (4, 'HourlyPolicy', NULL, 15, NULL, 4), (5, 'HourlyPolicy', NULL, 9, NULL, 5);
# SELECT * FROM Payroll;

# SELECT name, role FROM employee;
# SELECT policy_type FROM payroll WHERE weekly_salary is not NULL AND weekly_salary > 1200;
# SELECT * FROM payroll WHERE weekly_salary is not NULL and commission is not NULL;
# SELECT * FROM payroll WHERE policy_type = 'CommissionPolicy';

# # Find out what type of policies managers have!
# SELECT emp.name, prl.policy_type, emp.role
# FROM Payroll as prl
# JOIN Employee as emp
# ON prl.emp_id = emp.ID
# WHERE emp.role = 'manager';

# Connect to PyCharm's DB UI
# Execute some queries...




