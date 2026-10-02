from enum import Enum


class UserRole(Enum):
    EMPLOYEE = "Employee"
    MANAGER = "Manager"
    WAREHOUSE = "Warehouse"


class EquipmentStatus(Enum):
    AVAILABLE = "Available"
    RESERVED = "Reserved"
    BORROWED = "Borrowed"


class RequestStatus(Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    CANCELLED = "Cancelled"
    EXPIRED = "Expired"


class LoanStatus(Enum):
    ON_GOING = "On Going"
    COMPLETED = "Completed"
    OVERDUE = "Overdue"
