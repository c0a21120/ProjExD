
from turtle import update
import pygame as pg
import sys
import random
import tkinter as tk
a="ex04/fig/pg_bg.png"
def main():
    global screen,bom_x,bom_y,vx,vy,tori_x,tori_y,a
    vx=+1
    vy=+1
    tori_x=900
    tori_y=400
    pg.init()
    pg.display.set_caption("逃げろ！こうかとん")#タイトルバー
    screen=pg.display.set_mode((1600,900))#1600＊900の画面surfaceを生成
    sc_rect=screen.get_rect()

#こうかとん作成
    tori=pg.image.load("ex04/fig/9.png").convert_alpha()
    tori=pg.transform.rotozoom(tori,0,2.0)
    rect_tori=tori.get_rect()

    tori_x=random.randint(0,1600)#こうかとんの初期座標設定
    tori_y=random.randint(0,900)

    rect_tori.center=(tori_x,tori_y)

#爆弾作成
    bming_sfc=pg.Surface((20,20))
    bming_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bming_sfc,(255,0,0),(10,10),10)
    bming_rect=bming_sfc.get_rect()
    bming_rect.centerx=random.randint(0,sc_rect.width)
    bming_rect.centery=random.randint(0,sc_rect.height)



#背景作成
    bg=pg.image.load(a).convert_alpha()
    rect_bg=bg.get_rect()
    vx, vy = +1, +1
    vx2,vy2=+1,+1

     #爆弾二個目
    bming2_sfc=pg.Surface((20,20))
    bming2_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bming2_sfc,(0,255,0),(10,10),100)
    bming2_rect=bming2_sfc.get_rect()
    bming2_rect.centerx=random.randint(0,sc_rect.width)
    bming2_rect.centery=random.randint(0,sc_rect.height)

    while (1):
        bg=pg.image.load(a).convert_alpha()
        rect_bg=bg.get_rect()
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

        if check_bound(rect_tori,sc_rect) != (1,1):#領域外だったら
            if pressed_key[pg.K_LEFT]:#左キーが押されたとき
                rect_tori.move_ip(1,0)
            if pressed_key[pg.K_RIGHT]:#右キーが押されたと
                rect_tori.move_ip(-1,0)
            if pressed_key[pg.K_UP]:#上キーが押されたとき
                rect_tori.move_ip(0,1)
            if pressed_key[pg.K_DOWN]:#下キーが押されたとき
                rect_tori.move_ip(0,-1)


        # vx, vy = +1, +1
        bming_rect.move_ip(vx,vy)
        bming2_rect.move_ip(vx2,vy2)
        screen.blit(bg,(0,0))#背景を表示
        screen.blit(tori,rect_tori)#toriを表示
        screen.blit(bming_sfc,bming_rect)#爆弾表示
        screen.blit(bming2_sfc,bming2_rect)#爆弾2表示
        
    #爆弾の処理
        yoko,tate=check_bound(bming_rect,sc_rect)
        vx*=yoko
        vy*=tate

        yoko,tate=check_bound(bming2_rect,sc_rect)
        vx2*=yoko
        vy2*=tate
        if rect_tori.colliderect(bming_rect):
            a1,a2=game_over()
            screen.blit(a2,a1)

            #pg.display.update()#画面更新
            return

#爆弾２の処理
        if rect_tori.colliderect(bming_rect):
            screen.blit
            #game_over()
            #pg.display.update()#画面更新
            return  


        yoko,tate=check_bound(bming2_rect,sc_rect)
        vx*=yoko
        vy*=tate
    
    





            





#キーを押したとき
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_x:#Xキーが押されたとき
                    return
        

def check_bound(rct,sc_rect):
    """
[1]rct:こうかとん or 爆弾のrect
[2]screen:スクリーンのRect
    """
    yoko , tate = +1 , +1#領域内
    if rct.left <sc_rect.left or sc_rect.right < rct.right: yoko = -1 #領域外
    if rct.top  <sc_rect.top or sc_rect.bottom < rct.bottom: tate=- 1 #領域外
    return yoko ,tate

def game_over():
    global a
    a="ex04/fig/game over.png"
    game_over=pg.image.load(a).convert_alpha()
    rect_go=game_over.get_rect()
    return rect_go,game_over




if __name__ == "__main__":
    main()
