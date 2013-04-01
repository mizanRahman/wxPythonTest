#!/usr/bin/env python
import wx
class MyFrame(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600,600))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.control.SetBackgroundColour('#121121')
        self.control.SetForegroundColour('WHITE')

        #ststus bar
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        #menubar
        filemenu= wx.Menu()
        aboutMenuItem = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        openMenuItem = filemenu.Append(1, "&Open","Opens a file in the editor")
        filemenu.AppendSeparator()
        exitMenuItem = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        self.Bind(wx.EVT_MENU, self.OnAbout, aboutMenuItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitMenuItem)
        self.Bind(wx.EVT_MENU, self.OnOpen, openMenuItem)

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
     
        self.Show(True)

    def OnOpen(self,event):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file")
        if dlg.ShowModal() == wx.ID_OK:
          path = dlg.GetPath()
          f = open(path,'r')
          self.control.SetValue(f.read())
          f.close()
          
        dlg.Destroy()

    def OnAbout(self,event):
        dlg = wx.MessageDialog( self, "A small text editor", "About Sample Editor", wx.OK)
        

        dlg.Destroy() # finally destroy it when finished.         
    
    def OnExit(self,event):
        self.close()


app = wx.App(False)
frame = MyFrame(None, 'Small editor')
app.MainLoop()