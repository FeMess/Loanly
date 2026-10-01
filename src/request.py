from datetime import datetime
from random import randint

from enums import RequestStatus


class Request:
    def __init__(self, employee, equipments):
        # External attributes
        self.employee = employee
        self.equipments = equipments
        self.status = RequestStatus.PENDING

        # Internal attributes
        self.id = f"RE-{datetime.today().strftime('%d%m%Y')}-{randint(100000, 999999)}"  # noqa: DTZ002
        self.created_date = datetime.now()  # noqa: DTZ005

    def cancel(self):
        if not self.status == RequestStatus.PENDING:
            raise ValueError(
                "You cannot cancel this request. The status must be 'Pending'"
            )

        self.status = RequestStatus.CANCELLED

    def reject(self):
        if not self.status == RequestStatus.PENDING:
            raise ValueError(
                "You cannot reject this request. The status must be 'Pending'"
            )

        self.status = RequestStatus.REJECTED
