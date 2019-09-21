from controller.integer._intcontroller import IntController
from utils.inttype import MEDIUMINT


def generate(how_many: int, args: list):
    controller = IntController(MEDIUMINT, how_many, args)
    return controller.gen()

