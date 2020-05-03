import os
import argparse
import sys
import psutil
import fileinput
import glob
# for proc in psutil.process_iter():
#     print(proc.name())
import time
import re

# parser = argparse.ArgumentParser()
# args=parser.parse_args()
# print("there are 2 types of arguments")
print(sys.platform)
parser = argparse.ArgumentParser()
parser.add_argument("-bsd", "--board_file", help=".bsd file to load")
parser.add_argument("-hdd", "--hard_disk", help="Hard drive image to load")
parser.add_argument("-bios", "--bios_image", help="BIOS image to load")
parser.add_argument("-l", "--log", help="Log location of parsed log file")
parser.add_argument("-c", "--config", help="configuration file containing simnow commands")

ARGS = parser.parse_args()
BOARD = ARGS.board_file
SATA_IMAGE = ARGS.hard_disk
BIOS_IMAGE = ARGS.bios_image
CONFIG_FILE = ARGS.config
LOG = ARGS.log
LOG_CONTENT = ''
print(BOARD)
print(CONFIG_FILE)
TIMEOUT = 1200
TIMESTAMP_START = time.time()
#PATH = os.path.abspath(__file__).replace('port80h_snoop.py', '')
#print(PATH)
def set_bios(new_bios, config_file):
    """this function takes BIOS path & prints in simnow .script"""
    print("newBios")
    print(new_bios,config_file)
    with open(config_file) as cfg_file:
        for line in cfg_file:
            if 'memdevice:0.InitFile' in line:
                old_bios = line.split(' ')[1]
                print("oldBois",old_bios)
    for line in fileinput.input(config_file, inplace=True):
        print(line.replace(old_bios, str(new_bios)).strip('\n'))
if BOARD == '':
    print("board_file (-bsd) option needed")
    print("UNSTABLE")
if SATA_IMAGE == '':
    print("board_file (-bsd) option needed")
    print("UNSTABLE")
if CONFIG_FILE == '':
    print("config file (-c) option needed")
    print("UNSTABLE")
if BIOS_IMAGE is None:
    if glob.glob('*.FD') != [] and len(glob.glob('*.FD')) == 1:
        print("The unstashed BIOS file is present")
        BIOS_IMAGE = os.path.abspath(''.join(glob.glob('*.FD')))
        print(BIOS_IMAGE)
    else:
        print("No or Multiple unstashed BIOSs are available, hence Exiting")
        print("UNSTABLE")
#parser.add_argument("-bsd","--board_file", help=".bsd file to load")
set_bios(BIOS_IMAGE, CONFIG_FILE)

# #PATH=os.path.abspath(__file__)
# PATH=os.getcwd()+"\port80h_snoop1.log"
PATH=os.path.join(os.getcwd(),"port80h_snoop1.log")
print("Path is ",PATH)

with open("abc" , 'r') as log:
    try:
            print(log.readline())

    except Exception:
        print("Exception occured")
