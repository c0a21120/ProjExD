import tkinter as tk
from  tkinter import messagebox as tkm

calc=tk.Tk()
calc.title("電卓")
calc.geometry("300x500") 
fonts=("Times New Roman",30)
num_list=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,1]]
count=9

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押されました")


for i in num_list:
    button=tk.Button(calc,text=count,font=fonts,width=4,height=2)
    button.grid(row=i[0],column=i[1])
    count-=1
    button.bind("<1>",button_click)
calc.mainloop()
