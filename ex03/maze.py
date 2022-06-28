import tkinter as tk
import maze_maker
from random import randint

#グローバル変数を設定
key=""
cx,cy=150,150
mx,my=1,1



def key_down(event): #キーが押されたときの関数
    global key
    key = event.keysym
    

def key_up(event): #キーが離されたときの関数
    global key
    key=""

def main_proc(): #こうかとんを移動をおこなう関数
    global cx, cy ,key,tori,mx,my
    if key=="Up" and stage_list[mx-1][my]==0:#キーの上矢印が押されたときの移動処理
        cy-=100
        mx-=1
    elif key=="Down" and stage_list[mx+1][my]==0:#キーの下矢印が押されたときの移動処理
        cy+=100
        mx+=1
    elif key=="Right" and stage_list[mx][my+1]==0:#キーの右矢印が押されたときの移動処理
        cx+=100
        my+=1
    elif key=="Left" and stage_list[mx][my-1]==0:#キーの左矢印が押されたときの移動処理
        cx-=100
        my-=1
    


    canvas.after(100,main_proc)
    canvas.coords("tori",cx,cy)

def koukaton():#こうかとんの画像を表示する関数
    global tori , cx , cy
    tori_list=["ex03/fig/0.png","ex03/fig/1.png","ex03/fig/2.png","ex03/fig/3.png","ex03/fig/4.png","ex03/fig/5.png","ex03/fig/6.png","ex03/fig/7.png","ex03/fig/8.png","ex03/fig/9.png"]
    gazou=tori_list[randint(0,9)]
    tori=tk.PhotoImage(file=gazou)
    canvas.create_image(cx,cy,image=tori,tag="tori")


#タイマーを作成関数
def count_up():
    global tmr,cx,cy
    tmr = tmr-1
    label["text"]=tmr
    maze.after(1000,count_up)
    if tmr<1:
        rstart()
        tmr=10

#リスタートする関数
def rstart():
    global tmr,cx,cy,mx,my
    if tmr ==0:
        cx,cy,mx,my=150,150,1,1


#ゴール,スタート設定
def finish():
    global tate,yoko
    while True:
        yoko=randint(0,8)
        tate=randint(0,14)
        if stage_list[yoko][tate]==0:
            break
    canvas.create_rectangle(100,100,200,200,fill="Red")
    canvas.create_rectangle(tate*100,yoko*100,(tate*100)+100,(yoko*100)+100,fill="blue")



if __name__ == "__main__":

    maze=tk.Tk()#ウィンドウを作成
    maze.title("迷えるこうかとん")#ウィンドウのタイトルを設定
    maze.geometry("1500x900")#1500×900のウィンドウを設定


    canvas=tk.Canvas(maze,width=1500,height=900,bg="black")#迷路の大きさを1500×900でバックグラウンドを黒にして作成
    canvas.place(x=0,y=0)#ウィンドウの初期位置を設定
    maze.bind("<KeyPress>",key_down)#キーが押されたときの動作の紐づけ
    maze.bind("<KeyRelease>",key_up)#キーが離されたときの動作紐づけ
    maze.after(100,main_proc)#リアルタイム処理
    stage_list=maze_maker.make_maze(15,9)#迷路の道と壁を判定するリストをstage_listに代入
    maze_maker.show_maze(canvas,stage_list)#迷路を表示
   
    #タイマー
    label=tk.Label(maze,font=("Times New Roman",80))
    label.pack()
    tmr=10
    maze.after(1000,count_up)

    finish()
    koukaton()#こうかとんを表示



    maze.mainloop()#処理をループさせる


