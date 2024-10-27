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
        logger.info("Scheduled tasks:")

        for task in self.tasks:
            logger.info(f" * {task.name}: {task.trigger.description}")

    def workwork(self):
        for task in self.tasks:
            thread = Thread(target=task.run)
            thread.start()

    def nap(self):
        seconds = 60 - time() % 60
        logger.debug("💤 sleeping")
        sleep(seconds)
