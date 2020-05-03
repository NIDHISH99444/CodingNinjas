

def writingfunction(bsdFileLocation,BIOSFileLocation,HDDfileLocation,LogLocation):
    with open("SimNow_MR-SimNow_template", 'r') as ra:
        with open("SimNow_MR-SimNow.script", 'w')as wf:
            for line in ra:
                if "shell.open" in line:
                    line=line.rstrip('\n')+' '+bsdFileLocation
                    wf.write(line)
                    wf.write('\n')
                elif "memdevice:0.InitFile" in line:
                    line = line.rstrip('\n') + ' ' + BIOSFileLocation
                    wf.write(line)
                    wf.write('\n')
                elif "shell.SetLogFile" in line:
                    line = line.rstrip('\n') + ' ' + LogLocation
                    wf.write(line)
                    wf.write('\n')
                elif "nvmedrive:0.SetImage" in line:
                    line = line.rstrip('\n') + ' ' + HDDfileLocation
                    wf.write(line)
                    wf.write('\n')

                else:
                    wf.write(line)

def readingDirectoryPath(dirPath):
    import os
    dirFileList = os.listdir(dirPath)
    return dirFileList

# shell.open C:\SimNow\aransas_mr_ff3_family17h.bsd
# memdevice:0.InitFile D:\MERO_bios\MaunaExtUDK-16MB-0032-SimNow.FD
# shell.SetLogFile D:\MERO_bios\SimNow_MR-log-20200426_1539-SimNow.txt
# nvmedrive:0.SetImage D:\MERO_bios\win10_efi.hdd
print("Enter Directory Path")
dirPath=input()
dirFileList=readingDirectoryPath(dir)
# print("Enter BSD file location(.BSD)")
# bsdFileLocation=input()
# print("Enter BIOS file location(.FD)")
# BIOSFileLocation=input()
# print("Enter HDD file location")
# HDDfileLocation=input()
# print("Enter log location")
# LogLocation=input()

#writingfunction(bsdFileLocation,BIOSFileLocation,HDDfileLocation,LogLocation)
