from controller.integer._intcontroller import IntController
from utils.inttype import INT


def generate(how_many: int, args: list):
    return IntController(INT, how_many, args)
