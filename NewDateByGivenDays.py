# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 11:52:50 2021
Main algorithm finished on Fri Jul 16 13:12:50 2021

@author: gal.si
"""
class UnAcceptedValueError(Exception):   
    def __init__(self, data):    
        self.data = data
    def __str__(self):
        return repr(self.data)
import datetime
#This function receives the current month and year
#Returns number of days in a given month
#Using the year to test if this year is a "leap" year, for adding a day in February
#Using the month to return the number of days in that given month
def getNumOfDaysInMonth(currMonth, year):
    switcher = {
    12: 31,
    11: 30,
    10: 31,
    9: 30,
    8: 31,
    7: 31,
    6: 30,
    5: 31,
    4: 30,
    3: 31,
    2: 28,
    1: 31
    }
    if currMonth == 2:
        if (year % 100 != 0 and year % 4 == 0 or year % 400 == 0):
            return switcher.get(currMonth) + 1
    return switcher.get(currMonth)

#This function receives a date and number of days, and returns the new calculated date
#Doing so by iterating until the given days becomes zero
#Each iteration if the days left greater than the number of days in current month, 
#substracting current days in month with current day, advancing a month(and year if needed)
#else, adding the left days into our current day(and advancing a month if needed)
def calcNewDateByGivenDays():
    isValidInfo = True
    while(isValidInfo):
        year = input("Please enter the year(YYYY):\n")
        month = input("Please enter the month:\n")
        day = input("Please enter the day:\n")
        try:
            if(year.isdigit()):
                year = int(year)
            else:
                raise UnAcceptedValueError("You should enter year as a number.\nTry again")
            if(month.isdigit() and int(month) <= 12 and int(month) >= 1):
                month = int(month)
            else:
                raise UnAcceptedValueError("You should enter month as number and between 1 to 12.\nPlease Try Again")
            if(day.isdigit() and int(day) <= getNumOfDaysInMonth(month, year) and int(day) >= 1):
                day = int(day)
            else:
                raise UnAcceptedValueError(f"You should enter day as number and between 1 to {getNumOfDaysInMonth(month, year)}")
            addedDays = input("Please enter the amount days to add to your given date:\n")
            if(addedDays.isdigit() and int(addedDays) >= 0):
                addedDays = int(addedDays)
            else:
                raise UnAcceptedValueError("You should enter number of days that is a number and greater than 0")
        except UnAcceptedValueError as e:
            print ("Received error:", e.data)
        else:
            isValidInfo = False
    tmpAddingDays = 0
    #For testing#
    current_date = f"{month}/{day}/{year % 100}"
    current_date_temp = datetime.datetime.strptime(current_date, "%m/%d/%y")
    newdate = current_date_temp + datetime.timedelta(days=addedDays)
    print(f"Testing calculated date:{newdate}")
    #/End testing#
    while(addedDays != 0):
        currMonthNumDays = getNumOfDaysInMonth(month, year)
        if addedDays > currMonthNumDays: #First case, num of given days > num days in month
            tmpAddingDays = currMonthNumDays - day + 1
            if month == 12: #If we reached December and we need to advance a year
                month = 1
                year = year+1
            else: #No advancing year needed
                month = month + 1                
            day = 1
            addedDays = addedDays - tmpAddingDays
        else: #Second case, num of given days <= num days in month
            if (day + addedDays) > currMonthNumDays: #First case insdide second case
                                                     #We still need to advance a month
                if month == 12:#If we reached December and we need to advance a year
                    year = year + 1
                    month = 1
                else: #No advancing year needed
                    month = month + 1
                day = addedDays - (currMonthNumDays - day) 
                addedDays = 0
            else: #Second case inside second case
                  #No need to advance a month, just add left-over days
                day = day + addedDays
                addedDays = 0
    print(f"New date is: {year}-{month}-{day}")
calcNewDateByGivenDays()
