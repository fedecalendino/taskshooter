import logging
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict
from uuid import uuid4, UUID

from taskshooter.config import DEBUG
from .trigger import Trigger

logger = logging.getLogger(__name__)


class Task(ABC):
    def __init__(self, name: str, trigger: Trigger, emoji: str = None, metadata: Dict[str, object] = None):
        self.id: UUID = None
        self.name: str = name
        self.trigger: Trigger = trigger
        self.emoji: str = emoji
        self.metadata: Dict[str, object] = metadata or {}

        self.stated_at: datetime = None
        self.finished_at: datetime = None

    @abstractmethod
    def execute(self, force: bool = False):
        raise NotImplementedError()

    def run(self, force: bool = False, manual: bool = False):
        self.id = uuid4()

        self.info("running task...")

        self.stated_at = datetime.now()
        self.pre_run()

        try:
            self.execute(force)
            self.finished_at = datetime.now()
            self.info(f"completed successfully in {self.runtime}ms")

            self.post_run(manual=manual, exception=None)
        except Exception as exception:
            self.exception(exception)
            self.finished_at = datetime.now()

            self.post_run(manual=manual, exception=exception)

        self.id = None

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
        logger.log(level, f"[%s] %s > %s", str(self.id), str(self), message, exc_info=exception)

        if DEBUG:
            print(f"[{self.id}] {self} > {message}")

    def debug(self, message: str, exception: Exception = None):
        self.log(logging.DEBUG, message, exception)

    def info(self, message: str, exception: Exception = None):
        self.log(logging.INFO, message, exception)

    def warning(self, message: str, exception: Exception = None):
        self.log(logging.WARNING, message, exception)

    def error(self, message: str, exception: Exception = None):
        self.log(logging.ERROR, message, exception)

    def exception(self, exception: Exception):
        self.error(str(exception), exception)

    def __repr__(self):
        if self.emoji:
            return f"{self.emoji} {self.name}"
        else:
            return f"{self.name}"
