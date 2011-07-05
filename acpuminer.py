#-*- coding:utf-8 -*-
import os
import sys
import time

import argparse
#import curl
#import psutil
import json

PROGRAM_NAME = 'Asure CPUMiner'
PROGRAM_DESC = 'Bitcoin CPU Miner written in Python'
PROGRAM_VERSION = '0.1'

if os.name is ('posix' or 'os2'):
    # Process priority, higher number = lower priority
    PROCESS_PRIORITY = 19
else:
    PROCESS_PRIORITY = psutil.IDLE_PRIORITY_CLASS

DEFAULTS = {
    # host and port for RPC
    'RPC_HOST' : '127.0.0.1',
    'RPC_PORT' : 8332,

    # user name and password for RPC log-in
    'RPC_USER' : 'rpcuser',
    'RPC_PASS' : 'rpcpass'
}

# Argument parser, for parsing command line arguments
inparser = argparse.ArgumentParser(description=PROGRAM_DESC, add_help=False,)
inparser.add_argument('-V', '--version', action='version',
                       version=('%s v%s' % (PROGRAM_NAME, PROGRAM_VERSION)))
inparser.add_argument('-H', '--help', dest='HELP', action="store_true",
                       help='show this help message and exit')
maingroup = inparser.add_argument_group('configuration')
maingroup.add_argument('-c', '--config', type=str, dest='CONFFILE',
                       help='Location of config file')

authgroup = inparser.add_argument_group('authentication')
authgroup.add_argument('-h', '--host', type=str, dest='RPC_HOST',
                       default=DEFAULTS['RPC_HOST'],
                       help='Host for RPC')
authgroup.add_argument('-p', '--port', type=int, dest='RPC_PORT',
                       default=DEFAULTS['RPC_PORT'],
                       help='Port to use when connecting to host')
authgroup.add_argument('-U', '--user', type=str, dest='RPC_USER',
                       default=DEFAULTS['RPC_USER'],
                       help='User name used for RPC auth')
authgroup.add_argument('-P', '--pass', type=str, dest='RPC_PASS',
                       default=DEFAULTS['RPC_PASS'],
                       help='Password used for RPC auth')

args = vars(inparser.parse_args())

if args['HELP'] is True:
    inparser.print_help()
    sys.exit()

# Various options, read from a specified config file,
# config.json in the current directory (if present),
# or from the defaults specified above.
if args['CONFFILE'] is not None:
    with open(args['CONFFILE']) as cf:
        options = json.load(cf)
else:
    options = {}

for option in DEFAULTS.iterkeys():
    # Configuration from command line should override all others
    if option not in options:
        options[option] = args[option]
    # Configuration from file should override defaults
    elif args[option] != DEFAULTS[option]:
        options[option] = args[option]

print(json.dumps(options, indent=4))
