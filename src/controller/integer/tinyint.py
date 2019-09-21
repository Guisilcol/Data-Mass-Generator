from controller.integer._intcontroller import IntController
from utils.inttype import TINYINT


def generate(how_many: int, args: list):
    controller = IntController(TINYINT, how_many, args)
    return controller.gen()

