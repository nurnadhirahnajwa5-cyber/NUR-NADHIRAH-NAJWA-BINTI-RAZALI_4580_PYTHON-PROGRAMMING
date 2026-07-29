from employee import get_employee
from salary import gross_salary, epf, socso, net_salary
from report import print_report


def main():

    employee_name, employee_id, basic_salary, allowance = get_employee()

    gross = gross_salary(basic_salary, allowance)
    epf_amount = epf(gross)
    socso_amount = socso(gross)
    net = net_salary(gross)

    print_report(employee_name,
                 employee_id,
                 basic_salary,
                 allowance,
                 gross,
                 epf_amount,
                 socso_amount,
                 net)


if __name__ == "__main__":
    main()