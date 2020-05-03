import glob
import os,re
from datetime import datetime
start=datetime.now()
print(start)
print(os.listdir())


PATH=os.getcwd()
print(PATH)
#
# print("----------------------------")
# with open(PATH + '\port80h_snoop1.log', 'r') as log:
#     try:
#             line = log.readline()
#             print(line)
#             cleanLine = re.sub(r"Yuba:.", " ", line).rstrip()
#             print("Print Clearline",cleanLine)
#             # if cleanLine != "":
#     except Exception:
#         print("general Exception ")
import fileinput
with open("config.txt") as cfg_file:
    for line in cfg_file:
        if 'shell.open' in line:
            print(line)
            old_hdd = line.split(' ')[1]
            print(old_hdd)
for line in fileinput.input("config.txt", inplace=True):
    print(line.replace(old_hdd,"haha").strip('\n'))