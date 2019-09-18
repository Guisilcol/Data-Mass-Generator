from controller.integer._intcontroller import IntController
from utils.inttype import INT


def generate(): # TODO: pass the arguments to controller
    controller = IntController(INT, False, 1)
    return controller.gen()

