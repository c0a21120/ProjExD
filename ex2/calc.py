import tkinter as tk


calc=tk.Tk()
calc.title("電卓")
calc.geometry("300x500") 
fonts=("Times New Roman",30)
num_list=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,1]]
count=9
for i in num_list:
    button=tk.Button(calc,text=count,font=fonts,width=4,height=2)
    button.grid(row=i[0],column=i[1])
    count-=1
calc.mainloop()
