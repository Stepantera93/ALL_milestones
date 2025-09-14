from collections import defaultdict
from typing import List, Dict

def generate_salary_report(data: List[Dict[str, str]]) -> Dict[str, float]:
    salary_by_department = defaultdict(list)
    for row in data:
        dept = row['Department']
        salary_by_department[dept].append(int(row['Salary']))

    avg_salary_by_department = {
        dept: sum(salaries) / len(salaries)
        for dept, salaries in salary_by_department.items()
    }

    return avg_salary_by_department

def print_report(report_data: Dict[str, float]) -> None:
    print("Average Salary by Department:")
    for dept, avg_salary in report_data.items():
        print(f"{dept}: ${avg_salary:.2f}")
