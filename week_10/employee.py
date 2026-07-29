def get_employee():
    print("=== Employee Information ===")

    employee_name = input("Employee Name : ")
    employee_id = input("Employee ID : ")
    basic_salary = float(input("Basic Salary (RM): "))
    allowance = float(input("Allowance (RM): "))

    return employee_name, employee_id, basic_salary, allowance