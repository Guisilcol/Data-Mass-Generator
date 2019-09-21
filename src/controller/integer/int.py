from controller.integer._intcontroller import IntController
from utils.inttype import INT


def generate(how_many: int, args: list):
    controller = IntController(INT, how_many, args)
    return controller.gen()
