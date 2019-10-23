# A module is basically a file containing a set of functions to include in your application
# they are core python modules, can be installed using pip package manager

# Core modules
import datetime
from datetime import date
# imported date from datettime
import time
from time import time

# date of the day
today = date.today()
print(today)

# timestamp
timestamp = time()
print(timestamp)

# import custom module from validator.py
import validator
from validator import validate_email

email = 'test@gmail.com'
if validate_email(email):
    print('Valid Email Detected')
else:
    print('Invalid Email Detected')