import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import serial.tools.list_ports
import re
import serial

class ProcessDate(object):
    def __init__(self):
        self.port_list = serial.tools.list_ports.comports()
        self.port = None
        self.sn = None
        self.mode = None  # Move mode attribute here

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
        except Exception as e:
            return str(e)

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
        except Exception as e:
            messagebox.showerror("错误", f"写入失败: {str(e)}")

    def clear_sn(self):
        try:
            ser = self.open_serial()
            for a in range(15):
                ser.write(f'\ni2cset -y -f {self.mode} 0x50 {hex(a)} 0xFF\n')
            ser.close()
            messagebox.showinfo("信息", "写入完成！")
        except Exception as e:
            messagebox.showerror("错误", f"写入失败: {str(e)}")

    def get_sn(self):
        try:
            ser = self.open_serial()
            if self.mode != 3:
                ser.write("\ni2cdump -y -f -r 0x00-0xff 1 0x50\n")
                log_text = ser.readlines(5)
                return log_text
            else:
                ser.write("\ni2cdump -y -f -r 0x00-0xff 3 0x50\n")
                log_text = ser.readlines(5)
                return log_text
        except Exception as e:
            return str(e)

class WriteSerialNumApp:
    def __init__(self, master):
        self.master = master
        self.data = ProcessDate()
        self.port_list = self.data.port_list
        master.title('Write SN')
        master.geometry("")
        self.sn_value = tk.StringVar()
        self.select_sn = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # 创建第1容器
        first_frame = ttk.Frame(self.master)
        tk.Label(first_frame, text='端口：').grid(row=1, column=3)
        combo = ttk.Combobox(first_frame, values=self.port_list)
        combo.grid(row=1, column=2, sticky="w")
        combo.set(self.port_list[0])
        self.data.port = combo.get()
        tk.Button(first_frame, text='选择', command=self.data.open_serial).grid(row=1, column=3, sticky="w")

        # 创建第2个容器
        second_frame = ttk.Frame(self.master)
        tk.Label(second_frame, text='选择平台：').grid(row=2, column=1, sticky="w")
        self.data.mode = tk.StringVar(value="T113")  # Set default mode
        t113_mode = ttk.Radiobutton(second_frame, text="T113", variable=self.data.mode, value="T113")
        t5_mode = ttk.Radiobutton(second_frame, text="T5", variable=self.data.mode, value="T5")
        cf_mode = ttk.Radiobutton(second_frame, text="CFM", variable=self.data.mode, value="CFM")
        t113_mode.grid()
        t5_mode.grid()
        cf_mode.grid()

        # 创建第3个容器
        third_frame = ttk.Frame(self.master)
        tk.Label(third_frame, text='SN:').grid(row=3, column=1, sticky="w")
        sn_entry = tk.Entry(third_frame, textvariable=self.sn_value, validate="focusout",
                            validatecommand=(third_frame.register(self.data.validate_input), '%P'))
        self.data.sn = sn_entry.get()
        sn_entry.grid(row=3, column=2, sticky="w")
        write_button = tk.Button(third_frame, text='写入', command=self.data.write_sn)
        write_button.grid(row=4, column=1, sticky="w")
        clear_button = tk.Button(third_frame, text='擦除', command=self.data.clear_sn)
        clear_button.grid(row=4, column=2, sticky="w")
        select_button = tk.Button(self.master, text='查询', command=self.select_sn_val)
        select_button.grid(row=4, column=3, sticky="w")

    def select_sn_val(self):
        self.select_sn = self.data.get_sn()
        fourth_frame = ttk.Frame(self.master)
        tk.Label(fourth_frame, text='查询结果：').grid(row=5, column=1, sticky="w")
        fifth_frame = ttk.Frame(self.master)
        textbox = tk.Text(fifth_frame, height=10, width=50)
        textbox.grid(row=6, columnspan=3, sticky="w")
        textbox.insert(tk.END, self.select_sn)


if __name__ == "__main__":
    root = tk.Tk()
    app = WriteSerialNumApp(root)
    root.mainloop()
