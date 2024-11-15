import pytest # type: ignore
from case11_3 import Employee

@pytest.fixture
def employee():
    employee = Employee("Yusuf", "Mukhammadov", 10_000)
    return employee

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 15000
    
def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.salary == 20_000
    employee.give_raise(10000)
    assert employee.salary == 30_000
