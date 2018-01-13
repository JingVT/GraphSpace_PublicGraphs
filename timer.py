
#with this running, data is updated in every 200 second automatically

import sys  
import os  
import getopt  
import threading  
import time
import urllib2, base64
import json
import collections
import operator
import csv
import os.path
import dataFilter

def fun_timer():
    dataFilter
    global timer
    timer = threading.Timer(200, fun_timer)
    timer.start()

timer = threading.Timer(1, fun_timer)
timer.start()