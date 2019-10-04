from controller.integer._intcontroller import IntController
from utils.inttype import TINYINT


def generate(how_many: int, args: list):
    return IntController(TINYINT, how_many, args)

