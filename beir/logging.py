import logging
import tqdm

class LoggingHandler(logging.Handler):
    def __init__(self, level=logging.INFO):
        super().__init__(level)

