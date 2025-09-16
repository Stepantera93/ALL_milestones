import csv
from typing import List, Dict

def read_employee_data(file_path: str) -> List[Dict[str, str]]:
    with open(file_path, newline='') as csvfile:
        return list(csv.DictReader(csvfile))
