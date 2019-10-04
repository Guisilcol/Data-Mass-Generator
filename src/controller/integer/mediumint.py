from controller.integer._intcontroller import IntController
from utils.inttype import MEDIUMINT


def generate(how_many: int, args: list):
    return IntController(MEDIUMINT, how_many, args)

