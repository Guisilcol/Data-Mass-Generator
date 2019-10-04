from controller.integer._intcontroller import IntController
from utils.inttype import SMALLINT


def generate(how_many: int, args: list):
    return IntController(SMALLINT, how_many, args)
