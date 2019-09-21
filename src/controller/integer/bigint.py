from controller.integer._intcontroller import IntController
from utils.inttype import BIGINT


def generate(how_many: int, args: list):
    controller = IntController(BIGINT, how_many, args)
    return controller.gen()

