from enums import UserRole


def cancel_request(current_user, request):
    if not current_user.role == UserRole.EMPLOYEE:
        raise ValueError("You are not in a Employee role to cancel this request")

    if not current_user.id == request.employee.id:
        raise ValueError("You are not responsible for this request")

    request.cancel()


def reject_request(current_user, request):
    if not current_user.role == UserRole.MANAGER:
        raise ValueError("You are not in a Manager role to reject this request")

    if not current_user.department == request.employee.department:
        raise ValueError("You are not the Manager of the Employee requester")

    request.reject()


def approve_request(current_user, request):
    if not current_user.role == UserRole.MANAGER:
        raise ValueError("You are not in a Manager role to approve this request")

    if not current_user.department == request.employee.department:
        raise ValueError("You are not the Manager of the Employee requester")

    request.approve()
