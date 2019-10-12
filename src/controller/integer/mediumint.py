from controller.integer._intcontroller import IntController
from utils.inttype import MEDIUMINT


def generate(how_many: int, args: list):
    return IntController(MEDIUMINT.copy(), how_many, args)

