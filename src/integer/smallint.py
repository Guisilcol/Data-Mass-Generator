from controller.intcontroller import IntController
from integer.inttype import SMALLINT


def generate(): # TODO: pass the arguments to controller
    controller = IntController(SMALLINT, False, 1)
    return controller.gen()
