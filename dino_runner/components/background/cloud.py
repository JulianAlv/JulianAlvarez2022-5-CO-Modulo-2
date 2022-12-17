from dino_runner.components.background.background import Background
from dino_runner.utils.constants import CLOUD


class Cloud(Background):
    def __init__(self):
        super().__init__(CLOUD)
