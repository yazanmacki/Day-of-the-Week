import re
import math

def getWordFromString(the_string):
    word = ""

    for char in the_string:
        if char.isalpha():
            word += char

    return word

number_of_days = [31,28,31,30,31,30,31,31,30,31,30,31]
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

valid = False

format1 = "[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]"
format2 = "[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]"
format3 = "[0-9][0-9] (January|February|March|April|May|June|July|August|September|October|November|December) [0-9][0-9][0-9][0-9]"

while not valid:
    date_string = input("Type in the date: ")

    two_digit_number = "[0-9][0-9]"

    two_digit_nums = re.findall(two_digit_number, date_string)

    inFormat1 = re.findall(format1, date_string)
    inFormat2 = re.findall(format2, date_string)
    inFormat3 = re.findall(format3, date_string)

    if inFormat1 != [] or inFormat2 != []:
        day = int(two_digit_nums[0])
        month = int(two_digit_nums[1])
        century = int(two_digit_nums[2])
        year = int(two_digit_nums[3])
        valid = True
    elif inFormat3 != []:
        day = int(two_digit_nums[0])
        month = months.index(getWordFromString(inFormat3)) + 1
        century = int(two_digit_nums[1])
        year = int(two_digit_nums[2])
        valid = True
    else:
        valid = False

    if valid:
        if year % 4 == 0 and year != 0:
            leap = True
        elif year == 0:
            if century % 4:
                leap = True
            else:
                leap = False
        else:
            leap = False

    if valid:
        if month <= 12:
            if leap and month == 2:
                if day <= number_of_days[month - 1] + 1:
                    valid = True
                else:
                    valid = False
            else:
                if day <= number_of_days[month - 1]:
                    valid = True
                else:
                    valid = False
        else:
            valid = False

month_contributions = [4,0,0,3,5,1,3,6,2,4,0,2]
century_contribution_index = century - (math.floor(century/4) * 4)
century_contributions = [0,5,3,1]
days_of_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

total = math.floor(year/4) + year + 2 + day + month_contributions[month - 1] + century_contributions[century_contribution_index]

day_week = total % 7

if leap and (month == 1 or month == 2):
    day_week = day_week - 1

print(days_of_week[day_week])
