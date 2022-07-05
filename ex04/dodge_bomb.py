from turtle import width
import pygame as pg
import sys
from random import randint

def main():
    global screen,bom_x,bom_y,vx,vy
    vx=10
    vy=10
    pg.init()
    pg.display.set_caption("逃げろ！こうかとん")#タイトルバー
    screen=pg.display.set_mode((1600,900))#1600＊900の画面surfaceを生成

#こうかとん作成
    tori=pg.image.load("ex04/fig/9.png").convert_alpha()
    tori=pg.transform.rotozoom(tori,0,2.0)
    rect_tori=tori.get_rect()
    rect_tori.center=(900,400)

#爆弾作成
    bom_x=randint(0,1600)
    bom_y=randint(0,900)
    


#背景作成
    bg=pg.image.load("ex04/fig/pg_bg.png").convert_alpha()
    rect_bg=bg.get_rect()


    while (1):
        pg.display.update()#画面更新
        clock = pg.time.Clock()
        clock.tick(1000)

        

#こうかとんを矢印キーで動かす
        pressed_key=pg.key.get_pressed()
        if pressed_key[pg.K_LEFT]:#左キーが押されたとき
            rect_tori.move_ip(-1,0)



        if pressed_key[pg.K_RIGHT]:#右キーが押されたとき
            rect_tori.move_ip(1,0)
        if pressed_key[pg.K_UP]:#上キーが押されたとき
            rect_tori.move_ip(0,-1)
        if pressed_key[pg.K_DOWN]:#下キーが押されたとき
            rect_tori.move_ip(0,1)

        screen.blit(bg,(0,0))#背景を表示
        screen.blit(tori,rect_tori)#toriを表示
        bom=pg.draw.circle(screen,(255,0,0),(bom_x,bom_y),10)#爆弾表示
        if bom_x>10 and 1590>bom_x:
            bom_x+=vx
        else:
            vx*=-1
            bom_x+=vx
            print("a")

        if bom_y>10 and 890>bom_y:
            bom_y+=vy
        else:
            vy*=-1
            bom_y+=vy

            print("A")





#キーを押したとき
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_x:#Xキーが押されたとき
                    return
        
if __name__ == "__main__":
    main()
