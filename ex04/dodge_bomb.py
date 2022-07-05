
import pygame as pg
import sys
import random

def main():
    global screen,bom_x,bom_y,vx,vy,tori_x,tori_y
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
    rect_tori.center=(tori_x,tori_y)

#爆弾作成
    bming_sfc=pg.Surface((20,20))
    bming_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bming_sfc,(255,0,0),(10,10),10)
    bming_rect=bming_sfc.get_rect()
    bming_rect.centerx=random.randint(0,sc_rect.width)
    bming_rect.centery=random.randint(0,sc_rect.height)



#背景作成
    bg=pg.image.load("ex04/fig/pg_bg.png").convert_alpha()
    rect_bg=bg.get_rect()
    vx, vy = +1, +1

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
        screen.blit(bg,(0,0))#背景を表示
        screen.blit(tori,rect_tori)#toriを表示
        screen.blit(bming_sfc,bming_rect)#爆弾表示
    #爆弾の処理
        yoko,tate=check_bound(bming_rect,sc_rect)
        vx*=yoko
        vy*=tate

        




        if rect_tori.colliderect(bming_rect):
            return





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



if __name__ == "__main__":
    main()
