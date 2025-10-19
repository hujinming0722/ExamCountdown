from tkinter import Tk,Label,N,E,W,Entry,Button, messagebox
from datetime import datetime,timedelta
#import json
root=Tk()
root.title("ExamCountdown")
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


now = datetime.now().strftime("%H:%M")#时间转换成字符串放到开始时间的默认值
EntryStartTime.insert(0, now)
ButtonOfExit=Button(text="退出",command=root.destroy)
ButtonOfExit.grid(row=4,column=0,sticky=E)


def ExamStart():
    start_time_input = EntryStartTime.get()  # 保存开始时间输入值
    minutes_input = EntryMinutes.get()       # 保存时长输入值
    subject_input = EntrySub.get()           # 保存科目输入值
    if ":" not in start_time_input:
        messagebox.showerror("错误","您需要输入正确的时间格式,冒号应该为英文冒号，请在输入时切换为英文输入法以规避此问题。")   
    subject_text = f"本场考试的科目是{subject_input}" if subject_input else "未输入考试科目"
    print(subject_input)
    
    
    startTimeALL=datetime.strptime(start_time_input,"%H:%M")#获取输入并转换为'datetime.datetime
    time_interval1 = timedelta(minutes=int(minutes_input))#将用户输入考试时长的数字转换为时间
    end= startTimeALL+time_interval1 #相加以计算出datetime形式的考试结束时间
    startTime=startTimeALL.time() #把前面内俩转换为time格式
    endTime=end.time()
    def count_down(REMSEC): # 倒计时程序主函数，但体力拎出来为了方便调试，这个函数的部分pylance忽略即可
            minutes = REMSEC // 60
            secs = REMSEC % 60
            timeLABEL.config(text=f"考试时间还有{minutes}:{secs}")
    
            if REMSEC > 0:
                # 1秒后（1000毫秒）再次调用count_down，秒数减1
                countDownWindow.after(1000, count_down, REMSEC - 1)
            else:
                timeLABEL.config(text="考试结束！")

    Testseconds = int(time_interval1.total_seconds())#将用户输入的分钟转为秒(浮点数形式)
    print(type(startTimeALL)) #调试时瞎写的
    print(startTimeALL)
    print(Testseconds)

    root.destroy() #可以在root窗口下计算的工作完成之后关闭root
    countDownWindow=Tk()
    now = datetime.now()    #获取datetime格式的现在的时间
    countDownWindow.title("ExamCountdown")

    
    if now.time() < startTime:#当开始时间比现在小（还未开始）
        today=now.date()
        
        timeLABEL=Label(countDownWindow,text=f"考试将在{start_time_input}开始",font=("TkDefaultFont",64))
        timeLABEL.grid(row=0,column=0,sticky="nsew")
        today = now.date()
        start_datetime = datetime.combine(today, startTime)  # 组合成完整 datetime
        current_datetime = now  # 现在的完整 datetime
        wait_seconds = (start_datetime - current_datetime).total_seconds()
        countDownWindow.after(int(wait_seconds * 1000), count_down, Testseconds)
        subjectlabel=Label(countDownWindow,text=f"{subject_text}",font=("TkDefaultFont",64)) #
        subjectlabel.grid(row=1,column=0)
        countDownWindow.grid_columnconfigure(0,weight=1) #设置权重以在全屏时居中显示
        countDownWindow.grid_rowconfigure(0,weight=1)
        countDownWindow.grid_rowconfigure(1,weight=1)
    elif now.time() == startTime or now.time() > startTime < endTime :#当考试进行中
        # 更新标签显示
        timeLABEL=Label(countDownWindow,text="考试结束！",font=("TkDefaultFont",64))
        timeLABEL.grid(row=0,column=0)
        current_time = datetime.combine(now.date(), now.time())
        end_datetime = datetime.combine(now.date(), endTime)
        remaining = int((end_datetime - current_time).total_seconds())
        REMSEC = remaining if remaining > 0 else 0
        subjectlabel=Label(countDownWindow,text=f"{subject_text}",font=("TkDefaultFont",64))
        count_down(REMSEC)
        timeLABEL.grid(row=0,column=0)
        subjectlabel.grid(row=1,column=0)
        countDownWindow.grid_columnconfigure(0,weight=1)
        countDownWindow.grid_rowconfigure(0,weight=1)
        countDownWindow.grid_rowconfigure(1,weight=1)   
        
        countDownWindow.update_idletasks()
    
    
    screen_width = countDownWindow.winfo_screenwidth()
    screen_height = countDownWindow.winfo_screenheight()
    window_width = countDownWindow.winfo_reqwidth()
    window_height = countDownWindow.winfo_reqheight()
    windowX = int((screen_width - window_width) / 2)
    windowY = int((screen_height - window_height) / 2)
    countDownWindow.geometry(f"+{windowX}+{windowY}")
        

    countDownWindow.mainloop()

ButtonOfStart=Button(text="开始考试",command=ExamStart)
ButtonOfStart.grid(row=4,column=1,sticky=E)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
windowX = int((screen_width - window_width) / 2)
windowY = int((screen_height - window_height) / 2)
root.geometry(f"+{windowX}+{windowY}")

root.mainloop()