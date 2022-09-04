import pcbnew
from typing import List
from ..kicad.board import get_layer_names

class Model:
    def __init__(self, board, logger):
        self.logger = logger
        self.board:pcbnew.BOARD = board
        self.vias = []
        self.layers = []
        self.names:List[str] = []
        self.areas:List[pcbnew.ZONE] = []

        for i in range(0, self.board.GetAreaCount()):
            area:pcbnew.ZONE = self.board.GetArea(i)
            if area.IsOnCopperLayer() and not area.GetIsRuleArea():
                self.areas.append(area)
                name = str(area.GetZoneName())
                if name == '':
                    name = 'No Name ' + str(i)
                self.names.append(name)
                layer = area.GetLayer()
                self.logger.info(name)
                self.logger.info(layer)
        
        self.layers.append('All Layer')
        for name in get_layer_names(self.board):
            self.layers.append(name)
    