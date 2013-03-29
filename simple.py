#!/usr/bin/env python
import wx
class MyFrame(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600,600))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.control.SetBackgroundColour('#121121')
        self.control.SetForegroundColour('WHITE')
        self.Show(True)

app = wx.App(False)
frame = MyFrame(None, 'Small editor')
app.MainLoop()