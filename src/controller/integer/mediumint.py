from controller.integer._intcontroller import IntController
from utils.inttype import MEDIUMINT


def generate(): # TODO: pass the arguments to controller
    controller = IntController(MEDIUMINT, False, 1)
    return controller.gen()
