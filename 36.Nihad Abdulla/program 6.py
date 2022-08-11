from datetime import date
def minimum(date1,date2):
    return min(date1,date2)
date1 = date(2018, 12, 13)
date2 = date(2019, 2, 25)
print(minimum(date1,date2))
