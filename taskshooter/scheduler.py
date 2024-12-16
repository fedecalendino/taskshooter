import logging
from threading import Thread
from time import time, sleep

from .task import Task

logger = logging.getLogger(__name__)


class Scheduler:
    def __init__(self, tasks: list[Task] = None):
        self.tasks = tasks or []

    def run(self):
        self.show()

        while True:
            self.nap()
            self.workwork()

    def add(self, task: Task):
        self.tasks.append(task)

    def show(self):
        self.info("Scheduled tasks:")

        for task in self.tasks:
            self.info(f" * {task}: {task.trigger.description}")

    def workwork(self):
        for task in self.tasks:
            self.info(f"running {task}...")

            thread = Thread(target=task.run)
            thread.start()

    def nap(self):
        seconds = 60 - time() % 60
        self.debug("💤 sleeping")
        sleep(seconds)

    # logging
    def log(self, level: int, message: str, exception: Exception = None):
        logger.log(level, message, exc_info=exception)

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
