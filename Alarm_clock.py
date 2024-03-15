import datetime
import pywhatkit

alarmHour = int(input('Enter hour (12h):  '))
alarmMinute = int(input('Enter minute:  '))
alarmTimeType = input('AM / PM:  ')

if alarmTimeType == 'PM':
    alarmHour += 12

while True:
    if alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute:
        print('Wake up now! You will be late')
        pywhatkit.playonyt('https://www.youtube.com/watch?v=KK8vGa1tCjI')
        break