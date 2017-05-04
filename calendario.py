import calendar, datetime

def hojaMes(mes):
    if mes <0 or mes>12:
        print("eres tonto")
    else:
        cal = calendar.month(2017, mes)
        print(cal)

hojaMes(5)

x = datetime.datetime.now()
print(x)
print(x.isoformat())
print(x.astimezone())
print(x.day)

print(x.max)




