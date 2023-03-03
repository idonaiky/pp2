import math
from datetime import datetime
def f():
  a = str(raw_input('Enter full data separated by spaces: '))
  b = str(raw_input('Enter full data separated by spaces: '))
  date_format_str = '%d %m %Y %H %M %S'
  s = datetime.strptime(a, date_format_str)
  k =   datetime.strptime(b, date_format_str)
  d = abs(k - s)
  print(d.total_seconds())

f()
