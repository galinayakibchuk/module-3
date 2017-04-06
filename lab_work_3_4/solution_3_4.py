"""
Write a program, which takes a year as input and returns message if this is a leap year or note.
Please handle the exceptions which may arise is a user will enter non-numeric symbols.
Additional task – to show the closest leap year in case if entered year is not leap
Optional task - Add a possibility to print all the leap years within given range
"""
try:
    year = int(input('Please, enter the year:'))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('{} is leap year'.format(year))
    else:
        for y in [year + 1, year - 1,
                  year + 2, year - 2,
                  year + 3, year - 3]:
            if y % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                print('{} is next leap year'.format(y))
                break
except:
    print('Not a number passed')

"""
Optional task - Add a possibility to print all the leap years within given range
"""
try:
    start_year = int(input('Please, enter the start range year:'))
    end_year = int(input('Please, enter the end range year:'))

    leap_years_in_range = []
    for year in range(start_year, end_year +1):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            leap_years_in_range.append(year)

    leap_years_content = ''
    for i in range(len(leap_years_in_range)):
        separator = ', ' if i < len(leap_years_in_range) - 1 else ''
        leap_years_content += str(leap_years_in_range[i]) + separator
        if (i +1)% 10 ==0:
            leap_years_content +='\n'

    print('\tList of leap years in range from {start} to {end} is:\n[{content}]'
          .format(start=start_year, end=end_year, content=leap_years_content))

except ValueError:
    print('Wrong value passed!')








