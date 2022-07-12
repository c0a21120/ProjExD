from logging import root
import pygame as pg
import sys
import random
import pygame.mixer
import time
import tkinter as tk

#screenクラスを作成
class Screen:
    def __init__(self,title,wh,image):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode((wh))      # Surface
        self.rct = self.sfc.get_rect()            # Rect
        self.bgi_sfc = pg.image.load(image)       # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()    # Rext
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


#Birdクラスを作成

class Bird:
    def __init__(self,image: str,size: float,xy):
        self.sfc = pg.image.load(image)                     # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0,size)  # Surface
        self.rct = self.sfc.get_rect()                      # Rect
        self.rct.center = xy

    def blit(self,scr: Screen):
        #screen_sfc.blit(kkimg_sfc, kkimg_rct)
        scr.sfc.blit(self.sfc,self.rct)

    def update(self, scr: Screen):#こうかとんの移動の処理
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]:
            self.rct.centery -=1 
        if key_states[pg.K_DOWN]:
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 1
# 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外
            if key_states[pg.K_UP]:
                self.rct.sentery +=1 
            if key_states[pg.K_DOWN]:
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 1
        self.blit(scr)
#screen_sfc.blit(kkimg_sfc, kkimg_rct)

    def attack(self):
        return Shot(self)


#Bombクラスの作成
class Bomb:
    def __init__(self,color,size,vxy,scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (size,size), size)
        self.rct=self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self,scr: Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr: Screen):
         # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        # 練習5
        scr.sfc.blit(self.sfc,self.rct)
        self.blit(scr)
    
#こうかとんからでるビームクラス
class Shot:
    def __init__(self, chr: Bird):
        self.sfc = pg.image.load("ex05/fig/beam.png")
        self.sfc= pg.transform.rotozoom(self.sfc,0,0.5)
        self.rct = self.sfc.get_rect()                      # Rect
        self.rct.midleft = chr.rct.center

    def blit(self,scr: Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr: Screen):
        self.rct.move_ip(+1,0)
        if check_bound(self.rct,scr.rct) != (1,1):
            del self
        self.blit(scr)


#敵を呼び出すクラス
class Anamy:
    def __init__(self,size,image,vxy,scr: Screen):

        self.sfc = pg.image.load(image)                   
        self.sfc = pg.transform.rotozoom(self.sfc, 0,size)
        self.rct = self.sfc.get_rect()                   
        self.rct=self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self,scr: Screen):
        scr.sfc.blit(self.sfc,self.rct)
    
    def update(self,scr: Screen):#移動を制御
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        #scr.sfc.blit(self.sfc,self.rct)
        self.blit(scr)

#   音楽を流す関数
def ongaku():
    pg.mixer.init()
    pg.mixer.music.load("ex05/fig/魔王魂 旧ゲーム音楽 戦闘曲メドレー01.mp3")#音楽を読み込む
    pg.mixer.music.play(-1)#無限ループさせる
        
def main():



    clock = pg.time.Clock()

    scr=Screen("負けるな！こうかとん",(1600,900),"ex05/fig/pg_bg.png")#タイトルと大きさと読み込むファイルを設定
    kkt = Bird("ex05/fig/9.png",2.0,(900,400))#birdクラスのインスタンスを生成
    bkd = Bomb((255,0,0),10,(+1,+1),scr)#爆弾を生成
    ane = Anamy(0.5,"ex05/fig/スライム.png",(5,5),scr)#敵を生成
    
    beams = []
    bombs = []

    ongaku()#音楽関数
    while True:
        #ongaku()
        #screen_sfc.blit(bgimg_sfc, bgimg_rct)
        scr.blit()

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return

            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                beams.append(kkt.attack())

        kkt.update(scr)
        ane.update(scr)

#こうかとんからでるビームの処理
        for bkd in bombs:
            bkd.updete(scr)
            if kkt.rct.colliderect(bkd.rct):
                return



        bkd.update(scr)
        if len(beams) !=0:
            beams.update(scr)
            for b,bkb in enumerate(bombs):
                if bombs[b].rct.collidererct(beams.rct):
                    del bombs[b]

        # 練習8
        #if kkimg_rct.colliderect(bmimg_rct): return 
        if kkt.rct.colliderect(bkd.rct):
            return

        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()