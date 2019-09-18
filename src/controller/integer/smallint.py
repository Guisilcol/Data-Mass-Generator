from controller.integer._intcontroller import IntController
from utils.inttype import SMALLINT


def generate(): # TODO: pass the arguments to controller
    controller = IntController(SMALLINT, False, 1)
    return controller.gen()
