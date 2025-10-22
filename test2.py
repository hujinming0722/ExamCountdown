import json
import os
from tkinter import Tk, Frame, Button, Label, Entry, Listbox, Scrollbar,messagebox, END, SINGLE
from tkcalendar import DateEntry  # 需安装：pip install tkcalendar
from datetime import datetime# 配置
JSON_PATH = "exam_schedule.json"
DATE_FORMAT = "%Y-%m-%d"  # 日期格式
TIME_FORMAT = "%H:%M"     # 时间格式
data = {}  # 存储结构: {日期: [考试信息列表]}
current_date = None
date_listbox = None
time_tree = None
add_time_btn = None

#加载文件
if os.path.exists(JSON_PATH):
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            data= json.load(f)
    except:
        data= {}
data= {}

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

