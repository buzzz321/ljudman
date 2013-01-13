# -*- coding: utf-8 *-*
import subprocess
import sys
import re


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

get_sink_inputs()
