from session import Session
from model import Employee, Salary


def main():
    session = Session()

    employee = session.query(Employee).get(1)
    print(employee)

    for salary in employee.salaries:
        print(salary)

    employee.salaries.append(
        Salary(amount=50000, bonus=5000)
    )
    employee.pay(amount=1000, bonus=1000, comments="Monthly salary")
    session.commit()


if __name__ == "__main__":
    main()
