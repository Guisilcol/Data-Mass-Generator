from controller.integer._intcontroller import IntController
from utils.inttype import TINYINT


def generate(): # TODO: pass the arguments to controller
    controller = IntController(TINYINT, False, 1)
    return controller.gen()

