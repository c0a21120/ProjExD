import tkinter as tk
import maze_maker

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
    tori=tk.PhotoImage(file="ex03/fig/5.png")
    canvas.create_image(cx,cy,image=tori,tag="tori")


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
   
    koukaton()#こうかとんを表示
    maze.mainloop()#処理をループさせる

