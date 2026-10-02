import request_use_cases
from equipment import Equipment
from request import Request
from user import User, UserRole

equipments_list = []
users_list = []
requests_list = []

if __name__ == "__main__":
    # USERS
    brenda = User("Brenda Magalhães", "Digital", UserRole.MANAGER)
    felipe = User("Felipe Mesquita", "Digital", UserRole.EMPLOYEE)

    # EQUIPMENTS
    notebook = Equipment("Notebook Acer V15")
    equipments_list.append(notebook)

    # FELIPE CRIA REQUEST
    rq1 = Request(felipe, equipments_list)

    print("-" * 30)
    print(rq1.employee.name)
    for equipment in rq1.equipments:
        print(equipment.status)
    print(rq1.status)
    print("-" * 30)

    print()

    # BRENDA APROVA
    request_use_cases.approve_request(brenda, rq1)

    print("-" * 30)
    print(rq1.employee.name)
    for equipment in rq1.equipments:
        print(equipment.status)
    print(rq1.status)
    print("-" * 30)
