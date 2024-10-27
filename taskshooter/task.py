import logging
from abc import ABC, abstractmethod
from datetime import datetime

from .trigger import Trigger

logger = logging.getLogger(__name__)


class Task(ABC):
    def __init__(self, name: str, trigger: Trigger, emoji: str = None):
        self.name: str = name
        self.emoji: str = emoji
        self.trigger: Trigger = trigger

        self.stated_at: datetime = None
        self.finished_at: datetime = None

    @abstractmethod
    def execute(self):
        raise NotImplementedError()

    def run(self, force: bool = False, manual: bool = False):
        if not force:
            if not self.trigger.check():
                return

        self.info("running task...")

        self.stated_at = datetime.now()
        self.pre_run()

        try:
            self.execute()
            self.finished_at = datetime.now()
            self.info(f"completed successfully in {self.runtime}ms")

            self.post_run(manual=manual, exception=None)
        except Exception as exception:
            self.exception(exception)
            self.finished_at = datetime.now()

            self.post_run(manual=manual, exception=exception)

    def pre_run(self):
        pass

    def post_run(self, manual: bool = False, exception: Exception = None):
        pass

    @property
    def is_running(self) -> bool:
        return bool(self.stated_at and not self.finished_at)

    @property
    def runtime(self) -> float:
        if not self.finished_at:
            return None

        return int((self.finished_at - self.stated_at).microseconds / 1000)

    # logging
    def log(self, level: int, message: str, exception: Exception = None):
        if self.emoji:
            prefix = f"{self.emoji} {self.name}"
        else:
            prefix = f"{self.name}"

        logger.log(level, f"%s > %s", prefix, message, exc_info=exception)

    def info(self, message: str):
        self.log(logging.INFO, message)

    def error(self, message: str):
        self.log(logging.ERROR, message)

    def exception(self, exception: Exception):
        self.log(logging.ERROR, str(exception), exception)
