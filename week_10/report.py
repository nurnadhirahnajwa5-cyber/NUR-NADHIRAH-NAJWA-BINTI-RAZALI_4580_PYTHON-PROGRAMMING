def print_report(employee_name,
                 employee_id,
                 basic_salary,
                 allowance,
                 gross,
                 epf_amount,
                 socso_amount,
                 net):

    print("\n========== SALARY REPORT ==========")

    print(f"Employee Name : {employee_name}")
    print(f"Employee ID   : {employee_id}")

    print("-----------------------------------")

    print(f"Basic Salary  : RM {basic_salary:.2f}")
    print(f"Allowance     : RM {allowance:.2f}")

    print("-----------------------------------")

    print(f"Gross Salary  : RM {gross:.2f}")
    print(f"EPF (11%)     : RM {epf_amount:.2f}")
    print(f"SOCSO (0.5%)  : RM {socso_amount:.2f}")

    print("-----------------------------------")

    print(f"Net Salary    : RM {net:.2f}")

    print("===================================")