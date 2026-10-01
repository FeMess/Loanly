from datetime import datetime
from random import randint

from enums import RequestStatus


class Request:
    def __init__(self, employee, equipments):
        # External attributes
        self.employee = employee
        self.equipment = equipments
        self.status = RequestStatus.PENDING

        # Internal attributes
        self.id = f"RE-{datetime.today().strftime('%d%m%Y')}-{randint(100000, 999999)}"  # noqa: DTZ002
        self.created_date = datetime.now()  # noqa: DTZ005
