# -*- coding: utf-8 *-*
import subprocess
import sys
import re
from gui import Ui_MainWindow
from PyQt4 import QtCore, QtGui


def parse_sink_inputs(sink_inputs):

    indexfinder = re.compile(r'(?P<index>\s*index\:\s*(\d*))', re.M)
    appnamefinder = re .compile(r'(?:\s*application\.name\s*=\s*\"(.*)")', re.M)
    sinks = []

    for match in indexfinder.finditer(sink_inputs):
        appindex = match.group(2)
        start = match.span()[1]
        appname = appnamefinder.search(sink_inputs[start:])
        appname = appname.group(1)
        sinks.append({'index': appindex, 'appname': appname})

        print {'index': appindex, 'appname': appname}
    return sinks


def get_sink_inputs():

    cmd = "pacmd"
    paramter = "list-sink-inputs"

    try:
        result = subprocess.check_output([cmd, paramter])
        parse_sink_inputs(result)

    except OSError as e:
        print >>sys.stderr, "Execution failed:", e


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    get_sink_inputs()
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

