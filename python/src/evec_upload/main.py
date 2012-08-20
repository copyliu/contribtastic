# coding=utf-8
# python
#    EVE-Central.com Contribtastic
#    Copyright (C) 2005-2010 Yann Ramin
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License (in file COPYING) for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from evec_upload.version import *
from evec_upload.scanner import *
from evec_upload.uploader import get_uploader
from evec_upload.taskbar import *
import evec_upload.login
import evec_upload.options

from evec_upload.config import Config

import wx
import pickle
import os
import sys
import images
import urllib
import time

import wx.lib.newevent
(UpdateUploadEvent, EVT_UPDATE_UPLOAD) = wx.lib.newevent.NewEvent()
(DoneUploadEvent, EVT_DONE_UPLOAD) = wx.lib.newevent.NewEvent()


class MainFrame(wx.Frame):
    MENU_SETTINGS = wx.NewId()
    MENU_ABOUT = wx.NewId()
    MENU_SCANNOW = wx.NewId()
    MENU_LOCATE = wx.NewId()


    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title,
                          pos=(150, 150), style = wx.CAPTION | wx.MINIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CLOSE_BOX  )# size=(350, 150))

        try:
            check_protocol()
            r = check_client()
            if r is not True:
                dlg = wx.MessageDialog(self, u'發現新版本 ' + `r` + u' ! 請訪問 EVE 國服市場中心獲得新版本!', u'舊版本提醒',
                                       wx.OK | wx.ICON_ERROR
                                       )
                dlg.ShowModal()
                dlg.Destroy()
                os.system("explorer http://cem.copyliu.org")
                sys.exit(-1)

        except IOError:
            dlg = wx.MessageDialog(self, u'無法訪問網絡, 請確認網絡設置是否正確',
                                   u'無法訪問網絡',
                                   wx.OK | wx.ICON_ERROR
                                   )
            dlg.ShowModal()
            dlg.Destroy()
            sys.exit(-1)


        # Load config
        config = Config()
        r = config.reinit
        if r == -1:
            dlg = wx.MessageDialog(self, u"""已重置配置文件""", 'Client Upgrade', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()




        self.scanner_thread = ScannerThread()
        self.scanner_thread.start()

        def donecb(count, success, this=self):
            evt = DoneUploadEvent(count = count, success = success)
            wx.PostEvent(this, evt)
        self.donecb = donecb

        def updcb(typename, success, this=self):
            #print "UPD: %s, %s" % (typename, success,)
            evt = UpdateUploadEvent(typename = typename, success = success)
            wx.PostEvent(this, evt)
        self.updcb = updcb

        self.uploader = get_uploader(config, updcb)

        # Set icon
        self.SetIcon(images.getIconIcon())

        # Task Bar
        self.tbicon = TaskBarIcon(self)

        # Create the menubar
        menuBar = wx.MenuBar()

        # and a menu
        menu = wx.Menu()

        # option menu
        opmenu = wx.Menu()

        # help menu
        helpmenu = wx.Menu()


        # add an item to the menu, using \tKeyName automatically
        # creates an accelerator, the third param is some help text
        # that will show up in the statusbar
        menu.Append(self.MENU_SCANNOW, u"立即扫描...(&C)")
        menu.AppendSeparator()

        #menu.Append(self.MENU_SETTINGS, "&Settings...")
        #menu.Append(self.MENU_LOCATE, "&Locate cache folder...")

        menu.Append(wx.ID_EXIT, u"退出(&X)\tAlt-X", "Exit")

        helpmenu.Append(self.MENU_ABOUT, u"关于(&A)")

        # bind the menu event to an event handler
        self.Bind(wx.EVT_MENU, self.OnTimer, id=self.MENU_SCANNOW)
        self.Bind(wx.EVT_MENU, self.OnTimeToClose, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnAbout, id = self.MENU_ABOUT)
        self.Bind(wx.EVT_CLOSE, self.OnTimeToClose)

        # and put the menu on the menubar
        menuBar.Append(menu, u"文件(&F)")

        menuBar.Append(helpmenu, u"帮助(&H)")
        self.SetMenuBar(menuBar)

        self.CreateStatusBar()
        self.SetStatusText(u"空闲")

        # Now create the Panel to put the other controls on.
        panel = wx.Panel(self)

        self.pathtext = wx.StaticText(panel, -1, u"请稍候...")
        self.pathtext_l = wx.StaticText(panel, -1, u"EVE缓存文件夹: 自动识别")

        #self.usertext_l = wx.StaticText(panel, -1, "Character name:  ")
        #self.usertext = wx.StaticText(panel, -1, "...")

        self.uploadtext = wx.StaticText(panel, -1, "")

        if config['character_id'] == 0:
            self.uploads = long(0)
        else:
            self.uploads = long(0)
        self.scans = 0


        self.motd = wx.TextCtrl(panel, -1,
                                "",
                                size=(200, 100), style=wx.TE_MULTILINE|wx.TE_READONLY)

        self.update_motd()

        #text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))



        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer_path = wx.FlexGridSizer(2,2)
        #--
        sizer_path.Add(self.pathtext_l, 2, wx.EXPAND|wx.ALL, 1)
        sizer_path.Add(self.pathtext, 0, wx.ALL|wx.EXPAND, 1)

        #sizer_path.Add(self.usertext_l, 2, wx.EXPAND|wx.ALL, 1)
        #sizer_path.Add(self.usertext, 0, wx.ALL|wx.EXPAND, 1)

        #--
        sizer.Add(sizer_path, 0, wx.EXPAND | wx.ALL, 1)
        line = wx.StaticLine(panel, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        sizer.Add(self.uploadtext, 0, wx.ALL, 1)

        sizer.Add(self.motd, 4, wx.ALL|wx.EXPAND, 1)

        panel.SetSizer(sizer)
        panel.Layout()

        self.timer = wx.Timer(self)
        self.timer.Start(120000)

        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.Bind(EVT_UPDATE_UPLOAD, self.OnUploadUpdate)
        self.Bind(EVT_DONE_UPLOAD, self.OnUploadDone)

        self.load_infowidgets()

        self.paths = []
        self.paths_age = time.time()

    def load_infowidgets(self):
        config = Config()


        self.pathtext.SetLabel("")
        self.uploadtext.SetLabel(u"已上传: " + `self.uploads`[:-1] + u"  已扫描: " + `self.scans`)

    def OnTimeToClose(self, evt):
        """Event handler for the button click."""
        self.tbicon.OnTaskBarQuit(None)
        self.Close()
        sys.exit(0)

    def OnUploadUpdate(self, evt):

        self.uploads = self.uploads + 1
        self.SetStatusText(u"已上传 " + evt.typename)
        self.load_infowidgets()

    def OnUploadDone(self, evt):

        self.load_infowidgets()
        if evt.success == True:
            self.SetStatusText(u"空闲 - 上次上传了 " + `evt.count` + u" 份数据")
            self.scans += 1
            self.load_infowidgets()
        else:
            self.SetStatusText(u"无法找到EVE缓存文件.")

    def OnAbout(self, evt):
        global ProgramVersionNice
        dlg = wx.MessageDialog(self, 'Contribtastic! ' + ProgramVersionNice +"\n(c) 2006-2012 Yann Ramin. All Rights Reserved.\n\nSee EVE-Central.com for the latest updates and information.", 'About',
                               wx.OK
                               )
        dlg.ShowModal()
        dlg.Destroy()


    def OnTimer(self, evt):
        config = Config()
        self.SetStatusText(u"上传中...")

        if not self.paths or self.paths_age > (time.time() + (60*60*24)):
            self.paths = default_locations()
            self.paths_age = time.time()

        for path in self.paths:
            print "Scanning path ",path
            job = ScannerPayload(path, self.uploader, self.donecb)
            self.scanner_thread.trigger(job)

    def update_motd(self):
        motdf = urllib.urlopen("http://cem.copyliu.org/1.txt")
        motd = ""
        for line in motdf.readlines():
            motd += line
        motdf.close()

        self.motd.WriteText(motd.decode("utf8"))


class EVEc_Upload(wx.App):
    def OnInit(self):

        frame = MainFrame(None, u"国服市场数据采集!")
        self.SetTopWindow(frame)
        config = Config()
        show = True

        if len(sys.argv) > 1 and sys.argv[1] == "-hide":
            show = False

        print "Startup config: ",config.config_obj
        if 'hide' in config:
            show = not config['hide']

        frame.Show(show)

        return True

if __name__ == "__main__":
    app = EVEc_Upload(redirect=False)
    app.MainLoop()
