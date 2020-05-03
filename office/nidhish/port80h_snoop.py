"""This script accepts BSD file and OS image path to launch simnow
   and the path to bios is hardcoded.
   The OS used with the script should've HDTOUT driver
   So, that it writes console messages to the simnow log.
"""
import os
import sys
import subprocess
from subprocess import CREATE_NEW_CONSOLE
import time
import fileinput
import glob
import re
import argparse
import psutil

lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, lib_path)
from Libraries import exit_codes


def set_bsd(new_bsd, config_file):
    """this function takes BSD path passed as ARG prints in simnow .script"""
    with open(config_file) as cfg_file:
        for line in cfg_file:
            if 'shell.open' in line:
                old_bsd = line.split(' ')[1]
    for line in fileinput.input(config_file, inplace=True):
        print(line.replace(old_bsd, new_bsd).strip('\n'))


def set_bios(new_bios, config_file):
    """this function takes BIOS path & prints in simnow .script"""
    with open(config_file) as cfg_file:
        for line in cfg_file:
            if 'memdevice:0.InitFile' in line:
                old_bios = line.split(' ')[1]
    for line in fileinput.input(config_file, inplace=True):
        print(line.replace(old_bios, str(new_bios)).strip('\n'))


def set_hdd(new_hdd, config_file):
    """this function takes HDD path & prints in simnow .script"""
    with open(config_file) as cfg_file:
        for line in cfg_file:
            if '.image' in line:
                old_hdd = line.split(' ')[1]
    for line in fileinput.input(config_file, inplace=True):
        print(line.replace(old_hdd, new_hdd).strip('\n'))


def set_port80_log(port80_log, config_file):
    """this function takes log path & prints in simnow .script"""
    with open(config_file) as cfg_file:
        for line in cfg_file:
            if 'shell.SetLogFile ' in line:
                old_port80_log = line.split(' ')[1]
    for line in fileinput.input(config_file, inplace=True):
        print(line.replace(old_port80_log, port80_log).strip('\n'))


def set_port80_error_log(port80_error_log, config_file):
    """this function takes error log path & prints in Zeppelin.script"""
    with open(config_file) as cfg_file:
        for line in cfg_file:
            if 'shell.SetErrorLogFile ' in line:
                old_port80_error_log = line.split(' ')[1]
    for line in fileinput.input(config_file, inplace=True):
        print(line.replace(old_port80_error_log, port80_error_log).strip('\n'))


################################################################################################

print("Killing Simnow instance before starting Test , if there are any")
# for proc in psutil.process_iter():
#     if proc.name() == "simnow.exe":
#         proc.kill()

TIMEOUT = 1200
TIMESTAMP_START = time.time()
PATH = os.path.abspath(__file__).replace('port80h_snoop.py', '')
print(PATH)

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

if BOARD == '':
    print("board_file (-bsd) option needed")
    exit_codes.exit("UNSTABLE")
if SATA_IMAGE == '':
    print("board_file (-bsd) option needed")
    exit_codes.exit("UNSTABLE")
if CONFIG_FILE == '':
    print("config file (-c) option needed")
    exit_codes.exit("UNSTABLE")
if BIOS_IMAGE is None:
    if glob.glob('*.FD') != [] and len(glob.glob('*.FD')) == 1:
        print("The unstashed BIOS file is present")
        BIOS_IMAGE = os.path.abspath(''.join(glob.glob('*.FD')))
        print(BIOS_IMAGE)
    else:
        print("No or Multiple unstashed BIOSs are available, hence Exiting")
        exit_codes.exit("UNSTABLE")

if LOG is None:
    LOG = ''

os.chdir(PATH)
#set_bsd(BOARD, CONFIG_FILE)
set_bios(BIOS_IMAGE, CONFIG_FILE)
#set_hdd(SATA_IMAGE, CONFIG_FILE)
#set_port80_log(PATH + 'port80h_snoop.log', CONFIG_FILE)
#set_port80_error_log(PATH + 'port80h_snoop.log', CONFIG_FILE)
# Print the content of Zeppelin.script
print(CONFIG_FILE + " :")
with open(CONFIG_FILE, 'r') as fin:
    print(fin.read())

# subprocess.Popen(['C:/SimNow/simnow.exe', '-v'])
# time.sleep(5)

# Disabling Windows Error Reporting , if simnow crashes
if sys.platform.startswith("win"):
    import ctypes

    SEM_NOGPFAULTERRORBOX = 0x0002
    ctypes.windll.kernel32.SetErrorMode(SEM_NOGPFAULTERRORBOX);
    subprocess_flags = CREATE_NEW_CONSOLE
else:
    subprocess_flags = 0

time.sleep(5)
subprocess.Popen(['C:/SimNow/simnow.exe', '-e', PATH + CONFIG_FILE] \
                 , creationflags=subprocess_flags)

log_creation_countdown = 0
while True:
    log_creation_countdown += 1
    if os.path.isfile(PATH + 'port80h_snoop.log'):
        print("port80h_snoop.log is created")
        break
    else:
        time.sleep(5)
    if log_creation_countdown == 120:
        print("Exiting as NO simnow log was created after 10mins of simnow launch")
        exit_codes.exit("UNSTABLE")

with open(PATH + 'port80h_snoop.log', 'r') as log:
    try:
        while True:
            TIMESTAMP_NOW = time.time()
            TIME_DIFF = int(TIMESTAMP_NOW - TIMESTAMP_START)
            line = log.readline()
            cleanLine = re.sub(r"Yuba:.+", "", line).rstrip()
            if cleanLine != "":
                LOG_CONTENT += cleanLine + "\n"
            if TIME_DIFF >= TIMEOUT:
                print("Exiting due to the timeout of 1200 secs")
                print("Killing Simnow instance ")
                for proc in psutil.process_iter():
                    if proc.name() == "simnow.exe":
                        proc.kill()
                print("copying the log to simnow_os_boot folder")
                outputLog = open("outputLog.log", "w")
                outputLog.write(LOG_CONTENT)
                outputLog.close()
                os.rename("outputLog.log", "..\\..\\port80h_snoop.log")
                log.close()
                time.sleep(5)
                print("Deleting the tested BIOS")
                # os.remove(BIOS_IMAGE)
                exit_codes.exit("FAILED")
            if "/ #" in cleanLine:
                print("OS booted")
                time.sleep(5)
                for proc in psutil.process_iter():
                    if proc.name() == "simnow.exe":
                        proc.kill()
                time.sleep(5)
                log.close()
                print("copying the log to simnow_os_boot folder")
                outputLog = open("outputLog.log", "w")
                outputLog.write(LOG_CONTENT)
                outputLog.close()
                os.rename("outputLog.log", "..\\..\\port80h_snoop.log")
                # os.remove(BIOS_IMAGE)
                exit_codes.exit("PASSED")
    except Exception as error:
        print("There was an except caught.\nException msg :" + str(error))
        print("Killing the simnow instance and exiting with the code 1 i.e., Unstable")
        time.sleep(5)
        for proc in psutil.process_iter():
            if proc.name() == "simnow.exe":
                proc.kill()
        log.close()
        time.sleep(5)
        try:
            outputLog = open("outputLog.log", "w")
            outputLog.write(LOG_CONTENT)
            outputLog.close()
            os.rename("outputLog.log", "..\\..\\port80h_snoop.log")
            # os.remove(BIOS_IMAGE)
            exit_codes.exit("UNSTABLE")
        except Exception as exp:
            print(exp)
            exit_codes.exit("UNSTABLE")
