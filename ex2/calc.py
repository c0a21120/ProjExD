import tkinter as tk
from  tkinter import messagebox as tkm

calc=tk.Tk()
calc.title("電卓")
calc.geometry("400x404") 
fonts=("Times New Roman",30)
fonts2=("Times New Roman",40)

num_list=[[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,1],[3,2],[4,1]]
count=9


def button_click(event):
    btn=entry
    #btn = event.widget
    #txt = btn["text"]
    info = event.widget.grid_info()
    #print(info['row'],info['column'])
    if info['row']==1 and info['column']==0:
        btn.insert(tk.END,9)
    elif info['row']==1 and info['column']==1:
        btn.insert(tk.END,8)
    elif info['row']==1 and info['column']==2:
        btn.insert(tk.END,7)
    elif info['row']==2 and info['column']==0:
        btn.insert(tk.END,6)
    elif info['row']==2 and info['column']==1:
        btn.insert(tk.END,5)
    elif info['row']==2 and info['column']==2:
        btn.insert(tk.END,4)
    elif info['row']==3 and info['column']==0:
        btn.insert(tk.END,3)
    elif info['row']==3 and info['column']==1:
        btn.insert(tk.END,2)
    elif info['row']==3 and info['column']==2:
        btn.insert(tk.END,1)
    elif info['row']==4 and info['column']==1:
        btn.insert(tk.END,0)
    elif info['row']==2 and info['column']==3:
        btn.insert(tk.END,"+")
    elif info['row']==4 and info['column']==3:
        btn.insert(tk.END,"=")
    elif info['row']==3 and info['column']==3:
        btn.insert(tk.END,"-")

    #btn.insert(tk.END,count)
    #tkm.showinfo(txt,f"[{txt}]ボタンが押されました")


calc.entry_text=tk.StringVar#文字を入力するところ作成
entry=tk.Entry(width=40,justify=tk.CENTER,textvariable=calc.entry_text)
entry.grid(row=0,column=0,columnspan=3,padx=0,pady=0,ipadx=20,ipady=30)

button=tk.Button(calc,text="+",font=fonts,width=4,height=1)#＋ボタン作成
button.grid(row=2,column=3)
button.bind("<1>",button_click)

utton=tk.Button(calc,text="-",font=fonts,width=4,height=1)#-ボタン作成
utton.grid(row=3,column=3)
utton.bind("<1>",button_click)

button=tk.Button(calc,text="=",font=fonts,width=4,height=1)#=ボタン作成
button.grid(row=4,column=3)
button.bind("<1>",button_click)




for i in num_list:
    button=tk.Button(calc,text=count,font=fonts,width=4,height=1)
    button.grid(row=i[0],column=i[1])
    print(count)
    button.bind("<1>",button_click)
    count-=1

calc.mainloop()
