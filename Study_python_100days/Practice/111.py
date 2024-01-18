import tkinter as tk
import re
import serial.tools.list_ports
import serial
from tkinter import ttk
from tkinter import messagebox


class Process_Date(object):
    def __init__(self):
        self.port_list = serial.tools.list_ports.comports()
        self.port = None
        self.sn = None
        self.mode = None

    def validate_input(self):
        if self.mode == 2:
            # For mode 2, allow up to 13 characters with at least one digit and one letter
            return bool(re.match(r'^(?=.*\d)(?=.*[A-Z])[A-Z\d]{1,13}$', self.sn))

        else:
            # For modes 1 and 3, allow up to 15 characters with at least one digit and one letter
            return bool(re.match(r'^(?=.*\d)(?=.*[A-Z])[A-Z\d]{1,15}$', self.sn))

    def open_serial(self):
        try:
            ser = serial.Serial(self.port, 115200, timeout=0.5)
            return ser
        except Exception as E:
            return str(E)

    def write_sn(self):
        try:
            ser = self.open_serial()
            if self.mode != 2:
                for m, n in enumerate(self.sn):
                    ser.write(f"\ni2cset -y -f {self.mode} 0x50 {hex(m)} {ord(n)}\n")
                ser.write(f'\ni2cset -y -f {self.mode} 0x50 0xf 00\n')
                ser.close()
                tk.messagebox.showinfo("信息", "写入完成！")
            else:
                for x, y in enumerate(self.sn):
                    ser.write(f"\ni2cset -y -f 1 0x50 {hex(x)} {ord(y)}\n")
                ser.write(f'\ni2cset -y -f 1 0x50 0xe 00\n')
                ser.close()
                messagebox.showinfo("信息", "写入完成！")
        except Exception as E:
            messagebox.showerror("错误", f"写入失败: {str(E)}")

    def clear_sn(self):
        try:
            ser = self.open_serial()
            if self.mode != 2:
                for a in range(15):
                    ser.write(f'\ni2cset -y -f {self.mode} 0x50 {hex(a)} 0xFF\n')
                ser.close()
                messagebox.showinfo("信息", "写入完成！")
            else:
                for a in range(15):
                    ser.write(f'\ni2cset -y -f 1 0x50 {hex(a)} 0xFF\n')
                ser.close()
                messagebox.showinfo("信息", "写入完成！")

        except Exception as E:
            messagebox.showerror("错误", f"写入失败: {str(E)}")

    def get_sn(self):
        try:
            ser = self.open_serial()
            if self.mode != 3:
                ser.write("\ni2cdump -y -f -r 0x00-0xff 1 0x50\n")
                log_text = ser.readlines(5)
                log_text.find()


            else:
                ser.write("\ni2cdump -y -f -r 0x00-0xff 3 0x50\n")
                log_text = ser.readlines(5)
                log_text.find()
        except Exception as E:
            messagebox.showinfo("错误", f"写入失败：{str(E)}")


class WriteSerialNumApp:
    def __init__(self, master):
        self.master = master  # TK主窗口对象
        self.data = Process_Date()  # 实例化数据处理
        self.port_list = self.data.port_list  # 获取端口列表
        self.create_widgets()  # 创建窗口
        master.title('Write SN')  # 窗口标签
        master.geometry("800x480")  # 窗口尺寸

        # self.mode_value = None  # 获取模式数值
        self.select_sn = tk.StringVar()

    def create_widgets(self):
        # 创建第1容器
        first_Frame = ttk.Frame(self.master).grid(row=1)
        tk.Label(first_Frame, text='端口：').grid()  # 第1容其中标签
        combo = ttk.Combobox(self.master, values=self.port_list)  # 端口选择下拉框
        combo.grid(row=1, column=2, sticky="w")  # 设置下拉框位置
        combo.set(self.port_list[0])  # 设置下拉框默认值
        self.data.port = combo.get()
        tk.Button(self.master, text='选择', command=self.data.open_serial).grid(row=1, column=3, sticky="w")  # 绑定打开串口函数

        # 创建第2个容器
        second_Frame = ttk.Frame(self.master)
        tk.Label(second_Frame, text='选择平台：').grid(row=2, column=1, sticky="w")
        self.data.mode = tk.StringVar(value="T113")
        t113_mode = ttk.Radiobutton(second_Frame, text="T113", variable=self.data.mode, value=1,
                                    command=self.refresh_mode)
        t5_mode = ttk.Radiobutton(second_Frame, text="T5", variable=self.data.mode, value=3, command=self.refresh_mode)
        cf_mode = ttk.Radiobutton(second_Frame, text="CFM", variable=self.data.mode, value=2,
                                  command=self.refresh_mode)

        t113_mode.grid()
        t5_mode.grid()
        cf_mode.grid()

        # 创建第3个容器
        thrid_Frame = ttk.Frame(self.master)
        tk.Label(thrid_Frame, text='SN:').grid(row=3, column=1, sticky="w")
        self.sn_value = tk.StringVar()  # 获取sn
        self.sn_value.trace_add("write", self.refresh_entry)
        sn_entry = tk.Entry(thrid_Frame, textvariable=self.sn_value, validate="focusout",
                            validatecommand=(thrid_Frame.register(self.data.validate_input), '%P'))

        write_button = tk.Button(thrid_Frame, text='写入', command=self.data.write_sn)
        write_button.grid(row=4, column=1, sticky="w")
        clear_button = tk.Button(thrid_Frame, text='擦除', command=self.data.clear_sn)
        clear_button.grid(row=4, column=2, sticky="w")
        select_button = tk.Button(self.master, text='查询', command=self.select_sn_val)
        select_button.grid(row=4, column=3, sticky="w")

    def open_serial(self):
        ser = self.data.open_serial()
        if ser:
            messagebox.showinfo("信息", "打开成功！")
        else:
            messagebox.showinfo("错误", "打开失败！")


    def refresh_entry(self):
        self.sn_value = self.sn_value.get()
        self.data.sn = self.sn_value

    def refresh_mode(self):
        self.data.mode = self.data.mode.get()

    def select_sn_val(self):
        self.select_sn = self.data.get_sn
        fourth_Frame = ttk.Frame(self.master)
        tk.Label(fourth_Frame, text='查询结果：').grid(row=5, column=1, sticky="w")
        fifth_Frame = ttk.Frame(self.master)
        textbox = tk.Text(fifth_Frame, height=10, width=50)
        textbox.grid(row=6, columnspan=3, sticky="w")
        try:
            textbox.insert(tk.END, str(self.select_sn))
        except Exception as E:
            textbox.insert(tk.END, f"查询失败：{str(E)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = WriteSerialNumApp(root)
    root.mainloop()
