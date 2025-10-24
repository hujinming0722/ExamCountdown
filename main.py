import json
import os
from tkinter import Tk, LabelFrame, Button, Label, Entry, Listbox, Scrollbar,messagebox, END, SINGLE,N,E,W,ttk,Toplevel

from datetime import datetime,date
JSON_PATH = "exam_schedule.json"
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
#这段有关多日设置


def Settonsofday():
    # 全局配置
    
    DATE_FORMAT = "%Y-%m-%d"
    TIME_FORMAT = "%H:%M"

    # 全局变量
    data = {}  # 存储结构: {日期: [考试信息列表]}
    current_date = None
    date_listbox = None
    time_tree = None
    add_time_btn = None 
    def load_data():
        """加载已有数据"""
        if os.path.exists(JSON_PATH):
            try:
                with open(JSON_PATH, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                return {}
        return {}


    def refresh_date_list():
        """刷新日期列表"""
        date_listbox.delete(0, END)
        for date in sorted(data.keys()):
            date_listbox.insert(END, date)


    def on_date_select(event):
        """处理日期选择事件"""
        nonlocal current_date
        selected = date_listbox.curselection()
        if not selected:
            current_date = None
            add_time_btn.config(state="disabled")
            return

        current_date = date_listbox.get(selected[0])
        add_time_btn.config(state="normal")
    
        # 刷新表格
        for item in time_tree.get_children():
            time_tree.delete(item)
        for exam in data.get(current_date, []):
            time_tree.insert("", END, values=(exam["subject"], exam["start_time"], exam["duration"]))


    def add_date():
        """添加考试日期"""
        top = Toplevel(setofdayWindow)
        top.title("选择日期")
        top.grid_columnconfigure(0, weight=1)
    
        Label(top, text="请选择考试日期：").grid(row=0, column=0, pady=10, padx=10, sticky="n")

        cal = Entry(top, width=12)
        seetoday=str(date.today())
        cal.insert(0,seetoday)
        cal.grid(row=1, column=0, pady=10)
    
        def confirm():
            date = cal.get()
            if date not in data:
                data[date] = []
                refresh_date_list()
                messagebox.showinfo("提示", f"已添加日期：{date}")
            else:
                messagebox.showwarning("提示", f"日期 {date} 已存在")
            top.destroy()
    
        Button(top, text="确认", command=confirm).grid(row=2, column=0, pady=10)


    def add_time():
        """添加单科考试时间"""
        if not current_date:
            return
    
        top = Toplevel(setofdayWindow)
        top.title("添加考试时间")
        top.geometry("300x300")
        top.grid_columnconfigure(1, weight=1)
    
        # 科目输入
        Label(top, text="考试科目：").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        subject_entry = Entry(top)
        subject_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        subject_entry.insert(0, "数学")
    
        # 开始时间
        Label(top, text="开始时间：").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        time_entry = Entry(top)
        time_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        time_entry.insert(0, "09:00")
        Label(top, text="(HH:MM)", font=("SimHei", 8)).grid(row=1, column=2, padx=5, sticky="w")
    
        # 时长
        Label(top, text="时长(分钟)：").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        duration_entry = Entry(top)
        duration_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        duration_entry.insert(0, "120")
    
        def confirm():
            subject = subject_entry.get().strip()
            start_time = time_entry.get().strip()
            duration_str = duration_entry.get().strip()
        
            if not all([subject, start_time, duration_str]):
                messagebox.showerror("错误", "请填写所有字段")
                return
            try:
                datetime.strptime(start_time, TIME_FORMAT)
                duration = int(duration_str)
                if duration <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("错误", "时间格式错误或时长需为正整数")
                return
        
            data[current_date].append({
                "subject": subject,
                "start_time": start_time,
                "duration": duration
            })
            on_date_select(None)
            messagebox.showinfo("提示", "添加成功")
            top.destroy()
    
        Button(top, text="确认", command=confirm).grid(row=3, column=0, columnspan=2, pady=20)


    def save_data():
        """保存数据到JSON"""
        if not data:
            messagebox.showwarning("提示", "暂无数据可保存")
            return
    
        try:
            with open(JSON_PATH, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            messagebox.showinfo("成功", f"已保存到 {JSON_PATH}")
        except Exception as e:
            messagebox.showerror("错误", f"保存失败：{str(e)}")
    setofdayWindow = Tk()
    setofdayWindow.title("考试时间录入")
    setofdayWindow.geometry("800x500")
    setofdayWindow.grid_rowconfigure(1, weight=1)  # 内容区域自适应高度



        # 左侧日期列表区域（占1列）
    setofdayWindow.grid_columnconfigure(0, minsize=200)  # 固定最小宽度
    Label(setofdayWindow, text="考试日期列表", font=("SimHei", 12)).grid(
    row=0, column=0,sticky="nw")

# 日期列表（带滚动条）
    date_frame = LabelFrame(setofdayWindow)
    date_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    date_frame.grid_rowconfigure(0, weight=1)   
    date_frame.grid_columnconfigure(0, weight=1)

    date_scroll = Scrollbar(date_frame)
    date_scroll.grid(row=0, column=1, sticky="ns")
    date_listbox = Listbox(
        date_frame, selectmode=SINGLE, yscrollcommand=date_scroll.set, height=15)
    date_listbox.grid(row=0, column=0, sticky="nsew")
    date_scroll.config(command=date_listbox.yview)
    date_listbox.bind('<<ListboxSelect>>', on_date_select)

    # 添加日期按钮
    Button(setofdayWindow, text="+ 添加日期", command=add_date).grid(
        row=2, column=0, padx=10, pady=10, sticky="ew")

    # 右侧单    科时间区域（占1列）
    setofdayWindow.grid_columnconfigure(1, weight=1)  # 自适应宽度
    Label(setofdayWindow, text="单科考试时间", font=("SimHei", 12)).grid(
        row=0, column=1,sticky="nw")

    # 单科时间表格

    tree_frame = LabelFrame(setofdayWindow)
    tree_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
    tree_frame.grid_rowconfigure(0, weight=1)
    tree_frame.grid_columnconfigure(0, weight=1)

    columns = ("科目", "开始时间", "时长(分钟)")
    time_tree = ttk.Treeview(
        tree_frame, columns=columns, show="headings", height=10
    )
    for col in columns:
        time_tree.heading(col, text=col)
        time_tree.column(col, width=150)
    time_tree.grid(row=0, column=0, sticky="nsew")

    # 添加单科时间按钮
    add_time_btn = Button(setofdayWindow, text="+ 添加单科时间", command=add_time, state="disabled")
    add_time_btn.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # 保存按钮
    Button(setofdayWindow, text="保存", command=save_data).grid(row=2, column=1, padx=10, pady=10, sticky="e")

    # 初始化
    data = load_data()
    refresh_date_list()
    

    setofdayWindow.mainloop()



ButtonOfStart=Button(text="开始考试",command=ExamStart)
ButtonOfStart.grid(row=4,column=1,sticky=E)
ButtonOfMakelist=Button(text="设定多日或多次考试",command=Settonsofday)
ButtonOfReadlist=Button(text="读取多日或多次考试并开始")
ButtonOfMakelist.grid(row=4,column=2,sticky=E)
ButtonOfReadlist.grid(row=4,column=3,sticky=E)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
windowX = int((screen_width - window_width) / 2)
windowY = int((screen_height - window_height) / 2)
root.geometry(f"+{windowX}+{windowY}")

root.mainloop()