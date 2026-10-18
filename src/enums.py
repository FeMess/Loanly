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


class EventAction(Enum):
    CREATED = "The request has been created"
    CANCELLED = "The request has been cancelled"
    APPROVED = "The request has been approved"
    REJECTED = "The request has been rejected"
    DELIVERED = "The equipment has been delivered"
    RETURNED = "The equipment has been returned"
