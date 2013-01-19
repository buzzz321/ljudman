# -*- coding: utf-8 *-*
import subprocess
import sys
import re
from gui import Ui_MainWindow
from PyQt4 import QtCore, QtGui


def parse_sinks(sinks):
    indexfinder = re.compile(r'(?P<index>\s*index\:\s*(\d*))', re.M)
    namefinder = re .compile(r'(?:name\:\s+\<(.*)>)', re.M)
    sound_channels = []

    for match in indexfinder.finditer(sink_inputs):
        appindex = match.group(2)
        start = match.span()[1]
        name = namefinder.search(sink_inputs[start:])
        name = name.group(1)
        sound_channels.append({'index': appindex, 'name': name})

        print {'index': appindex, 'name': name}
    return sound_channels


def get_sinks():
    cmd = "pacmd"
    paramter = "list-sinks"

    try:
        result = subprocess.check_output([cmd, paramter])
        return parse_sinks(result)

    except OSError as e:
        print >>sys.stderr, "Execution failed:", e

    return []


def parse_sink_inputs(sink_inputs):

    indexfinder = re.compile(r'(?P<index>\s*index\:\s*(\d*))', re.M)
    appnamefinder = re .compile(r'(?:\s*application\.name\s*=\s*\"(.*)")', re.M)  # lint:ok
    sinkfinder = re .compile(r'(?:sink\:\s+(\d+)\s+\<(.*)>)', re.M)
    inputs = []

    for match in indexfinder.finditer(sink_inputs):
        appindex = match.group(2)
        start = match.span()[1]
        appname = appnamefinder.search(sink_inputs[start:])
        appname = appname.group(1)
        active_sink = sinkfinder.search(sink_inputs[start:])
        active_sink = active_sink.group(1)
        inputs.append({'index': appindex, 'appname': appname, 'active_sink': active_sink})  # lint:ok

        print {'index': appindex, 'appname': appname, 'active_sink': active_sink}  # lint:ok
    return inputs


def get_sink_inputs():

    cmd = "pacmd"
    paramter = "list-sink-inputs"

    try:
        result = subprocess.check_output([cmd, paramter])
        return parse_sink_inputs(result)

    except OSError as e:
        print >>sys.stderr, "Execution failed:", e

    return []

def callbacker():
    print "hejsan"


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.goto_channel1,QtCore.SIGNAL("clicked()"), callbacker)  # lint:ok

    def update_sinks(self, sink_inputs):
        for sink in sink_inputs:
            item = QtGui.QListWidgetItem("%s" % sink['appname'])
            self.ui.sinks.addItem(item)


if __name__ == "__main__":
    sink_inputs = get_sink_inputs()
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()

    myapp.update_sinks(sink_inputs)
    myapp.show()
    sys.exit(app.exec_())

