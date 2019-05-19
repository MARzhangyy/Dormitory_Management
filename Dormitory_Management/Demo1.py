import wx
import Demo
class MyFrame(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,id=wx.ID_ANY, title=u"宿舍管理系统", pos=wx.DefaultPosition, size=wx.Size(300,250),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.Center()
        self.m_panel1 = wx.Panel(self)
        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"用户名：", (20, 70))
        self.m_staticText2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"密  码：", (20, 110))
        self.m_staticText3 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"欢迎来到宿舍管理系统",(20,20))
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.m_staticText3.SetFont(font)
        self.t1 = wx.TextCtrl(self.m_panel1, pos=(90, 70), size=(120, 25))
        self.t2 = wx.TextCtrl(self.m_panel1,-1,u'', pos=(90, 110), size=(120, 25), style=wx.TE_PASSWORD)

        self.m_button1 = wx.Button(self.m_panel1, wx.ID_ANY, u"登  录", (50, 160), size = (70,25))
        self.m_button2 = wx.Button(self.m_panel1, wx.ID_ANY, u"取  消", (160, 160), size = (70,25))
        self.m_button1.Bind(wx.EVT_BUTTON, self.judge)
        self.m_button2.Bind(wx.EVT_BUTTON, self.exit)
        #设置按钮颜色
        self.m_button1.SetBackgroundColour('#0a74f7')
        self.m_button1.SetForegroundColour('white')
        self.m_button2.SetBackgroundColour('#0a74f7')
        self.m_button2.SetForegroundColour('white')
        # 设置面板的背景颜色
        self.m_panel1.SetBackgroundColour('white')
    def judge(self,event):
        user = self.t1.GetValue()
        passwd = self.t2.GetValue()
        if user == 'host' and passwd == '1234':
            Demo.MyFrame1(None).Show()
        else:
            dial = wx.MessageDialog(None, '用户名或密码错误!', '结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
            dial.ShowModal()

    def exit(self,event):
        wx.Exit()
