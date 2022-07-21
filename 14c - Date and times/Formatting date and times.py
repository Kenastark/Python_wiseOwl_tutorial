
import datetime

# memorable date/time
memorable_time = datetime.datetime(2001,9,11,8,45,0)

# show this as dddd, dd mmmm, yyyy at hh:MM:ss am
print(memorable_time.strftime("%A %d %B %Y"))

# print the time
print(memorable_time.strftime("%I:%M:%S %p"))

