import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
import math
from configparser import ConfigParser

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        config = ConfigParser()
        config.read("config.ini")
        self.iconbitmap("images.ico")
        self.title("Calculator")
        self.geometry(f"{config['geometery']['x']}x{config['geometery']['y']}")
        self.minsize(380,400 )
        self.operator = f_operator(self)
        self.output = f_output(self)
        self.mainloop()


class f_operator(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.place(rely=0.2, relheight=0.8, relwidth=1)
        self.f_col()
        self.operators(parent)

    def f_col(self):
        self.col1 = ttk.Frame(self)
        self.col2 = ttk.Frame(self)
        self.col3 = ttk.Frame(self)
        self.col4 = ttk.Frame(self)

        self.col1.pack(side="left", expand=True, fill="both")
        self.col2.pack(side="left", expand=True, fill="both")
        self.col3.pack(side="left", expand=True, fill="both")
        self.col4.pack(side="left", expand=True, fill="both")

    def operators(self,parent):
        num1 = ttk.Button(self.col1, text="1", command=lambda: parent.output.calc_("1"))
        num2 = ttk.Button(self.col2, text="2", command=lambda: parent.output.calc_("2"))
        num3 = ttk.Button(self.col3, text="3", command=lambda: parent.output.calc_("3"))
        num4 = ttk.Button(self.col1, text="4", command=lambda: parent.output.calc_("4"))
        num5 = ttk.Button(self.col2, text="5", command=lambda: parent.output.calc_("5"))
        num6 = ttk.Button(self.col3, text="6", command=lambda: parent.output.calc_("6"))
        num7 = ttk.Button(self.col1, text="7", command=lambda: parent.output.calc_("7"))
        num8 = ttk.Button(self.col2, text="8", command=lambda: parent.output.calc_("8"))
        num9 = ttk.Button(self.col3, text="9", command=lambda: parent.output.calc_("9"))
        num0 = ttk.Button(self.col2, text="0", command=lambda: parent.output.calc_("0"))
        log = ttk.Button(self.col1, text="log()", command=lambda: parent.output.calc_("log"))
        decimal = ttk.Button(self.col3, text=".", command=lambda: parent.output.calc_("."))
        sqrt = ttk.Button(self.col3, text="√", command=lambda: parent.output.calc_("sqrt"))
        pow_calc = ttk.Button(self.col2, text="x²", command=lambda: parent.output.calc_("pow"))
        one_by = ttk.Button(self.col1, text="1/x", command=lambda: parent.output.calc_("1/"))

        add = ttk.Button(self.col4, text="+", command=lambda: parent.output.calc_("+"))
        sub = ttk.Button(self.col4, text="-", command=lambda: parent.output.calc_("-"))
        div = ttk.Button(self.col4, text=f"{chr(247)}", command=lambda: parent.output.calc_("/"))
        prod = ttk.Button(self.col4, text="x", command=lambda: parent.output.calc_("*"))
        equ = ttk.Button(self.col4, text="=", command=lambda: parent.output.calc_("="))
        clear = ttk.Button(self.col3, text="c", command=lambda: parent.output.calc_("c"))
        delete = ttk.Button(self.col4, text="⌫", command=lambda: parent.output.calc_("cl"))
        clear_history = ttk.Button(self.col2, text="CE", command=lambda: parent.output.calc_("ce"))
        percent = ttk.Button(self.col1, text="%", command=lambda: parent.output.calc_("%"))

        percent.pack(side="top", expand=True, fill="both")
        clear_history.pack(side="top", expand=True, fill="both")
        one_by.pack(side="top", expand=True, fill="both")
        num7.pack(side="top", expand=True, fill="both")
        num4.pack(side="top", expand=True, fill="both")
        num1.pack(side="top", expand=True, fill="both")

        pow_calc.pack(side="top", expand=True, fill="both")
        clear.pack(side="top", expand=True, fill="both")
        sqrt.pack(side="top", expand=True, fill="both")
        num8.pack(side="top", expand=True, fill="both")
        num5.pack(side="top", expand=True, fill="both")
        num2.pack(side="top", expand=True, fill="both")
        num0.pack(side="top", expand=True, fill="both")

        delete.pack(side="top", expand=True, fill="both")
        num9.pack(side="top", expand=True, fill="both")
        num6.pack(side="top", expand=True, fill="both")
        num3.pack(side="top", expand=True, fill="both")
        decimal.pack(side="top", expand=True, fill="both")
        log.pack(side="top", expand=True, fill="both")

        div.pack(side="top", expand=True, fill="both")
        prod.pack(side="top", expand=True, fill="both")
        sub.pack(side="top", expand=True, fill="both")
        add.pack(side="top", expand=True, fill="both")
        equ.pack(side="top", expand=True, fill="both")

class f_output(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.calc = tk.StringVar(value="")
        self.disp = ""
        self.place(relheight=0.2, relwidth=1)
        self.font_var = ("Arial", 29)
        self.output_label = ttk.Label(self, textvariable=self.calc, font=self.font_var)
        self.output_label.pack(expand = True,fill="y",anchor="se")
        parent.bind("<Key>", self.keypress)
        parent.bind("<BackSpace>", self.backspace)
        parent.bind("<Return>", self.enter)
        parent.bind("<Delete>", self.dele)
        parent.bind("<Shift-Delete>", self.history_del)
        self.his_menu = ttk.Menubutton(self, text="history")
        self.history_menu = ttk.Menu(self.his_menu)
        self.his_menu["menu"] = self.history_menu
        self.his_menu.place(anchor="nw")

        def text_size(event):
            if (len(self.calc.get())) >= 7:
                self.output_label.config(font=("Arial", int(self.winfo_height() / 1.75 / (len(self.calc.get()) * 0.15))))
                return
            self.output_label.config(font=("Arial", int(self.winfo_height() / 1.75)))
            return
        self.bind("<Configure>", text_size)

    def calc_(self, num):
        if num == "ce":
            self.calc.set("")
            self.his_update("ce")
            self.disp = ""
            return
        if num == "c":
            self.calc.set("")
            self.disp = ""
            return
        if num == "cl":
            self.calc.set(self.calc.get()[0:-1])
            self.disp = self.calc.get()
            return
        if num == "=":
            try:
                self.his_update(eval(self.disp),self.calc.get(),self.disp)
                self.calc.set(eval(self.disp))
            except:
                self.calc.set("Invalid Syntax")
            return
        if len(self.calc.get()) >= 20:
            return
        if num == "log":
            self.calc.set(f"log({self.calc.get()})")
            self.disp = f"(math.log({self.disp}))"
            return
        if num == "%":
            self.calc.set(f"{self.calc.get()}% x ")
            self.disp = f"({self.disp}/100)*"
            return
        if num == "1/":
            self.calc.set(f"1/{self.calc.get()}")
            self.disp = f"1/({self.disp})"
            return
        if num == "sqrt":
            self.calc.set(f"√{self.calc.get()}")
            self.disp = f"math.sqrt({self.disp})"
            return
        if num == "pow":
            self.calc.set(f"{self.calc.get()}²")
            self.disp = self.disp + "**2"
            return
        if self.disp == "" and num == "=":
            return
        if num == "/":
            self.calc.set(value=self.calc.get() + chr(247))
            self.disp += "/"
            return
        if num == "*":
            self.calc.set(value=self.calc.get() + "x")
            self.disp += "*"
            return
        self.disp += num
        self.calc.set(value=self.calc.get() + num)
        return

    def keypress(self,event):
        if event.char.isnumeric() or event.char in ["/", "*", "+", "-", "."]:
            self.calc_(event.char)
        return

    def backspace(self,event):
        self.calc_("cl")

    def enter(self,event):
        self.calc_("=")

    def dele(self,event):
        self.calc_("c")

    def history_del(self,event):
        self.calc_("ce")

    def his_update(self,char,equ=None,disp_equ=None):
        if char == "ce":
            self.history_menu.delete(0,'end')
            return
        self.history_menu.add_command(label=f"{equ}={char}",command=lambda :self.reset(equ,disp_equ))

    def reset(self,equ,disp_equ):
        self.calc.set(equ)
        self.disp = disp_equ

Calculator()