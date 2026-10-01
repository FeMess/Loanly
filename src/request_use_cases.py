from enums import UserRole


def cancel_request(current_user, request):
    if not current_user.role == UserRole.EMPLOYEE:
        raise ValueError("You are not in a Employee role to cancel this request")

    if not current_user.id == request.employee.id:
        raise ValueError("You are not responsible for this request")

    request.cancel()
