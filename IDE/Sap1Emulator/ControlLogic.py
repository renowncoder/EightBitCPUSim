import wx
from pubsub import pub

class ControlLogic(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, size=(200, 75))
        self.parent = parent
        self.box = wx.StaticBox(self, wx.ID_ANY, "Control Logic", wx.DefaultPosition, (200, 75))
        nmSizer = wx.StaticBoxSizer(self.box, wx.VERTICAL)

        self.SetSizer(nmSizer)

