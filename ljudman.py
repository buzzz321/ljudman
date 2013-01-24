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

    for match in indexfinder.finditer(sinks):
        appindex = match.group(2)
        start = match.span()[1]
        name = namefinder.search(sinks[start:])
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

        #print {'index': appindex, 'appname': appname, 'active_sink': active_sink}  # lint:ok
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

        QtCore.QObject.connect(self.ui.goto_channel_0,
            QtCore.SIGNAL("clicked()"), callbacker)  # lint:ok

        QtCore.QObject.connect(self.ui.create_null,
            QtCore.SIGNAL("clicked()"), self.create_null)  # lint:ok

        # Create a QTimer
        self.channel_timer = QtCore.QTimer()
        # Connect it to f
        self.channel_timer.timeout.connect(self.get_sink_inputs)
        # Call f() every 5 seconds
        self.channel_timer.start(1000)

    def update_sinks(self, sink_inputs):
        #old_items = self.ui.sinks.findItems('.*', QtCore.Qt.MatchRegExp)
        self.ui.sinks.clear()

        for sink in sink_inputs:
            item = QtGui.QListWidgetItem("%s" % sink['appname'])
            self.ui.sinks.addItem(item)

    def update_channels(self, channels):
        for channel in channels:
            item = QtGui.QListWidgetItem("%s" % channel['name'])
            self.ui.channel1.addItem(item)

            if channel['name'] == 'streamer':
                self.ui.create_null.setEnabled(False)

    def get_sink_inputs(self):
        self.update_sinks(get_sink_inputs())

    def create_null(self):
        cmd = "pactl"
        paramter = "load-module module-null-sink sink_name=streamer"

        try:
            subprocess.check_output([cmd, paramter])

        except OSError as e:
            print >>sys.stderr, "Execution failed:", e

if __name__ == "__main__":
    channels = get_sinks()
    sink_inputs = get_sink_inputs()
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()

    myapp.update_sinks(sink_inputs)
    myapp.update_channels(channels)

    myapp.show()
    sys.exit(app.exec_())

