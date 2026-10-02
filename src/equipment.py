from datetime import datetime
from random import randint

from enums import EquipmentStatus


class Equipment:
    def __init__(self, name):
        # External attributes
        self.name = name
        self.status = EquipmentStatus.AVAILABLE

        # Internal attributes
        self.id = f"EQ-{datetime.today().strftime('%d%m%Y')}-{randint(100000, 999999)}"  # noqa: DTZ002

    def reserve(self):
        if not self.status == EquipmentStatus.AVAILABLE:
            raise ValueError(
                "You cannot reserve this equipment. The equipment is not available"
            )

        self.status = EquipmentStatus.RESERVED

    def borrow(self):
        if not self.status == EquipmentStatus.RESERVED:
            raise ValueError("All equipments must be reserved before deliver")

        self.status = EquipmentStatus.BORROWED
