from datetime import datetime
from random import randint

from enums import UserRole


class User:
    def __init__(self, name, department, role):
        if not isinstance(role, UserRole):
            raise TypeError("Invalid user role")

        # External attributes
        self.name = name
        self.department = department
        self.role = role

        # Internal attributes
        self.id = f"US-{datetime.today().strftime('%d%m%Y')}-{randint(100000, 999999)}"  # noqa: DTZ002
        self.created_date = datetime.now()  # noqa: DTZ005
