from datetime import datetime
from random import randint

from enums import EquipmentStatus


class Equipment:
    def __init__(self, name, status):
        # External attributes
        self.name = name
        self.status = EquipmentStatus.AVAILABLE

        # Internal attributes
        self.id = f"EQ-{datetime.today().strftime('%d%m%Y')}-{randint(100000, 999999)}"  # noqa: DTZ002
