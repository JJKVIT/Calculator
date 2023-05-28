import tkinter as tk
import ttkbootstrap as ttk

calc = ""
vis_calc = ""

window = tk.Tk()
window.title("Calculator")
window.geometry("380x400")
window.minsize(380,400)
window.maxsize(380,400)

output_frame = ttk.Frame(window)
operator_frame = ttk.Frame(window)

output_label = ttk.Label(output_frame,background="red")
operator_nums = ttk.Frame(operator_frame)
operator_funcs = ttk.Frame(operator_frame)

num_row1 = ttk.Frame(operator_nums)
num_row2 = ttk.Frame(operator_nums)
num_row3 = ttk.Frame(operator_nums)

num1 = ttk.Button(num_row1,text="1")
num2 = ttk.Button(num_row2,text="2")
num3 = ttk.Button(num_row3,text="3")
num4 = ttk.Button(num_row1,text="4")
num5 = ttk.Button(num_row2,text="5")
num6 = ttk.Button(num_row3,text="6")
num7 = ttk.Button(num_row1,text="7")
num8 = ttk.Button(num_row2,text="8")
num9 = ttk.Button(num_row3,text="9")
num0 = ttk.Button(num_row2,text="0")

add = ttk.Button(operator_funcs)
sub = ttk.Button(operator_funcs)
div = ttk.Button(operator_funcs)
prod = ttk.Button(operator_funcs)


output_frame.place(relheight=0.2,relwidth=1)
output_label.pack(expand=True,fill="both")

operator_frame.place(rely=0.2,relheight=1,relwidth=1)

operator_nums.place(relwidth=0.75,relheight=1)
operator_funcs.place(relx=0.75,relwidth=1,relheight=1)

num_row1.pack(side="left",expand=True,fill="both")
num_row2.pack(side="left",expand=True,fill="both")
num_row3.pack(side="left",expand=True,fill="both")




window.mainloop()