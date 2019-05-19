import wx
import pymysql

#建一个窗口类MyFrame1继承wx.Frame
class MyFrame1(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,id=wx.ID_ANY, title=u"宿舍管理系统", pos=wx.DefaultPosition, size=wx.Size(600,300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.Center() #居中显示

        # 小构件，如按钮，文本框等被放置在面板窗口。 wx.Panel类通常是被放在一个wxFrame对象中。这个类也继承自wxWindow类。
        self.m_panel1 = wx.Panel(self)
        # 标签，一行或多行的只读文本，Wx.StaticText(parent, id, label, position, size, style)
        #设置静态文本字体
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)

        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"宿  舍：", (20, 20))
        self.m_staticText1.SetFont(font)
        self.m_button1 = wx.Button(self.m_panel1, wx.ID_ANY, u"宿舍基本信息", (130, 20), wx.DefaultSize,
                                   style=wx.BORDER_MASK)

        self.m_staticText2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"管理员：", (20, 90))
        self.m_staticText2.SetFont(font)
        self.m_button2 = wx.Button(self.m_panel1, wx.ID_ANY, u"管理员基本信息", (130, 90), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        self.m_button3 = wx.Button(self.m_panel1, wx.ID_ANY, u"聘请管理员", (250, 90), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        self.m_button4 = wx.Button(self.m_panel1, wx.ID_ANY, u"解雇管理员", (370, 90), wx.DefaultSize,
                                   style=wx.BORDER_MASK)

        self.m_staticText3 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"学  生：", (20, 160))
        self.m_staticText3.SetFont(font)
        self.m_button5 = wx.Button(self.m_panel1, wx.ID_ANY, u"学生基本信息", (130, 160), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        self.m_button6 = wx.Button(self.m_panel1, wx.ID_ANY, u"入  住", (250, 160), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        self.m_button7 = wx.Button(self.m_panel1, wx.ID_ANY, u"迁  出", (370, 160), wx.DefaultSize,
                                   style=wx.BORDER_MASK)

        # 按钮绑定对话框的弹出
        # 在创建应用程序时，Bind函数可以将按钮的动作与特定的函数绑定，当按钮上有动作时，这个函数就会启动，从而处理响应的事件。
        # 个Button被单击发生了EVT_BUTTON事件
        self.m_button1.Bind(wx.EVT_BUTTON, MyDialog1(None).OnClick)
        self.m_button2.Bind(wx.EVT_BUTTON, MyDialog21(None).OnClick)
        self.m_button3.Bind(wx.EVT_BUTTON, MyDialog22(None).OnClick)
        self.m_button4.Bind(wx.EVT_BUTTON, MyDialog23(None).OnClick)
        self.m_button5.Bind(wx.EVT_BUTTON, MyDialog31(None).OnClick)
        self.m_button6.Bind(wx.EVT_BUTTON, MyDialog32(None).OnClick)
        self.m_button7.Bind(wx.EVT_BUTTON, MyDialog33(None).OnClick)

        self.m_button1.SetBackgroundColour('#0a74f7')
        self.m_button1.SetForegroundColour('white')

        self.m_button2.SetBackgroundColour('#238E23')
        self.m_button2.SetForegroundColour('white')
        self.m_button3.SetBackgroundColour('#238E23')
        self.m_button3.SetForegroundColour('white')
        self.m_button4.SetBackgroundColour('#238E23')
        self.m_button4.SetForegroundColour('white')
        self.m_button5.SetBackgroundColour('#6F4242')
        self.m_button5.SetForegroundColour('white')
        self.m_button6.SetBackgroundColour('#6F4242')
        self.m_button6.SetForegroundColour('white')
        self.m_button7.SetBackgroundColour('#6F4242')
        self.m_button7.SetForegroundColour('white')

        self.m_panel1.SetBackgroundColour('white')  # 设置面板的背景颜色

#宿舍基本信息
class MyDialog1(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"宿舍基本信息", pos=wx.DefaultPosition, size=wx.Size(500, 200),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "宿舍号：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(90, 20), size=(120, 25))

        wx.StaticText(self.panel, wx.ID_ANY, "宿舍号", (20, 60))
        wx.StaticText(self.panel, wx.ID_ANY, "宿舍长", (140, 60))
        wx.StaticText(self.panel, wx.ID_ANY, "电  话", (260, 60))

    def OnClick(self, event):
        dialog = MyDialog1(None)
        btn = wx.Button(parent=dialog.panel, label="查询", pos=(240, 20), size=(70, 25))
        btn.Bind(wx.EVT_BUTTON, dialog.find)
        dialog.ShowModal()

    def find(self, event):
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='zyy960316', db='Dorm', charset='utf8')
        cursor = conn.cursor()
        num = self.t1.GetValue().encode('utf8')
        try:
            sql = "select Dormitory,DorSnum,phonenum from dormitory where Dormitory = %s"
            cursor.execute(sql,num)
            rs = cursor.fetchall()
            h = 80
            for row in rs:
                h = h + 20
                dor_Dormitory = row[0]
                dor_DorSnum = row[1]    #注意数据库中的数据为数字 int 类型时的读取方式 id = '%d' % i[0]
                dor_phonenum = row[2]
                wx.StaticText(self.panel, wx.ID_ANY, dor_Dormitory, (20, h))
                wx.StaticText(self.panel, wx.ID_ANY, str(dor_DorSnum), (140, h))
                wx.StaticText(self.panel, wx.ID_ANY, str(dor_phonenum), (260, h))
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

#关于管理员
class MyDialog21(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"管理员信息", pos=wx.DefaultPosition, size=wx.Size(400, 200),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "工号：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(90, 20), size=(120, 25))
        wx.StaticText(self.panel, wx.ID_ANY, "工号", (20, 60))
        wx.StaticText(self.panel, wx.ID_ANY, "姓名", (80, 60))
        wx.StaticText(self.panel, wx.ID_ANY, "年龄", (140, 60))
        wx.StaticText(self.panel, wx.ID_ANY, "工龄", (200, 60))
        wx.StaticText(self.panel, wx.ID_ANY, "电话", (260, 60))

    def OnClick(self, event):
        dialog2 = MyDialog21(None)
        btn = wx.Button(parent=dialog2.panel, label="查询", pos=(240, 20), size=(70, 25))
        btn.Bind(wx.EVT_BUTTON, dialog2.find)
        dialog2.ShowModal()

    def find(self, event):
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='zyy960316', db='Dorm', charset='utf8')
        cursor = conn.cursor()
        num = self.t1.GetValue().encode('utf8')
        try:
            sql = "select id,aname,age,wage,phone from Administrator where id = %s"
            cursor.execute(sql,num)
            rs = cursor.fetchall()
            h = 80
            for row in rs:
                h = h + 20
                ad_id = row[0]
                ad_aname = row[1]
                ad_age = row[2]
                ad_wage = row[3]
                ad_phone = row[4]
                wx.StaticText(self.panel, wx.ID_ANY, str(ad_id), (20, h))
                wx.StaticText(self.panel, wx.ID_ANY, str(ad_aname), (80, h))
                wx.StaticText(self.panel, wx.ID_ANY, str(ad_age), (140, h))
                wx.StaticText(self.panel, wx.ID_ANY, str(ad_wage), (200, h))
                wx.StaticText(self.panel, wx.ID_ANY, str(ad_phone), (260, h))
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
#聘请管理员
class MyDialog22(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"聘请管理员", pos=wx.DefaultPosition, size=wx.Size(400, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "请输入工号：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(140, 20), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入姓名：", (20, 70))
        self.t2 = wx.TextCtrl(self.panel, pos=(140,70), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入年龄：", (20, 120))
        self.t3 = wx.TextCtrl(self.panel, pos=(140, 120), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入工龄：", (20, 170))
        self.t4 = wx.TextCtrl(self.panel, pos=(140, 170), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入电话：", (20, 220))
        self.t5 = wx.TextCtrl(self.panel, pos=(140, 220), size=(120, 25))

    def OnClick(self, e):
        dialog22 = MyDialog22(None)
        btn = wx.Button(parent=dialog22.panel, label="聘请", pos=(20, 280), size=(70, 25))
        btn.Bind(wx.EVT_BUTTON, dialog22.insert)
        dialog22.ShowModal()

    def insert(self, e):
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='zyy960316', db='Dorm', charset='utf8')
        cursor = conn.cursor()

        id = self.t1.GetValue().encode('utf8')  # 注意GetValue()获取的是unicode编码，
        aname = self.t2.GetValue().encode('utf8')  # 你使用的#coding=utf8，那就对获取的数据.encode('utf8')
        age = self.t3.GetValue().encode('utf8')
        wage = self.t4.GetValue().encode('utf8')
        phone = self.t5.GetValue().encode('utf8')

        data = (id,aname,age,wage,phone)
        try:
            sql = "insert into Administrator values (%s,%s,%s,%s,%s)"
            cursor.execute(sql, data)
            conn.commit()
            dial = wx.MessageDialog(None, '成功聘请管理员!', '结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
            dial.ShowModal()  # 显示对话框
        except:
            dial = wx.MessageDialog(None, '聘请管理员失败!', '结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
            dial.ShowModal()  # 显示对话框
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
#解雇管理员
class MyDialog23(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"解雇管理员", pos=wx.DefaultPosition, size=wx.Size(200, 200),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "管理员工号：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(20, 50), size=(120, 25))

    def OnClick(self, e):
        dialog23 = MyDialog23(None)
        btn = wx.Button(parent=dialog23.panel, label="解雇", pos=(20, 90), size=(70, 25))
        btn.Bind(wx.EVT_BUTTON, dialog23.delete)
        dialog23.ShowModal()

    def delete(self, e):
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='zyy960316', db='Dorm', charset='utf8')
        cursor = conn.cursor()

        id = self.t1.GetValue().encode('utf8')  # 注意GetValue()获取的是unicode编码
        try:
            sql = "delete from Administrator where id=%s"
            cursor.execute(sql,id)
            conn.commit()
            dial = wx.MessageDialog(None, '成功解雇管理员!', '结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
            dial.ShowModal()  # 显示对话框
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
#关于学生
class MyDialog31(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"学生基本信息", pos=wx.DefaultPosition, size=wx.Size(420, 200),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "学号：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(90, 20), size=(120, 25))
        # btn = wx.Button(parent=self.panel, label="查询", pos=(240, 20), size=(70, 25))
        # btn.Bind(wx.EVT_BUTTON, self.find)
        wx.StaticText(self.panel, wx.ID_ANY, "学号", (20, 60))
        wx.StaticText(self.panel, wx.ID_ANY, "姓名", (80, 60))
        wx.StaticText(self.panel, wx.ID_ANY, "学院", (140, 60))
        wx.StaticText(self.panel, wx.ID_ANY, "籍贯", (200, 60))
        wx.StaticText(self.panel, wx.ID_ANY, "宿舍", (260, 60))
        wx.StaticText(self.panel, wx.ID_ANY, "入住时间", (320, 60))

    def OnClick(self, e):
        dialog31 = MyDialog31(None)
        btn = wx.Button(parent=dialog31.panel, label="查询", pos=(240, 20), size=(70, 25))
        btn.Bind(wx.EVT_BUTTON, dialog31.find)
        dialog31.ShowModal()

    def find(self, event):
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='zyy960316', db='Dorm', charset='utf8')
        cursor = conn.cursor()
        num = self.t1.GetValue().encode('utf8')
        try:
            sql = "select Snum,Sname,Sdept,place,dormitory,time from students where Snum = %s"
            cursor.execute(sql,num)
            rs = cursor.fetchall()
            h = 80
            for row in rs:
                h = h + 20
                s_snum = row[0]
                s_sname = row[1]
                s_sdept = row[2]
                s_place = row[3]
                s_dormitory = row[4]
                s_time = row[5]
                wx.StaticText(self.panel, wx.ID_ANY, str(s_snum), (20, h))
                wx.StaticText(self.panel, wx.ID_ANY, str(s_sname), (80, h))
                wx.StaticText(self.panel, wx.ID_ANY, str(s_sdept), (140, h))
                wx.StaticText(self.panel, wx.ID_ANY, str(s_place), (200, h))
                wx.StaticText(self.panel, wx.ID_ANY, str(s_dormitory), (260, h))
                wx.StaticText(self.panel, wx.ID_ANY, str(s_time), (320, h))
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
#入住
class MyDialog32(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"入住", pos=wx.DefaultPosition, size=wx.Size(350, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "请输入学号：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(140, 20), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入姓名：", (20, 70))
        self.t2 = wx.TextCtrl(self.panel, pos=(140, 70), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入学院：", (20, 120))
        self.t3 = wx.TextCtrl(self.panel, pos=(140, 120), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入籍贯：", (20, 170))
        self.t4 = wx.TextCtrl(self.panel, pos=(140, 170), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入宿舍：", (20, 220))
        self.t5 = wx.TextCtrl(self.panel, pos=(140, 220), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入入住时间：", (20, 270))
        self.t6 = wx.TextCtrl(self.panel, pos=(140, 270), size=(120, 25))

    def OnClick(self, e):
        dialog32 = MyDialog32(None)
        btn = wx.Button(parent=dialog32.panel, label="入   住", pos=(20, 310), size=(70, 25))
        btn.Bind(wx.EVT_BUTTON, dialog32.insert)
        dialog32.ShowModal()

    def insert(self, e):
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='zyy960316', db='Dorm', charset='utf8')
        cursor = conn.cursor()

        snum = self.t1.GetValue().encode('utf8')  # 注意GetValue()获取的是unicode编码，
        sname = self.t2.GetValue().encode('utf8')  # 你使用的#coding=utf8，那就对获取的数据.encode('utf8')
        sdept = self.t3.GetValue().encode('utf8')
        place = self.t4.GetValue().encode('utf8')
        dormitory = self.t5.GetValue().encode('utf8')
        time = self.t6.GetValue().encode('utf8')
        data = (snum,sname,sdept,place,dormitory,time)

        try:
            sql = "insert into students values(%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, data)
            conn.commit()
            dial = wx.MessageDialog(None, '成功入住!', '入住结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
            dial.ShowModal()  # 显示对话框
        except:
            dial = wx.MessageDialog(None, '入住失败!', '入住结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
            dial.ShowModal()
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
#迁出
class MyDialog33(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"迁出学生", pos=wx.DefaultPosition, size=wx.Size(200, 200),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "学号：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(20, 50), size=(120, 25))

    def OnClick(self, e):
        dialog33 = MyDialog33(None)
        btn = wx.Button(parent=dialog33.panel, label="迁   出", pos=(20, 90), size=(70, 25))
        btn.Bind(wx.EVT_BUTTON, dialog33.delete)
        dialog33.ShowModal()

    def delete(self, e):
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='zyy960316', db='Dorm', charset='utf8')
        cursor = conn.cursor()

        snum = self.t1.GetValue().encode('utf8')  # 注意GetValue()获取的是unicode编码
        try:
            sql = "delete from students where snum=%s"
            cursor.execute(sql, snum)
            conn.commit()
            dial = wx.MessageDialog(None, '成功迁出!', '迁出结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
            dial.ShowModal()  # 显示对话框
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
