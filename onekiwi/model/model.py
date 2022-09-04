import pcbnew
from typing import List

class Model:
    def __init__(self, board, logger):
        self.logger = logger
        self.board:pcbnew.BOARD = board
        self.vias = []
        self.names:List[str] = []
        self.areas:List[pcbnew.ZONE] = []

        for i in range(0, self.board.GetAreaCount()):
            area:pcbnew.ZONE = self.board.GetArea(i)
            if area.IsOnCopperLayer():
                self.areas.append(area)
                name = str(area.GetZoneName())
                if name == '':
                    name = 'No Name ' + str(i)
                self.names.append(name)
    