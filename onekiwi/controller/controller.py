from ..model.model import Model
from ..view.view import ViaStitchingView
from .logtext import LogText
from ..kicad.board import *
import pcbnew
import wx
import sys
import logging
import logging.config

# https://github.com/weirdgyn/viastitching/blob/master/viastitching_dialog.py
class Controller:
    def __init__(self, board):
        self.view = ViaStitchingView()
        self.board = board
        self.logger = self.init_logger(self.view.textLog)
        self.model = Model(self.board, self.logger)
        self.area = None
        self.get_vias()
        self.get_layers()
        self.get_areas()
        self.logger.info('init done')
        #self.logger.info(pcbnew.F_Cu)
        #self.logger.info(pcbnew.B_Cu)

        # Connect Events
        self.view.choiceArea.Bind(wx.EVT_CHOICE, self.OnChoiceArea)
        self.view.buttonApply.Bind(wx.EVT_BUTTON, self.OnButtonApply)
        self.view.buttonClear.Bind(wx.EVT_BUTTON, self.OnButtonClear)
        

    def Show(self):
        self.view.Show()
    
    def Close(self):
        self.view.Destroy()

    def OnChoiceArea(self, event):
        self.logger.info('OnChoiceArea')
        index = event.GetEventObject().GetSelection()
        area = self.model.areas[index]
        net = str(area.GetNetname())
        self.view.SetNetText(net)
        if self.area != None:
            self.area.ClearBrightened()
        area.SetBrightened()
        self.area = area
        pcbnew.Refresh()

    def OnButtonApply(self, event):
        self.FillupArea()
    
    def OnButtonClear(self, event):
        self.area.ClearBrightened()
        self.area = None
        pcbnew.Refresh()

    def get_layers(self):
        names = self.model.layers
        self.view.AddLayersName(names)

    def get_areas(self):
        self.view.AddAreasName(self.model.names)
        area = self.model.areas[0]
        net = str(area.GetNetname())
        self.view.SetNetText(net)
        if self.area != None:
            self.area.ClearBrightened()
        area.SetBrightened()
        self.area = area
        pcbnew.Refresh()
        
    
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
    
    def FillupArea(self):
        '''Fills selected area with vias.'''        

        drillsize = self.model.vias[0].m_Drill
        viasize = self.model.vias[0].m_Diameter
        step_x = 2000000
        step_y = 2000000
        #clearance = self.FromUserUnit(float(self.m_txtClearance.GetValue()))

        index = self.view.choiceArea.GetSelection()
        area = self.model.areas[index]

        bbox = area.GetBoundingBox()
        top = bbox.GetTop()
        bottom = bbox.GetBottom()
        right = bbox.GetRight()
        left = bbox.GetLeft()
        
        #index = self.view.choiceArea.GetSelection()
        #area = self.model.areas[index]
        netname = str(area.GetNetname())
        netcode = self.board.GetNetcodeFromNetname(netname)
        #commit = pcbnew.COMMIT()
        viacount = 0
        x = left

        #Cycle trough area bounding box checking and implanting vias
        layer = area.GetLayer()
        while x <= right:
            y = top
            while y <= bottom:
                p = pcbnew.wxPoint(x,y)
                #HitTestFilledArea(ZONE self, PCB_LAYER_ID aLayer, VECTOR2I aRefPos, int aAccuracy=0) -> bool
                #if area.HitTestFilledArea(layer, p, 0):
                if kicad.get_major_version >= 7:
                    filled_area = area.HitTestFilledArea(layer, pcbnew.VECTOR2I(p), 0)
                else:
                    filled_area = area.HitTestFilledArea(layer, p, 0)

                if filled_area:
                    via = pcbnew.PCB_VIA(self.board)
                    if kicad.get_major_version >= 7:
                        via.SetPosition(p)
                    else:
                        via.SetPosition(pcbnew.VECTOR2I(p))
                    via.SetLayer(layer)
                    via.SetNetCode(netcode)
                    via.SetDrill(drillsize)
                    via.SetWidth(viasize)
                    #via.SetTimeStamp(__timecode__)
                    self.board.Add(via)
                    viacount +=1
                    """
                    if not self.CheckOverlap(via):
                        #Check clearance only if clearance value differs from 0 (disabled)
                        if (clearance == 0) or self.CheckClearance(p, self.area, clearance):
                            self.board.Add(via)
                            #commit.Add(via)
                            viacount +=1
                            """
                y += step_y
            x += step_x

        self.area.ClearBrightened()
        pcbnew.Refresh()