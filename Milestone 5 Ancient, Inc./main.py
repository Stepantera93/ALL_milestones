from data_generator import generate_data
from database import read_employee_data
from report import generate_salary_report, print_report

if __name__ == "__main__":
    departments = ["HR", "Engineering", "Sales", "Marketing"]
    min_age = 20
    max_age = 65
    min_salary = 40000
    max_salary = 120000
    num_records = 100
    file_path = "database.csv"

    generate_data(
        file_path=file_path,
        departments=departments,
        min_age=min_age,
        max_age=max_age,
        min_salary=min_salary,
        max_salary=max_salary,
        num_records=num_records
    )

    data = read_employee_data(file_path)
    report = generate_salary_report(data)
    print_report(report)