#-*- coding:utf-8 -*-
import os
import sys
import time

#import curl
#import psutil

from common import *
from _parseopts import *

options = init_opts()

if os.name is ('posix' or 'os2'):
    # Process priority, higher number = lower priority
    PROCESS_PRIORITY = 19
else:
    PROCESS_PRIORITY = psutil.IDLE_PRIORITY_CLASS
