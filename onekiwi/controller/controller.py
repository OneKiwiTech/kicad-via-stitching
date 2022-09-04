from ..model.model import Model
from ..view.view import ViaStitchingView
from .logtext import LogText
import pcbnew
import sys
import logging
import logging.config

class Controller:
    def __init__(self, board):
        self.view = ViaStitchingView()
        self.board = board
        self.logger = self.init_logger(self.view.textLog)
        self.model = Model(self.board, self.logger)
        self.get_vias()
        self.logger.info('init done')

    def Show(self):
        self.view.Show()
    
    def Close(self):
        self.view.Destroy()

    def get_vias(self):
        units = pcbnew.GetUserUnits()
        vias = self.board.GetDesignSettings().m_ViasDimensionsList
        unit = ''
        scale = 1
        # pcbnew.EDA_UNITS_INCHES = 0
        if units == pcbnew.EDA_UNITS_INCHES:
            unit = 'in'
            scale = 25400000
        # pcbnew.EDA_UNITS_MILLIMETRES = 1
        elif units == pcbnew.EDA_UNITS_MILLIMETRES:
            unit = 'mm'
            scale = 1000000
        # pcbnew.EDA_UNITS_MILS = 5
        elif units == pcbnew.EDA_UNITS_MILS:
            unit = 'mil'
            scale = 25400
        else:
            unit = 'mil'
            scale = 25400

        vialist = []
        for via in vias:
            if via.m_Diameter > 0:
                self.model.vias.append(via)
                diam = via.m_Diameter
                hole = via.m_Drill
                display = str(diam/scale) + ' / ' + str(hole/scale) + ' ' + unit
                vialist.append(display)
        self.view.SetUnitText(unit)
        self.view.AddViasSize(vialist)
        if len(vialist) < 1:
            self.logger.info('Please create Via')

    def init_logger(self, texlog):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        # Log to stderr
        handler1 = logging.StreamHandler(sys.stderr)
        handler1.setLevel(logging.DEBUG)
        # and to our GUI
        handler2 = LogText(texlog)
        handler2.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(funcName)s -  %(message)s",
            datefmt="%Y.%m.%d %H:%M:%S",
        )
        handler1.setFormatter(formatter)
        handler2.setFormatter(formatter)
        root.addHandler(handler1)
        root.addHandler(handler2)
        return logging.getLogger(__name__)
    