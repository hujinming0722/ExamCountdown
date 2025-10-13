from tkinter import Tk,Label,N,E,W,S,Entry,Button
from datetime import datetime,timedelta
root=Tk()
title1=Label(text="请输入有关此次考试的信息",font=("TkDefaultFont",32))
title1.grid(row=0,column=0,sticky=N)
tip1=Label(text="请输入此次考试的科目",font=("TkDefaultFont",16))
tip1.grid(row=1,column=0,sticky=W)
EntrySub=Entry(font=("TkDefaultFont",16),width=5)
EntrySub.grid(row=1,column=1)#这个还没用上 
tip1=Label(text="请输入此次考试以分钟计算的时长",font=("TkDefaultFont",16))
tip1.grid(row=2,column=0,sticky=W)
EntryMinutes=Entry(font=("TkDefaultFont",16),width=5)
EntryMinutes.grid(row=2,column=1)
EntryMinutes.insert(0,"120")
tip2=Label(text="请输入此次考试的开始时间",font=("TkDefaultFont",16))
tip2.grid(row=3,column=0,sticky=W)
EntryStartTime=Entry(font=("TkDefaultFont",16),width=5)
EntryStartTime.grid(row=3,column=1)


now = datetime.now().strftime("%H:%M")#时间转换成字符串放到开始时间的默认值
EntryStartTime.insert(0, now)
ButtonOfExit=Button(text="退出",command=root.destroy)
ButtonOfExit.grid(row=4,column=0,sticky=E)


def ExamStart():
    
    startTimeALL=datetime.strptime(EntryStartTime.get(),"%H:%M")#获取输入并转换为'datetime.datetime
    time_interval1 = timedelta(minutes=int(EntryMinutes.get()))#将用户输入考试时长的数字转换为时间
    end= startTimeALL+time_interval1 #相加以计算出datetime形式的考试结束时间
    startTime=startTimeALL.time() #把前面内俩转换为time格式
    endTime=end.time()

#MD，Windowsapp远程桌面太难用了，输入法不好切而且还无法把键盘直接传入，Fu** microsoft

    Testseconds = time_interval1.total_seconds()#将用户输入的分钟转为秒(浮点数形式)
    print(type(startTime)) #调试时瞎写的
    print(endTime)
    print(Testseconds)

    root.destroy() #可以在root窗口下计算的工作完成之后关闭root
    countDownWindow=Tk()
    now = datetime.now()    #获取datetime格式的现在的时间
    if now < startTimeALL:#当开始时间比现在小（还未开始）
        print("a")
        timeLABEL=Label(countDownWindow,text="Test Not start",font=("TkDefaultFont",64))
    elif now.time() <= endTime:#当考试进行中
        print("b")
        timeLABEL=Label(countDownWindow,text="time",font=("TkDefaultFont",64))
        timeLABEL.grid(row=0,column=0)
        keeptime = Testseconds
        start_time= 0
        remaining_time = keeptime -  
        if a : 
    else:#考试结束
        pass

    countDownWindow.mainloop()

ButtonOfStart=Button(text="开始考试",command=ExamStart)
ButtonOfStart.grid(row=4,column=1,sticky=E)



root.mainloop()