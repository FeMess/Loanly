from datetime import datetime
from random import randint

from enums import EventAction


class Event:
    def __init__(self, actor, action):
        if not isinstance(action, EventAction):
            raise TypeError("Invalid event action")

        # External attributes
        self.actor = actor
        self.action = action

        # Internal attributes
        self.id = f"EV-{datetime.today().strftime('%d%m%Y')}-{randint(100000, 999999)}"  # noqa: DTZ002
        self.created_date = datetime.now()  # noqa: DTZ005
