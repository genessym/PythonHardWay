import datetime 

date1 = datetime.date(1034,7,25)
date1_format = "\n{:%B %d, %Y}"
new_date = date1_format.format(date1)
print (new_date)