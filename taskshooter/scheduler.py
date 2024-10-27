import logging
from logging import Logger
from threading import Thread
from time import time, sleep

from .task import Task

default_logger = logging.getLogger(__name__)


class Scheduler:
    def __init__(self, tasks: list[Task] = None, logger: Logger = None):
        self.tasks: list[Task] = tasks or []
        self.logger: Logger = logger

    def update_loggers(self):
        for task in self.tasks:
            if not task.logger:
                task.logger = self.logger

    def run(self):
        self.update_loggers()

        self.show()

        while True:
            self.nap()
            self.workwork()

    def add(self, task: Task):
        self.tasks.append(task)

    def show(self):
        self.logger.info("Scheduled tasks:")

        for task in self.tasks:
            self.logger.info(f" * {task.name}: {task.trigger.description}")

    def workwork(self):
        for task in self.tasks:
            thread = Thread(target=task.run)
            thread.start()

    def nap(self):
        self.debug("💤 sleeping")
        sleep(60 - time() % 60)

    # logging
    def log(self, level: int, message: str, exception: Exception = None):
        logger = self.logger or default_logger
        logger.log(level, message, exc_info=exception)

    def debug(self, message: str):
        self.log(logging.DEBUG, message)
