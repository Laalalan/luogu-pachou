import tkinter as tk


def crawl():
    # 爬取逻辑代码
    pass


# 创建GUI窗口
window = tk.Tk()
window.title("题目筛选与爬取")

# 获取屏幕宽度和高度
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# 设置页面大小
window_width = int(screen_width / 3)
window_height = int(screen_height * 0.5)
window.geometry(f"{window_width}x{window_height}")

# 题目难度选项
difficulties = [
    "暂无评定入门",
    "普及-",
    "普及/提高-",
    "普及+/提高",
    "提高+/省选-",
    "省选/NOI-",
    "NOI/NOI+/CTSC"
]

# 创建框架容器
frame = tk.Frame(window)
frame.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

# 第一排 - 筛选条件
filter_label = tk.Label(frame, text="筛选条件：")
filter_label.pack(anchor=tk.W, pady=3)

# 单独选的形式在一个框中呈现题目难度选项
difficulty_frame = tk.Frame(frame)
difficulty_frame.pack(anchor=tk.W, padx=5)

row1_frame = tk.Frame(difficulty_frame)
row1_frame.pack(side=tk.TOP, anchor=tk.W)

row2_frame = tk.Frame(difficulty_frame)
row2_frame.pack(side=tk.TOP, anchor=tk.W)

checkbox_vars = []
checkboxes = []

for i, difficulty in enumerate(difficulties[:4]):
    var = tk.IntVar()
    checkbox = tk.Checkbutton(row1_frame, text=difficulty, variable=var)
    checkbox.pack(side=tk.LEFT, padx=2, pady=1)
    checkbox_vars.append(var)
    checkboxes.append(checkbox)

for i, difficulty in enumerate(difficulties[4:]):
    var = tk.IntVar()
    checkbox = tk.Checkbutton(row2_frame, text=difficulty, variable=var)
    checkbox.pack(side=tk.LEFT, padx=2, pady=1)
    checkbox_vars.append(var)
    checkboxes.append(checkbox)

# 开始题号和截至题号
filter_label = tk.Label(frame, text="开始题号")
filter_label.pack(side=tk.LEFT, anchor=tk.W, pady=3)

min_entry = tk.Entry(frame)
min_entry.pack(side=tk.LEFT, anchor=tk.W)

filter_label = tk.Label(frame, text="截至题号")
filter_label.pack(side=tk.LEFT, anchor=tk.W, pady=3)

max_entry = tk.Entry(frame)
max_entry.pack(side=tk.LEFT, anchor=tk.W)

# 开始爬虫按钮
crawl_button = tk.Button(frame, text="开始爬虫", command=crawl)
crawl_button.pack(side=tk.LEFT, padx=5)

# 爬取结果框架
result_frame = tk.Frame(window)
result_frame.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

# 爬取进度
progress_label = tk.Label(result_frame, text="爬取进度：")
progress_label.pack(side=tk.LEFT, anchor=tk.W, pady=3)

progress_text = tk.Text(result_frame, height=int(
    window_height * 0.04), width=int(window_width*0.05))
progress_text.pack(side=tk.LEFT, anchor=tk.W)

# 爬取结果
result_label = tk.Label(result_frame, text="爬取结果：")
result_label.pack(side=tk.RIGHT, anchor=tk.W, pady=3)

result_text = tk.Text(result_frame, height=int(
    window_height * 0.04), width=int(window_width*0.05))
result_text.pack(side=tk.RIGHT, anchor=tk.W)

# # 第三排左边 - 爬取进度
# progress_label = tk.Label(frame, text="爬取进度：")
# progress_label.pack(side=tk.LEFT, anchor=tk.W, pady=5)

# progress_text = tk.Text(frame, height=window_height *
#                         0.25, width=int(window_width*0.09))
# progress_text.pack()

# # 第三排右边 - 爬取结果
# result_label = tk.Label(frame, text="爬取结果：")
# result_label.pack(side=tk.RIGHT, anchor=tk.W, pady=5)

# result_text = tk.Text(frame, height=window_height *
#                       0.25, width=int(window_width*0.09))
# result_text.pack()


window.mainloop()
