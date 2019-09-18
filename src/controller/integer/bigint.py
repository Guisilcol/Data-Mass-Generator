from controller.integer._intcontroller import IntController
from utils.inttype import BIGINT


def generate(): # TODO: pass the arguments to controller
    controller = IntController(BIGINT, False, 1)
    return controller.gen()

