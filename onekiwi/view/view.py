import wx
from .dialog import *
from ..kicad.board import get_current_unit
from ..version import version

class ViaStitchingView(ViaStitchingDialog):
    def __init__(self):
        ViaStitchingDialog.__init__(self, None)
        self.window = wx.GetTopLevelParent(self)

    def HighResWxSize(self, window, size):
        """Workaround if wxWidgets Version does not support FromDIP"""
        if hasattr(window, "FromDIP"):
            return window.FromDIP(size)
        else:
            return size