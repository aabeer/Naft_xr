# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk, WebKit # pylint: disable=E0611
import logging
logger = logging.getLogger('mybrowser')

from mybrowser_lib import Window
from mybrowser.AboutMybrowserDialog import AboutMybrowserDialog
from mybrowser.PreferencesMybrowserDialog import PreferencesMybrowserDialog

# See mybrowser_lib.Window.py for more details about how this class works
class MybrowserWindow(Window):
    __gtype_name__ = "MybrowserWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(MybrowserWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutMybrowserDialog
        self.PreferencesDialog = PreferencesMybrowserDialog

        # Code for other initialization actions should be added here.

        self.scrolledwindow = self.builder.get_object("scrolledwindow")
        self.webview = WebKit.WebView()
        self.scrolledwindow.add(self.webview)
        self.webview.show()
        self.webview.open("http://www.naftemporiki.gr/finance/athexRealTimeTickerPopup")
