import wx
import Demo1

if __name__ == "__main__":
    app = wx.App()
    Demo1.MyFrame(None).Show()
    app.MainLoop()