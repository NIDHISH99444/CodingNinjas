import os

def writingfunction(dirPath,dirFileList):
    with open("SimNow_MR-SimNow_template", 'r') as ra:
        with open("SimNow_MR-SimNow.script", 'w')as wf:
            for line in ra:
                # if "shell.open" in line:
                #
                #     line=line.rstrip('\n')+' '+bsdFileLocation
                #     wf.write(line)
                #     wf.write('\n')
                if "memdevice:0.InitFile" in line:
                    flag=0
                    for entry in dirFileList:
                        if ".FD" in entry:
                            BIOSFileLocation = entry
                            flag=1
                            break
                    if flag==1:
                        line = line.rstrip('\n') + ' ' +dirPath+'\\'+BIOSFileLocation
                        wf.write(line)
                        wf.write('\n')
                    else:
                        line ="# "+line.rstrip('\n')
                        wf.write(line)
                        wf.write('\n')
                elif "shell.SetLogFile" in line:
                    flag=0
                    for entry in dirFileList:
                        if "log" in entry:
                            LogLocation = entry
                            flag=1
                            break
                    if flag==1:
                        line = line.rstrip('\n') + ' ' +dirPath+'\\'+LogLocation
                        wf.write(line)
                        wf.write('\n')
                    else:
                        line ="# "+line.rstrip('\n')
                        wf.write(line)
                        wf.write('\n')
                elif "nvmedrive:0.SetImage" in line:
                    flag=0
                    for entry in dirFileList:
                        if ".hdd" in entry:
                            HDDfileLocation = entry
                            flag=1
                            break
                    if flag==1:
                        line = line.rstrip('\n') + ' ' +dirPath+'\\'+HDDfileLocation
                        wf.write(line)
                        wf.write('\n')
                    else:
                        line ="# "+line.rstrip('\n')
                        wf.write(line)
                        wf.write('\n')

                # elif "shell.SetLogFile" in line:
                #     line = line.rstrip('\n') + ' ' + LogLocation
                #     wf.write(line)
                #     wf.write('\n')
                # elif "nvmedrive:0.SetImage" in line:
                #     line = line.rstrip('\n') + ' ' + HDDfileLocation
                #     wf.write(line)
                #     wf.write('\n')

                else:
                    wf.write(line)

def readingDirectoryPath(dirPath):
    dirFileList = os.listdir(dirPath)
    return dirFileList

# shell.open C:\SimNow\aransas_mr_ff3_family17h.bsd
# memdevice:0.InitFile D:\MERO_bios\MaunaExtUDK-16MB-0032-SimNow.FD
# shell.SetLogFile D:\MERO_bios\SimNow_MR-log-20200426_1539-SimNow.txt
# nvmedrive:0.SetImage D:\MERO_bios\win10_efi.hdd
print("Enter Directory Path")
dirPath=input()
dirFileList=readingDirectoryPath(dirPath)
writingfunction(dirPath,dirFileList)
# for ele in dirFileList:
#     if ".FD" in ele:
#         val=ele
#         print(val)
#         break