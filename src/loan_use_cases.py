from enums import EquipmentStatus, LoanStatus, RequestStatus, UserRole
from loan import Loan


def deliver_equipments(current_user, request):
    if not current_user.role == UserRole.WAREHOUSE:
        raise ValueError("You are not authorized to deliver the equipments")

    if not request.status == RequestStatus.APPROVED:
        raise ValueError("The request is not approved")

    for equipment in request.equipments:
        if not equipment.status == EquipmentStatus.RESERVED:
            raise ValueError("All equipments must be reserved before deliver")

    for equipment in request.equipments:
        equipment.borrow()

    return Loan(request)


def return_equipments(current_user, loan):
    if not current_user.role == UserRole.WAREHOUSE:
        raise ValueError("You are not authorized to receive the equipments")

    if not loan.status == LoanStatus.ON_GOING:
        raise ValueError("The loan is not on going")

    for equipment in loan.request.equipments:
        if not equipment.status == EquipmentStatus.BORROWED:
            raise ValueError("The equipments must be borrowed before return")

    for equipment in loan.request.equipments:
        equipment.make_available()

    loan.complete_loan()
