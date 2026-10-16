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
        self.extension_used = False

    def complete_loan(self):
        if not self.status == LoanStatus.ON_GOING:
            raise ValueError("The loan is not on going")

        self.status = LoanStatus.COMPLETED

    def extend_due_date(self, days):
        if not self.status == LoanStatus.ON_GOING:
            raise ValueError("The loan is not on going")

        if self.extension_used:
            raise ValueError("You already request the extension for this loan")

        if not type(days) == int:
            raise ValueError("The quantity of days must be a integer numeric value")

        if not (days > 0 and days < 16):
            raise ValueError("You can just extend the due date for more 15 days")

        self.due_date = self.due_date + timedelta(days=days)
        self.extension_used = True
