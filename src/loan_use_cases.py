from enums import EquipmentStatus, RequestStatus, UserRole
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
