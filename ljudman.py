# -*- coding: utf-8 *-*
import subprocess
import sys
import re
from gui import Ui_MainWindow
from PyQt4 import QtCore, QtGui


def parse_pulse_data(reg_exps, pulse_data):
    """ convert pulse audio text data to hash maps
    
    Keyword arguments:
    reg_exps    -- list of hash map containing tag to parse and its regexp.
                    The first item in the list will be the anchor item the rest
                    will be the sub items.
                    [{ tag : 'index', regexp: '.*' }]
    pulse_data  -- text data output from an pulse audio command
    
    """
    
    parsed_data = []    
    for match in reg_exps[0]['regexp'].finditer(pulse_data):
        appindex = match.group(2)
        start = match.span()[1]
        audio_items = {reg_exps[0]['tag']: appindex}
        for tag in reg_exps[1:]:            
            tag_value = tag['regexp'].search(pulse_data[start:])
            tag_value = tag_value.group(1)
            audio_items[tag['tag']] = tag_value
            
        parsed_data.append(audio_items)
    print parsed_data
    return parsed_data
    
#===============================================================================
# def parse_sound_channels(sinks):
#    indexfinder = re.compile(r'(?P<index>\s*index\:\s*(\d*))', re.M)
#    namefinder = re .compile(r'(?:name\:\s+\<(.*)>)', re.M)
#    sound_channels = []
# 
#    for match in indexfinder.finditer(sinks):
#        appindex = match.group(2)
#        start = match.span()[1]
#        name = namefinder.search(sinks[start:])
#        name = name.group(1)
#        sound_channels.append({'index': appindex, 'name': name})
# 
#        print {'index': appindex, 'name': name}
#    return sound_channels
#===============================================================================


def get_sound_channels():
    cmd = "pacmd"
    paramter = "list-sinks"

    try:
        result = subprocess.check_output([cmd, paramter])
        return parse_pulse_data([
                          {"tag": 'index',
                            "regexp": re.compile(r'(?P<index>\s*index\:\s*(\d*))', re.M)},
                          {"tag": 'name', 
                           "regexp": re.compile(r'(?:name\:\s+\<(.*)>)', re.M)} 
                          ], result)

    except OSError as e:
        print >>sys.stderr, "Execution failed:", e

    return []


def get_active_player_programs():

    cmd = "pacmd"
    paramter = "list-sink-inputs"

    try:
        result = subprocess.check_output([cmd, paramter])        
        return parse_pulse_data([
                             {"tag": 'index',
                              "regexp": re.compile(r'(?P<index>\s*index\:\s*(\d*))', re.M)},
                             {"tag": 'appname', 
                              "regexp": re.compile(r'(?:\s*application\.name\s*=\s*\"(.*)")', re.M)},
                             {"tag": 'active_sink', 
                              "regexp": re.compile(r'(?:sink\:\s+(\d+)\s+\<(.*)>)', re.M)} 
                             ], result)

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
        self.channel_timer.timeout.connect(self.get_active_player_programs)
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

    def get_active_player_programs(self):
        self.update_sinks(get_active_player_programs())

    def create_null(self):
        cmd = ["pactl"]
        paramter = ["load-module", "module-null-sink", "sink_name=streamer"]

        try:
            sink_number = subprocess.call(cmd + paramter)

        except OSError as e:
            print >>sys.stderr, "Execution failed:", e

if __name__ == "__main__":
    channels = get_sound_channels()
    sink_inputs = get_active_player_programs()
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()

    myapp.update_sinks(sink_inputs)
    myapp.update_channels(channels)

    myapp.show()
    sys.exit(app.exec_())

