# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TestPluginDialog
                                 A QGIS plugin
 my awesome plugin
                             -------------------
        begin                : 2016-06-27
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Marco Bernasocchi
        email                : marco@opengis.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'test_plugin_dialog_base.ui'))


class TestPluginDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, iface, parent=None):
        """Constructor."""
        super(TestPluginDialog, self).__init__(parent)
        self.iface = iface
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    def update_layer_name(self):
        active_layer = self.iface.activeLayer()
        active_layer_name = active_layer.name()
        self.active_layer_input.setText(active_layer_name)
