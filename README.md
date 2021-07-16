# calcNewDateByGivenDays

## Main Purpose
Creating a new date-time by a given date and a given number of days

## Algorithm
1.return new date by calculating the given date + number of days given

2.by a given days, calculate if we pass to a new year by calculating the remaining days to finish a year plus the given days

3.iterate each month with the given days, while each iteration deduct the "used" days, and creating a new temp date untill finishing accumulative the days into the given date

## Testing used
I used the strptime function from datetime module to test my results

## Extra cases and testing
Testing the input we got
Year - Testing if the input is digit
Month - Testing if the input is digit, and between 1 to 12
Day - Testing if the input is digit, and between 1 to the max current month given
addedDays - Testing if the input is digit, and greater than 0
Added a small case inside the switcher if we are on leap year (February is 29 days instead of 28)
