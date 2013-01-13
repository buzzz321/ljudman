# -*- coding: utf-8 *-*
import subprocess
import sys

def get_sinks():
    cmd = "pacmd"
    paramter = "list-sinks"

    try:
        result = subprocess.check_output([cmd, paramter]).splitlines()

    except OSError as e:
        print >>sys.stderr, "Execution failed:", e
