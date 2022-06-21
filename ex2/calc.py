from gettext import bind_textdomain_codeset
import tkinter as tk
from  tkinter import messagebox as tkm

calc=tk.Tk()
calc.title("電卓")
calc.geometry("500x450") 
fonts=("Times New Roman",30)
fonts2=("Times New Roman",40)

num_list=[[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,1],[3,2],[4,1]]
count=9

def equal(event):#四則演算
    entry_value=entry.get()
    entry.delete(0,tk.END)
    ans=eval(entry_value)
    entry.insert(tk.END,ans)

def button_click(event):#ボタンが押されたときにどのような処理をするかを区別する関数
    btn=entry
    info = event.widget
    count=0
    entry.insert(tk.END,info["text"])

def button_click_C(event):
    entry.delete(0,tk.END)

def dog_age(event):
    btn=entry.get()
    entry.delete(0,tk.END)
    info =int(btn)
    info=(info-31)/16
    if info<0:
        info="生前"
    entry.insert(tk.END,info)
    
def button_click_1C(event):
    btn=entry.get()
    entry.delete(len(btn)-1)

def button_silyouhi(event):
    btn=entry.get()
    entry.delete(0,tk.END)
    info=int(btn)
    info=1.1*info
    info=round(info)
    entry.insert(tk.END,info)


calc.entry_text=tk.StringVar#文字を入力するところ作成
entry=tk.Entry(width=10,justify="right",font=fonts2)
entry.grid(row=0,column=0,columnspan=3,padx=0,pady=0,ipadx=20,ipady=30)

button=tk.Button(calc,text="+",font=fonts,width=4,height=1)#＋ボタン作成
button.grid(row=2,column=3)
button.bind("<1>",button_click)

utton=tk.Button(calc,text="-",font=fonts,width=4,height=1)#-ボタン作成
utton.grid(row=3,column=3)
utton.bind("<1>",button_click)

button=tk.Button(calc,text="=",font=fonts,width=4,height=1)#=ボタン作成
button.grid(row=4,column=0)
button.bind("<1>",equal)

button=tk.Button(calc,text="C",font=fonts,width=4,height=1)#Cボタン作成
button.grid(row=4,column=2)
button.bind("<1>",button_click_C)

button=tk.Button(calc,text="*",font=fonts,width=4,height=1)#*ボタン作成
button.grid(row=2,column=4)
button.bind("<1>",button_click)

button=tk.Button(calc,text="/",font=fonts,width=4,height=1)#÷ボタン作成
button.grid(row=3,column=4)
button.bind("<1>",button_click)

button=tk.Button(calc,text="犬",font=fonts,width=4,height=1)#犬から人間ボタン作成
button.grid(row=1,column=4)
button.bind("<1>",dog_age)

button=tk.Button(calc,text="(×)",font=fonts,width=4,height=1)#一文字削除ボタン作成
button.grid(row=4,column=3)
button.bind("<1>",button_click_1C)

button=tk.Button(calc,text="税",font=fonts,width=4,height=1)#一文字削除ボタン作成
button.grid(row=1,column=3)
button.bind("<1>",button_silyouhi)


for i in num_list:  #数字ボタン作成
    button=tk.Button(calc,text=count,font=fonts,width=4,height=1)
    button.bind("<1>",button_click)
    button.grid(row=i[0],column=i[1])
    count-=1

calc.mainloop()
