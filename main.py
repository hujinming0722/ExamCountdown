from tkinter import Tk,Label,N,E,W,S,Entry,Button
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
tip2=Label(text="请输入此次考试的开始时间",font=("TkDefaultFont",16))
tip2.grid(row=3,column=0,sticky=W)
EntryStartTime=Entry(font=("TkDefaultFont",16),width=5)
EntryStartTime.grid(row=3,column=1)
ButtonOfExit=Button(text="退出",command=root.destroy)
ButtonOfExit.grid(row=4,column=0,sticky=E)
ButtonOfStart=Button(text="开始考试")
ButtonOfStart.grid(row=4,column=1,sticky=E)
def ExamStart():
    import time
    



root.mainloop()