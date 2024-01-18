import tkinter as tk
import re
import serial.tools.list_ports
import serial
from tkinter import ttk
from tkinter import messagebox

# class WriteSerialNum:
#     def __init__(self, master):

mode = 1
# 初始化窗口宽高
S_WIDTH = 300
S_HEIGHT = 500


def select_mode():
    global mode
    if combo_mode.get() == "T113":
        return mode
    elif combo_mode.get() == "T5":
        mode = 3
        return mode


def get_available_ports():
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]


def write_serial():
    ser = open_serial()
    sn = SN_entry.get()
    mode_num = mode
    if sn:
        for m, i in enumerate(sn):
            ser.write(f"i2cset -y -f {mode_num} 0x50 {hex(m)} {ord(i)}\n")
        ser.write(f'i2cset -y -f {mode_num} 0x50 0xf 00\n')
        messagebox.showinfo("信息", "写入完成！")

    else:
        for i in range(17):
            ser.write(f'i2cset -y -f {mode_num} 0x50 0xf 0xFF\n')
            messagebox.showinfo("信息", "写入完成！")


def open_serial():
    ser = serial.Serial(combo.get(), 115200, timeout=0.5)
    if ser:
        tk.messagebox.showinfo("信息", "打开成功")
    else:
        tk.messagebox.showinfo("信息", "打开失败")
    return ser


def validate_input(sn):
    if len(sn) != 15 or (len(sn) >= 4 and not re.match(r'^[a-zA-Z]*$', sn[:4])):
        return False
    return True


def window_resize(event=None):
    if event is not None:
        # listen events of window resizing.
        # 窗口宽高任一值产生变化，则记录并使展示高清大图自适应窗体调整。
        # 1)
        if window_width != master.winfo_width() or window_height != master.winfo_height():
            if window_width != master.winfo_width():
                window_width = master.winfo_width()
            if window_height != master.winfo_height():
                window_height = master.winfo_height()
            # What happens here?
            if first_load:
                first_load = False
            else:
                # 重新设置展示的图片大小
                load_image(image_pos)


master = tk.Tk()  # 实例化
master_frame = tk.Frame(master)
master.title('Write SN')
master.wm_title('Write SN')
# 默认窗口包含标题栏
master.overrideredirect(False)
# 初始化窗口大小并自适应屏幕居中
master.geometry(str(S_WIDTH) + 'x' + str(S_HEIGHT) + '+'
                + str((master.winfo_screenwidth() - S_WIDTH) // 2) + '+'
                + str((master.winfo_screenheight() - S_HEIGHT) // 2 - 18))
# 第一次加载，因为监听窗口大小调整事件，初始化时会调用绑定'<Configure>'的函数/方法
first_load = True
# 注册（绑定）窗口变动事件
master.bind('<Configure>', window_resize)

"""第0行"""
tk.Label(master, text='端口：').grid(row=1, column=0, columnspan=4, ipadx=10)
# 添加下拉框,获取当前值
options = get_available_ports()
combo = ttk.Combobox(master, values=options)
combo.grid(row=1, column=1, columnspan=4)

# 绑定事件，当选择发生变化时调用 on_select 函数
combo.bind('<Configure>', get_available_ports)
# 选择按钮，触发打开串口
select_button = tk.Button(master, text='选择', command=open_serial)
select_button.grid(row=1, column=2, columnspan=4)

"""第2行"""
tk.Label(master, text='平台：').grid(row=2, column=0, sticky="w")
# 选择平台，对应不对I2c总线
mode_options = ["T113", "T5", "CF"]
ttk.Combobox(master, values=mode_options).grid(row=2, column=1)

"""第4行"""
validate_input_command = master.register(validate_input)
tk.Label(master, text='SN：').grid(row=3, column=0, sticky="w")
SN_entry = tk.Entry(master, validate="key", validatecommand=(validate_input_command, '%P'))
SN_entry.grid(row=3)
tk.Button(master, text='写入', command=write_serial).grid(row=3, column=1)
tk.Button(master, text='擦除', command=write_serial).grid(row=3, column=2)
tk.Button(master, text='查询', command=write_serial).grid(row=3, column=3)

"""第6行"""
tk.Label(master, text='写入结果:').grid(row=6, sticky="w")
command_text = tk.Text(master, height=2, width=10)
command_text.grid(row=8)

tk.OptionMenu(master, value="开始", variable=options)
master.mainloop()
