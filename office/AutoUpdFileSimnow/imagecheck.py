import sys
import os
import re
import time
import datetime
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    todayDate=datetime.date.today()
    logging.basicConfig(filename="check.log", level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    date_list = []

    def checkDate():

        for i in range(4,-5,-1):     #checking dates in the range of 4 days from todays date and previous 5 days e
            tdelta = datetime.timedelta(days=i)
            # print(todayDate - tdelta)
            year, month, date = str(todayDate + tdelta).split('-')
            date_list.append(month + '_' + date + '_' + year[2:])
            # print(month + '_' + date + '_' + year[2:])
        print("Date Range for checking in 'path(D:\Learning)' folder :-",date_list)

    def readingLogFile():
        getRequiredDate = 0
        finalResultantFile = ""
        for line in reversed(list(open("check.log"))):   #reversed the check.log so that we can start reading from the latest line which was updated in check.log
            for dateCheck in date_list:                  #checking the first date in the "dateCheck" which match the check.log file and if it matches just breaking out of the loop
                if dateCheck in line and 'int.exe'in line  and getRequiredDate == 0:
                    finalResultantFile = line.split('\\')[-1]
                    print(finalResultantFile)   #printing the last updated file in the check.log which was updated after reading the path="D:\Learning"
                    getRequiredDate = 1
                    break


#############################

    def noOfLineCalculator():
        num_lines=0
        with open('check.log', 'r') as f:
            for line in f:
                num_lines += 1

        return num_lines


    #path = sys.argv[1] if len(sys.argv) > 1 else '.'
    #Reading the folder where the files will be appended
    path="D:\Learning"

    checkDate()   #checkDate() function check the date range for which we want to check if "*int.exe" file is present
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()                #observer.start() is checking the "path" folder for updates
    try:
        while True:
            prevLines=noOfLineCalculator()          #lines calculation in "check.log"
            print("Prev Number of lines in 'check.log' :- ",prevLines)
            time.sleep(10)                  #checking the path folder every 10 seconds

            currLines=noOfLineCalculator()
            print("curr Number of lines in 'check.log' :- ", currLines)
            if currLines>prevLines:     # if there is change in no of lines then we will read the "check.log" for the updated simnow*****int.exe version
                readingLogFile()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

