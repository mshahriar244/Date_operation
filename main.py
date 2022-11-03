from datetime import date

date1 = date(2022,1,1)
date2 = date(2022,12,1)
if date1 < date2:
    diff = date2-date1
else:
    diff = date1-date2
print(f"{date1} and {date2} " 
      f"is{diff} apart.")
