import tkinter as tk
from tkinter import messagebox
def calculate():
    #perform calculation based on user input
    try:
        num1=float(entry_num1.get())
        num2=float(entry_num2.get())
        operation=operation_var.get()
        if operation=="+":
            result=num1+num2
        elif operation=="-":
            result=num1-num2
        elif operation=="*":
            result=num1*num2
        elif operation=="/":
            if num2==0:
                messagebox.showerror("Error","Division by zero!")
                return
            result=num1%num2
        elif operation=="^":
            result=num1**num2
        else:
            messagebox.showerror("Error","Please select an operation")
            return
        result_label.config(text=f"Result:{result}")
    except ValurError:
        messagebox.shoewrror("Error","please enter valid numbers!")
#create main window 
root=tk.TK()
root.title("Simple Calculator")
root.geometry("300*300")
root.resizable(False,False)

#create input fields
tk.Label(root,text="First Number:").pack(pady=5)
entry_num1=tk.Entry(root)
entry_num1.pack(pady=5)

tk.Label(root,text="Second Number":).pack(pady=5)
entry_num2=tk.Entry(root)
entry_num2.pack(pady=5)

#Operation selection
tk.Label(root,text="Select Operation:").pack(pady=5)
operations=["+","-","*","/","%","^"]
operation_var=tk.StringVar(value="+")
frame=tk.Frame(root)
frame.pack(pady=5)
for op in operations:
    tk.Radibutton(frame,text=op,variable=operation_var,value=op).pack(side=tk.LEFT,padx=2)
#calculate button
tk.Button(root,text="Calculate",command=calculate,bg="blue,fg="white).pack(pady=10)
#Resule label
result_label=tk.Label(root,tex"Result:",font=("arial",12,"bold"))
result_label.pack(pady=10)
#Run the application
root.mainloop()

