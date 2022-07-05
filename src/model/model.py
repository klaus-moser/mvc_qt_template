import random


class Model:
    """
    Model Class of MVC.
    """
    def __init__(self, view: object) -> None:
        pass

    def return_random(self):
        return random.randint(0, 100)
