from app.commands import Command
import random

class RandomCommand(Command):
    def execute(self):
        print(random.randint(0,100))