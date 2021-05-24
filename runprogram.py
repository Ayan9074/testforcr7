import os
import schedule
import time
import random
#os.system('C:/Users/Ayan/AppData/Local/Programs/Python/Python38/python.exe FinalYoutubeUpload.py')
def uploadvid():
    os.system('C:/Users/Ayan/AppData/Local/Programs/Python/Python38/python.exe FinalYoutubeUpload.py')

def restartschedules():
    #schedule.clear()
    #schedule.every().day.at("00:00").do(upload)
    schedule.every().day.at("00:00").do(uploadvid)
    schedule.every().day.at("06:00").do(uploadvid)
    schedule.every().day.at("07:00").do(uploadvid)
    schedule.every().day.at("08:00").do(uploadvid)
    schedule.every().day.at("09:00").do(uploadvid)
    schedule.every().day.at("10:00").do(uploadvid)
    schedule.every().day.at("11:00").do(uploadvid)
    schedule.every().day.at("12:00").do(uploadvid)
    schedule.every().day.at("13:00").do(uploadvid)
    schedule.every().day.at("14:00").do(uploadvid)
    schedule.every().day.at("15:00").do(uploadvid)
    schedule.every().day.at("16:00").do(uploadvid)
    schedule.every().day.at("17:00").do(uploadvid)
    schedule.every().day.at("18:00").do(uploadvid)
    schedule.every().day.at("19:00").do(uploadvid)
    schedule.every().day.at("20:00").do(uploadvid)
    schedule.every().day.at("21:00").do(uploadvid)
    schedule.every().day.at("22:00").do(uploadvid)
    schedule.every().day.at("23:00").do(uploadvid)
    schedule.every().day.at("01:00").do(uploadvid)
    schedule.every().day.at("02:00").do(uploadvid)
    schedule.every().day.at("03:00").do(uploadvid)
    schedule.every().day.at("04:00").do(uploadvid)
    schedule.every().day.at("05:00").do(uploadvid)

restartschedules()

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
    print('Waiting ... boring ... long time long time')