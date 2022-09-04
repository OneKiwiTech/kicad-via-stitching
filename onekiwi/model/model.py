import pcbnew

class Model:
    def __init__(self, board, logger):
        self.logger = logger
        self.footprints = board.GetFootprints()
