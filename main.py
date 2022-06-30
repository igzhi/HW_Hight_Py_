from application.salary import calculate_salary
from application.db import people as p


if __name__ == '__main__':
    calculate_salary()
    p.get_employees()

