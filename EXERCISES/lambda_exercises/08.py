"""

8. Write a Python program to extract year, month, date and time using Lambda.
Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178

"""

import datetime

now = datetime.datetime.now()


month = lambda x: x.month
day = lambda x: x.day
year = lambda x: x.year
time = lambda x: x.time()


