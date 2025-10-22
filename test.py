import json
import os
from tkinter import (Tk, Label, Entry, Button, Listbox, Scrollbar, messagebox,
                     ttk, END, SINGLE, Toplevel,LabelFrame)
from tkcalendar import DateEntry
from datetime import datetime

# 全局配置
JSON_PATH = "exam_schedule.json"
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
    global current_date
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
    top = Toplevel(root)
    top.title("选择日期")
    top.grid_columnconfigure(0, weight=1)
    
    Label(top, text="请选择考试日期：").grid(row=0, column=0, pady=10, padx=10, sticky="n")
    cal = DateEntry(top, date_pattern="yyyy-mm-dd", width=12)
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
    
    top = Toplevel(root)
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


# 主窗口
root = Tk()
root.title("考试时间录入")
root.geometry("800x500")
root.grid_rowconfigure(1, weight=1)  # 内容区域自适应高度



# 左侧日期列表区域（占1列）
root.grid_columnconfigure(0, minsize=200)  # 固定最小宽度
Label(root, text="考试日期列表", font=("SimHei", 12)).grid(
    row=0, column=0,sticky="nw")

# 日期列表（带滚动条）
date_frame = LabelFrame(root)
date_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
date_frame.grid_rowconfigure(0, weight=1)
date_frame.grid_columnconfigure(0, weight=1)

date_scroll = Scrollbar(date_frame)
date_scroll.grid(row=0, column=1, sticky="ns")
date_listbox = Listbox(
    date_frame, selectmode=SINGLE, yscrollcommand=date_scroll.set, height=15
)
date_listbox.grid(row=0, column=0, sticky="nsew")
date_scroll.config(command=date_listbox.yview)
date_listbox.bind('<<ListboxSelect>>', on_date_select)

# 添加日期按钮
Button(root, text="+ 添加日期", command=add_date).grid(
    row=2, column=0, padx=10, pady=10, sticky="ew")

# 右侧单科时间区域（占1列）
root.grid_columnconfigure(1, weight=1)  # 自适应宽度
Label(root, text="单科考试时间", font=("SimHei", 12)).grid(
    row=0, column=1,sticky="nw")

# 单科时间表格

tree_frame = LabelFrame(root)
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
add_time_btn = Button(root, text="+ 添加单科时间", command=add_time, state="disabled")
add_time_btn.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# 保存按钮
Button(root, text="💾 保存", command=save_data).grid(
    row=2, column=1, padx=10, pady=10, sticky="e")

# 初始化
data = load_data()
refresh_date_list()

root.mainloop()