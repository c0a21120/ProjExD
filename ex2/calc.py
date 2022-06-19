import tkinter as tk
from  tkinter import messagebox as tkm

calc=tk.Tk()
calc.title("電卓")
calc.geometry("300x425") 
fonts=("Times New Roman",30)
fonts2=("Times New Roman",40)

num_list=[[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,1],[3,2],[4,1]]
count=9

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押されました")


calc.entry_text=tk.StringVar
entry=tk.Entry(width=40,justify=tk.CENTER,textvariable=calc.entry_text)
entry.grid(row=0,column=0,columnspan=3,padx=0,pady=0,ipadx=20,ipady=30)


for i in num_list:
    button=tk.Button(calc,text=count,font=fonts,width=4,height=1)
    button.grid(row=i[0],column=i[1])
    count-=1
    button.bind("<1>",button_click)
calc.mainloop()
