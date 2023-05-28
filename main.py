import tkinter as tk
import ttkbootstrap as ttk


vis_calc = ""

window = tk.Tk()
window.title("Calculator")
window.geometry("380x400")
window.minsize(380,400)
window.maxsize(380,400)

output_frame = ttk.Frame(window)
operator_frame = ttk.Frame(window)

calc = tk.StringVar(value = "")
disp = ""
def calc_(num):
    global disp
    if disp=="" and num=="=":
        return
    if num == "=":
        calc.set(eval(disp))
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
operator_nums = ttk.Frame(operator_frame)
operator_funcs = ttk.Frame(operator_frame)


num1 = ttk.Button(operator_nums,text="1",command=lambda :calc_("1"))
num2 = ttk.Button(operator_nums,text="2",command=lambda :calc_("2"))
num3 = ttk.Button(operator_nums,text="3",command=lambda :calc_("3"))
num4 = ttk.Button(operator_nums,text="4",command=lambda :calc_("4"))
num5 = ttk.Button(operator_nums,text="5",command=lambda :calc_("5"))
num6 = ttk.Button(operator_nums,text="6",command=lambda :calc_("6"))
num7 = ttk.Button(operator_nums,text="7",command=lambda :calc_("7"))
num8 = ttk.Button(operator_nums,text="8",command=lambda :calc_("8"))
num9 = ttk.Button(operator_nums,text="9",command=lambda :calc_("9"))
num0 = ttk.Button(operator_nums,text="0",command=lambda :calc_("0"))

add = ttk.Button(operator_funcs,text="+",command=lambda :calc_("+"))
sub = ttk.Button(operator_funcs,text="-",command=lambda :calc_("-"))
div = ttk.Button(operator_funcs,text=f"{chr(247)}",command=lambda :calc_("/"))
prod = ttk.Button(operator_funcs,text="x",command=lambda :calc_("*"))
equ = ttk.Button(operator_funcs,text="=",command=lambda :calc_("="))


output_frame.place(relheight=0.2,relwidth=1)
output_label.pack(expand = True,fill="y",anchor="se")

operator_frame.place(rely=0.2,relheight=1,relwidth=1)

operator_nums.place(relwidth=0.75,relheight=0.914)
operator_funcs.place(relx=0.75,relwidth=0.25,relheight=0.799)

operator_nums.columnconfigure(0,weight=1)
operator_nums.columnconfigure(1,weight=1)
operator_nums.columnconfigure(2,weight=1)


operator_nums.rowconfigure(0,weight=1)
operator_nums.rowconfigure(1,weight=1)
operator_nums.rowconfigure(2,weight=1)
operator_nums.rowconfigure(3,weight=1)
operator_nums.rowconfigure(4,weight=1)



num1.grid(row=0,column=0,sticky="nsew")
num2.grid(row=0,column=1,sticky="nsew")
num3.grid(row=0,column=2,sticky="nsew")
num4.grid(row=1,column=0,sticky="nsew")
num5.grid(row=1,column=1,sticky="nsew")
num6.grid(row=1,column=2,sticky="nsew")
num7.grid(row=2,column=0,sticky="nsew")
num8.grid(row=2,column=1,sticky="nsew")
num9.grid(row=2,column=2,sticky="nsew")
num0.grid(row=3,column=1,sticky="nsew")

add.pack(side="top",expand=True,fill="both")
sub.pack(side="top",expand=True,fill="both")
prod.pack(side="top",expand=True,fill="both")
div.pack(side="top",expand=True,fill="both")
equ.pack(side="top",expand=True,fill="both")



window.mainloop()