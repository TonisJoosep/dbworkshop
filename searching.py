from sqlalchemy import or_, not_, and_

from session import Session
from model import Salary


def main():
    session = Session()

    # result = session.query(Salary).filter(
    #     not_(
    #         or_(
    #             Salary.amount > 100_000,
    #             Salary.bonus != 0
    #         )
    #     )
    # )
    # result = session.query(Salary).filter_by(
    #     amount=150_000, bonus=400
    # )
    result = session.query(Salary).filter(
        and_(
            Salary.amount == 150_000,
            Salary.bonus == 400
        )
    )
    for salary in result:
        print(salary, salary.bonus, salary.employee)


if __name__ == "__main__":
    main()
