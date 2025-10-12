from tkinter import Tk,Label,N,E,W,S,Entry,Button
from datetime import datetime,timedelta
root=Tk()
title1=Label(text="请输入有关此次考试的信息",font=("TkDefaultFont",32))
title1.grid(row=0,column=0,sticky=N)
tip1=Label(text="请输入此次考试的科目",font=("TkDefaultFont",16))
tip1.grid(row=1,column=0,sticky=W)
EntrySub=Entry(font=("TkDefaultFont",16),width=5)
EntrySub.grid(row=1,column=1)
tip1=Label(text="请输入此次考试以分钟计算的时长",font=("TkDefaultFont",16))
tip1.grid(row=2,column=0,sticky=W)
EntryMinutes=Entry(font=("TkDefaultFont",16),width=5)
EntryMinutes.grid(row=2,column=1)
EntryMinutes.insert(0,"120")
tip2=Label(text="请输入此次考试的开始时间",font=("TkDefaultFont",16))
tip2.grid(row=3,column=0,sticky=W)
EntryStartTime=Entry(font=("TkDefaultFont",16),width=5)
EntryStartTime.grid(row=3,column=1)
now = datetime.now().strftime("%H:%M")
EntryStartTime.insert(0, now)
ButtonOfExit=Button(text="退出",command=root.destroy)
ButtonOfExit.grid(row=4,column=0,sticky=E)
def ExamStart():
    
    startTimeALL=datetime.strptime(EntryStartTime.get(),"%H:%M")
    time_interval1 = timedelta(minutes=int(EntryMinutes.get()))
    end= startTimeALL+time_interval1
    startTime=startTimeALL.time()
    endTime=end.time()
    print(type(startTime))
    print(endTime)
    root.destroy()
    countDownWindow=Tk()
    now = datetime.now()    
    if now < startTimeALL:#当开始时间比现在小（还未开始）
        print("a")
    elif now.time() <= endTime:#当考试进行中
        print("b")
    else:#考试结束
        pass

    countDownWindow.mainloop()

ButtonOfStart=Button(text="开始考试",command=ExamStart)
ButtonOfStart.grid(row=4,column=1,sticky=E)



root.mainloop()