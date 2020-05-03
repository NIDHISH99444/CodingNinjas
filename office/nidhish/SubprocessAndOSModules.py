import time
from datetime import datetime
import  subprocess
import os  # allow to interact  with underlying OS
# with open("output.txt","w") as f:
#     p1=subprocess.run('dir',shell=True,stdout=f,text=True)
# print(p1.args)
# print(p1.returncode)
# print(p1.stdout)
# print()
#print(p1.stderr)

# p1=subprocess.run('type output.txt',shell=True,capture_output=True,text=True)
# print(p1.returncode)
# print(p1.stdout)
#
# p2=subprocess.run('findstr Volume',shell=True,capture_output=True,text=True,input=p1.stdout)
# print("Taking input from first file and grepping string containing 'Volume as keyword':----------")
# print(p2.stdout)
# TIMESTAMP_NOW = time.time()
# print(TIMESTAMP_NOW)
#---------------------------------------
#OS module
print("print content in OS module")
print(dir(os))
print("print current directory")
print(os.getcwd())
print("changing the working directory and checking if it has changed")
os.chdir("D:\TRy\TryCopy")
print(os.getcwd())
print("Printing the content in dir 'D:\TRy\TryCopy'")
print(os.listdir())
#to create the directory win10_efi11.hdd we prefer to use makedirs as it can make tree structure as well
#os.makedirs('win10_efi11.hdd')
#os.makedirs('win10_efi12.hdd/abcd')

#os.makedirs('win10_efi12.hdd/pqrst')
#deleting folder
#os.rmdir('win10_efi12.hdd/pqrs')
# print("rename file")
# os.rename("win10_efi.hdd","win10_efi.hdd_cc")
# print(os.listdir())
print("Os stat ")
print("getting date time of module ")
mod_time=(os.stat("win10_efi.hdd_cc").st_mtime)
print(mod_time)
print("making date time in huma redable form(time when file was created) ")
print(datetime.fromtimestamp(mod_time))

print("We want to see the directory tree uses os.walk method---------------------")
for dirpath,dirname,filename in os.walk(os.getcwd()):
    print("current directory",dirpath)
    print("Directory names",dirname)
    print("Filename",filename)

print("compete directory tracversal for file --------------------------")
print("Os path module ")

file_path=os.path.join(os.getcwd(),'Nidhish.txt')
print(file_path)

print("creating the file")
f=open(file_path,'w')
f.write("this is the file ")
f.close()
print(f.closed)
print("check path exists")
print(os.path.exists("D:\TRy\TryCopy"))
print("checking 'D:\TRy\TryCopy\\Nidhish.txt' is file")
print(os.path.isfile(file_path))
print("checking 'D:\TRy\TryCopy\\Nidhish.txt' is directory")
print(os.path.isdir(file_path))

print(os.path.splitext(file_path))








