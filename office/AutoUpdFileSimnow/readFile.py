#import re
# with open ('check.log','r') as f :
#     for line in reversed(f):
#         #if line.__contains__("ext.exe"):
#         #    print(line,end="")
#         print(line)
import datetime
todayDate = datetime.date.today()
# val=str(todayDate)
# year,month,date=str(todayDate).split('-')
# print(month+'_'+date+'_'+year[2:])
# getting dates for today and 2 days back
date_list=[]
for i in range(6,-1,-1):
    tdelta = datetime.timedelta(days=i)
    #print(todayDate - tdelta)
    year, month, date = str(todayDate+tdelta).split('-')
    date_list.append(month + '_' + date + '_' + year[2:])
    #print(month + '_' + date + '_' + year[2:])
print(date_list)
getRequiredDate=0
finalResultantFile=""
for line in (open("check.log")):
    for dateCheck in date_list:
        if dateCheck in line  and getRequiredDate==0:
            finalResultantFile=line.split('\\')[-1]
            print(finalResultantFile)
            getRequiredDate=1
            break

    #print(line.rstrip())
