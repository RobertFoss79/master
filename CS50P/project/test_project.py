import pytest
import project
import income
import expenses
import utils

@pytest.fixture
def sample_data():
    return {
        'payroll_income': 1000.0,
        'other_income': 200.0,
        'rent': 800.0,
        'power_gas': 150.0,
        'groceries': 300.0
    }

# Tests for project.py functions
def test_collect_income(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1000')
    payroll_income = income.input_payroll_income()
    assert payroll_income == 1000.0
    
    monkeypatch.setattr('builtins.input', lambda _: '200')
    other_income = income.input_other_income()
    assert other_income == 200.0

def test_collect_expenses(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '800')
    rent = expenses.input_rent()
    assert rent == 800.0
    
    monkeypatch.setattr('builtins.input', lambda _: '150')
    power_gas = expenses.input_power_gas()
    assert power_gas == 150.0

    monkeypatch.setattr('builtins.input', lambda _: '300')
    groceries = expenses.input_groceries()
    assert groceries == 300.0

# Tests for utils.py functions
def test_save_to_file(sample_data):
    filename = 'test_budget_data.csv'
    utils.save_to_file(sample_data, filename)
    
    assert os.path.exists(filename)  # Check if the file has been created

    with open(filename, 'r') as file:
        content = file.read()
        assert 'payroll_income,1000.0' in content
        assert 'rent,800.0' in content

    os.remove(filename)  # Clean up after test

def test_load_from_file(sample_data):
    filename = 'test_budget_data.csv'
    utils.save_to_file(sample_data, filename)
    
    loaded_data = utils.load_from_file(filename)
    
    assert loaded_data == sample_data  # Check if the loaded data matches the sample data
    
    os.remove(filename)  # Clean up after test
