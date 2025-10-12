from datetime import datetime,timedelta
a=datetime.strptime("11:45","%H:%M")
aa=a.time()
print(type(a.time()))
time_interval = timedelta(minutes=45)
end= a+time_interval
print(end.time())
print(datetime.now())
print(datetime.timestamp())