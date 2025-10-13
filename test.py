from datetime import timedelta,datetime

startTimeALL=datetime.strptime("11:45","%H:%M")#获取输入并转换为'datetime.datetime
time_interval1 = timedelta(minutes=int(45))#将用户输入考试时长的数字转换为时间
end= startTimeALL+time_interval1
Testseconds = time_interval1.total_seconds()#将用户输入的分钟转为秒
print(type(end))
print(end)
print(type(Testseconds))
print(Testseconds)