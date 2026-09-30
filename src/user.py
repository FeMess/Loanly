from datetime import datetime
from random import randint


class User:
    def __init__(self, name, department, role):
        # External attributes
        self.name = name
        self.department = department
        self.role = role  # ["Employee", "Warehouse", "Manager"]

        # Internal attributes
        self.id = f"US-{datetime.today().strftime('%d%m%Y')}-{randint(100000, 999999)}"  # noqa: DTZ002
        self.created_date = datetime.now()  # noqa: DTZ005
