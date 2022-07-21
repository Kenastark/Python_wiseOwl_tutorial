
import datetime

# memorable date 
md = datetime.date(2001,9,1)

import calendar
md_formatted = "{0} {1:02} {2}, {3}".format(
    calendar.day_name[md.weekday()],
    md.day,
    calendar.month_name[md.month],
    md.year
)

# print  the formatted date
print(md_formatted)