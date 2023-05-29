import tkinter as tk
import ttkbootstrap as ttk
import math

window = tk.Tk()
window.iconbitmap("images.ico")
window.title("Calculator")
window.geometry("380x400")
window.minsize(380,400)
window.maxsize(380,400)

output_frame = ttk.Frame(window)
operator_frame = ttk.Frame(window)

calc = tk.StringVar(value = "")
disp = ""
history = []
def calc_(num):
    global disp,history
    if num == "log":
        calc.set(f"log({calc.get()})")
        disp = f"(math.log({disp}))"
        return
    if num == "%":
        calc.set(f"{calc.get()}% x ")
        disp = f"({disp}/100)*"
        return
    if num == "1/":
        calc.set(f"1/{calc.get()}")
        disp = f"1/({disp})"
        return
    if num == "sqrt":
        calc.set(f"√{calc.get()}")
        disp = f"math.sqrt({disp})"
        return
    if num=="pow":
        calc.set(f"{calc.get()}²")
        disp = disp+"**2"
        return
    if num=="ce":
        print(history)
        history=[]
        calc.set("")
        return
    if num == "c":
        calc.set("")
        disp = ""
        return
    if num == "cl":
        calc.set(calc.get()[0:-1])
        disp = calc.get()
        return
    if disp=="" and num=="=":
        return
    if num == "=":
        try:
            calc.set(eval(disp))
            history.append([disp,eval(disp)])
        except:
            calc.set("Invalid Syntax")
        return
    disp += num
    if num=="/":
        calc.set(value=calc.get()+chr(247))
        return
    if num=="*":
        calc.set(value=calc.get()+"x")
        return
    calc.set(value = calc.get()+num)
    return

output_label = ttk.Label(output_frame,textvariable=calc,font=("Arial",25))

col1 = ttk.Frame(operator_frame)
col2 = ttk.Frame(operator_frame)
col3 = ttk.Frame(operator_frame)
col4 = ttk.Frame(operator_frame)

num1 = ttk.Button(col1,text="1",command=lambda :calc_("1"))
num2 = ttk.Button(col2,text="2",command=lambda :calc_("2"))
num3 = ttk.Button(col3,text="3",command=lambda :calc_("3"))
num4 = ttk.Button(col1,text="4",command=lambda :calc_("4"))
num5 = ttk.Button(col2,text="5",command=lambda :calc_("5"))
num6 = ttk.Button(col3,text="6",command=lambda :calc_("6"))
num7 = ttk.Button(col1,text="7",command=lambda :calc_("7"))
num8 = ttk.Button(col2,text="8",command=lambda :calc_("8"))
num9 = ttk.Button(col3,text="9",command=lambda :calc_("9"))
num0 = ttk.Button(col2,text="0",command=lambda :calc_("0"))
log = ttk.Button(col1,text="log()",command=lambda :calc_("log"))
decimal = ttk.Button(col3,text=".",command=lambda :calc_("."))
sqrt = ttk.Button(col3,text="√",command=lambda :calc_("sqrt"))
pow = ttk.Button(col2,text="x²",command=lambda :calc_("pow"))
one_by = ttk.Button(col1,text="1/x",command=lambda :calc_("1/"))

add = ttk.Button(col4,text="+",command=lambda :calc_("+"))
sub = ttk.Button(col4,text="-",command=lambda :calc_("-"))
div = ttk.Button(col4,text=f"{chr(247)}",command=lambda :calc_("/"))
prod = ttk.Button(col4,text="x",command=lambda :calc_("*"))
equ = ttk.Button(col4,text="=",command=lambda :calc_("="))
clear = ttk.Button(col3,text="c",command=lambda :calc_("c"))
delete = ttk.Button(col4,text="⌫",command=lambda :calc_("cl"))
clear_history = ttk.Button(col2,text="CE",command=lambda :calc_("ce"))
percent = ttk.Button(col1,text="%",command=lambda :calc_("%"))

output_frame.place(relheight=0.2,relwidth=1)
output_label.pack(expand = True,fill="y",anchor="se")

operator_frame.place(rely=0.2,relheight=0.8,relwidth=1)

col1.pack(side="left",expand=True,fill="both")
col2.pack(side="left",expand=True,fill="both")
col3.pack(side="left",expand=True,fill="both")
col4.pack(side="left",expand=True,fill="both")

percent.pack(side="top",expand=True,fill="both")
clear_history.pack(side="top",expand=True,fill="both")
one_by.pack(side="top",expand=True,fill="both")
num7.pack(side="top",expand=True,fill="both")
num4.pack(side="top",expand=True,fill="both")
num1.pack(side="top",expand=True,fill="both")
log.pack(side="top",expand=True,fill="both")

pow.pack(side="top",expand=True,fill="both")
clear.pack(side="top",expand=True,fill="both")
sqrt.pack(side="top",expand=True,fill="both")
num8.pack(side="top",expand=True,fill="both")
num5.pack(side="top",expand=True,fill="both")
num2.pack(side="top",expand=True,fill="both")
num0.pack(side="top",expand=True,fill="both")

delete.pack(side="top",expand=True,fill="both")
num9.pack(side="top",expand=True,fill="both")
num6.pack(side="top",expand=True,fill="both")
num3.pack(side="top",expand=True,fill="both")
decimal.pack(side="top",expand=True,fill="both")

div.pack(side="top",expand=True,fill="both")
prod.pack(side="top",expand=True,fill="both")
sub.pack(side="top",expand=True,fill="both")
add.pack(side="top",expand=True,fill="both")
equ.pack(side="top",expand=True,fill="both")

window.mainloop()