import csv
import random
from typing import List

def generate_data(
    file_path: str,
    departments: List[str],
    min_age: int,
    max_age: int,
    min_salary: int,
    max_salary: int,
    num_records: int
) -> None:
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "Department", "Salary"])

        for i in range(1, num_records + 1):
            writer.writerow([
                i,
                f"Employee{i}",
                random.randint(min_age, max_age),
                random.choice(departments),
                random.randint(min_salary, max_salary)
            ])