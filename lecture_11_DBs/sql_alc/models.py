from sqlalchemy import Column, String, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from base import Base

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)

    def __init__(self, name, role):
        self.name = name
        self.role = role


class Payroll(Base):
    __tablename__ = 'payroll'

    id = Column(Integer, primary_key=True)
    policy_type = Column(String)
    weekly_salary = Column(Numeric, nullable=True)
    hourly_rate = Column(Numeric, nullable=True)
    commission = Column(Numeric, nullable=True)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    employee = relationship("Employee")

    def __init__(self, policy_type, employee, weekly_salary=None, hourly_rate=None, commission=None):
        self.policy_type = policy_type
        self.weekly_salary = weekly_salary
        self.hourly_rate = hourly_rate
        self.commission = commission
        self.employee = employee


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    street = Column(String)
    street_2 = Column(String, nullable=True)
    city = Column(String)
    state = Column(String)
    zipcode = Column(String)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    employee = relationship("Employee")

    def __init__(self, street, city, state, zipcode, employee, street_2=None):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.employee = employee
        self.street_2 = street_2
