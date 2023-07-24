#import libraires
import datetime as dt
import numpy as np

#define birth date
year, month, day = [int(item) for item in input('Enter Year, Month and Day: ').split(' ')]

#define input and variables
def birth_days(year, month, day):
	days = (dt.datetime.today() - dt.datetime(year, month, day)).days
	return days

days = birth_days(year = year, month = month, day =day)

kind = {
	'Physical': int(23),
    'Emotional': int(28),
    'Intellectual': int(33)
}

#define biorhythm function
def biorythm(days,kind):
	return np.sin(2*np.pi*days/kind)
                
#print output
for var in kind.keys():
	print(f'{var}: {round(100*biorythm(days,kind.get(var)),2)}%')
