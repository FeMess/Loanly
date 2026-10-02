from datetime import datetime, timedelta
from random import randint

from enums import LoanStatus, RequestStatus


class Loan:
    def __init__(self, request):
        if not request.status == RequestStatus.APPROVED:
            raise ValueError("This request is not approved")

        # External attributes
        self.request = request

        # Internal attributes
        self.id = f"LO-{datetime.today().strftime('%d%m%Y')}-{randint(100000, 999999)}"  # noqa: DTZ002
        self.status = LoanStatus.ON_GOING
        self.start_date = datetime.now()  # noqa: DTZ005
        self.due_date = self.start_date + timedelta(days=30)
