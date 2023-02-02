#! python 3
# dateDetection.py - Looks at a date in DD/MM/YYYY format and confirms if date is valid.
def dateDetection():
    import re

    # create date regex and ask for input

    dateRegex = re.compile(r'(\d{2})/(\d{2})/(\d{4})$')
    date_match = dateRegex.search(input("Enter a date (DD/MM/YYYY): "))

    if date_match != None:
        day = int(date_match.group(1))
        month = int(date_match.group(2))
        year = int(date_match.group(3))
    else:
        print("Invalid format entered.")
        return

    # checks for valid date and prints results.

    valid_date = f"{date_match.group()} is a valid date."

    if 1000 <= year <= 2999:
        if month in [4,6,9,11] and day in range(1,31):
            print(valid_date)
        elif month in [1,3,5,7,8,10,12] and day in range(1,32):
            print(valid_date)
        elif month == 2:
            if year % 400 == 0 and day in range(1,30):
                print(valid_date)
            elif year % 4 == 0 and not year % 100 == 0 and day in range(1,30):
                print(valid_date)
            elif day in range (1,29):
                print(valid_date)
            else:
                print("Not a real date. Sorry!")

dateDetection()
    






