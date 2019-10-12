from controller.integer._intcontroller import IntController
from utils.inttype import BIGINT


def generate(how_many: int, args: list):
    return IntController(BIGINT.copy(), how_many, args)

