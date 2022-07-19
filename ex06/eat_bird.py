
import pygame as pg
import random
import sys


class Screen:
    def __init__(self,title,wh,image):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode((wh))      # Surface
        self.rct = self.sfc.get_rect()            # Rect
        self.bgi_sfc = pg.image.load(image)       # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()    # Rext
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)
class Bird:
    def __init__(self,image: str,size: float,xy):
        self.sfc = pg.image.load(image)                     # Surface
        
        self.sfc = pg.transform.rotozoom(self.sfc, 0,size)  # Surface
        #self.disp=pg.display.set_mode((self.width,self.height))
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
                self.rct.centery +=1 
            if key_states[pg.K_DOWN]:
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 1
        self.blit(scr)


class yakitori:
    def __init__(self,size,image,vxy,scr: Screen):
        self.sfc = pg.image.load(image)                   
        self.sfc = pg.transform.rotozoom(self.sfc, 0,size)
        self.rct = self.sfc.get_rect()                   
        self.rct=self.sfc.get_rect() # Rect
        self.rct.centerx = 1700
        self.rct.centery = random.randint(0,900)
        self.vx, self.vy = vxy # 練習6


    def blit(self,scr: Screen):
        scr.sfc.blit(self.sfc,self.rct)
    
    def update(self,scr: Screen):#移動を制御
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.blit(scr)



class teki:#上から降ってくる敵クラス
    def __init__(self,size,image,vxy,scr: Screen):
        self.sfc = pg.image.load(image)                   
        self.sfc = pg.transform.rotozoom(self.sfc, 0,size)
        self.rct = self.sfc.get_rect()                   
        self.rct=self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0,1600)
        self.rct.centery = 1000
        self.vx, self.vy = vxy # 練習6


    def blit(self,scr: Screen):
        scr.sfc.blit(self.sfc,self.rct)
    
    def update(self,scr: Screen):#移動を制御
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.blit(scr)


#   音楽を流す関数
def ongaku():
    pg.mixer.init()
    pg.mixer.music.load("ex06/fig/魔王魂 旧ゲーム音楽 戦闘曲メドレー01.mp3")#音楽を読み込む  famipop3.mp3  魔王魂 旧ゲーム音楽 戦闘曲
    pg.mixer.music.play(-1)#無限ループさせる
        




def main():

    font=pg.font.Font(None,55)
    score=0
    
    ysp=random.randint(1,4)
    ysp1=random.randint(1,4)
    ysp2=random.randint(1,4)


    clock = pg.time.Clock()

    scr=Screen("獲得ゲーム",(1600,900),"ex06/fig/pg_bg.png")

    kkt = Bird("ex05/fig/9.png",2.0,(900,400))#birdクラスのインスタンスを
    ane = yakitori(0.3,"ex06/fig/やきとり.png",(-ysp,0),scr)#やきとりを生成
    ane1 = yakitori(0.3,"ex06/fig/やきとり.png",(-ysp1,0),scr)#やきとりを生成
    ane2 = yakitori(0.3,"ex06/fig/やきとり.png",(-ysp2,0),scr)#やきとりを生成

    anemy = teki(0.3,"ex06/fig/ニート.png",(0,ysp),scr)#敵を生成
    anemy1 = teki(0.3,"ex06/fig/ニート.png",(0,ysp1),scr)#敵を生成
    anemy2 = teki(0.3,"ex06/fig/ニート.png",(0,ysp2),scr)#敵を生成

    #sco  = Score(10,10)
 
    beams = []
    bombs = []

    ongaku()#音楽関数
    while True:
        scr.blit()
        text = font.render(str(score), True, (255,0,0))   # 描画する文字列の設定
        scr.sfc.blit(text, [1600//2, 100])
        

        ysp=random.randint(1,4)
        xsp=random.randint(1,4)
    



        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return

            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                beams.append(kkt.attack())

        kkt.update(scr)

        ane.update(scr)
        ane1.update(scr)
        ane2.update(scr)

        anemy.update(scr)
        anemy1.update(scr)
        anemy2.update(scr)



        if len(beams) !=0:
            beams.update(scr)
            for b,bkb in enumerate(bombs):
                if bombs[b].rct.collidererct(beams.rct):
                    del bombs[b]



        pg.display.update()
        clock.tick(1000)

        if kkt.rct.colliderect(ane.rct):#球に当たった時の処理
            score+=100
            ane.rct.move_ip(1800,ysp)
            ane.rct.centery = random.randint(0,900)
            
        if kkt.rct.colliderect(ane1.rct):#球に当たった時の処理
            score+=100
            ane1.rct.move_ip(1800,ysp)
            ane1.rct.centery = random.randint(0,900)

        if kkt.rct.colliderect(ane2.rct):#球に当たった時の処理
            score+=100
            ane2.rct.move_ip(1800,ysp)
            ane2.rct.centery = random.randint(0,900)

#yakitoriが画面外に出たときの処理
        if ane.rct.left<=0: # 領域外  
            ane.rct.move_ip(1800,ysp)
            ane.rct.centery = random.randint(0,900) 

        if  ane1.rct.left<=0:# 領域外
            ane1.rct.move_ip(1800,ysp)
            ane1.rct.centery = random.randint(0,900)

        if ane2.rct.left<=0: # 領域外
            ane2.rct.move_ip(1800,ysp)
            ane2.rct.centery = random.randint(0,900)
    
    
#tekiに当たった時の処理
        if kkt.rct.colliderect(ane.rct):
            score-=100
            anemy.rct.move_ip(1800,ysp)
            anemy.rct.centery = random.randint(0,900)
    
        if kkt.rct.colliderect(ane1.rct):
            score-=100
            anemy1.rct.move_ip(1800,ysp)
            ane1.rct.centery = random.randint(0,900)
        if kkt.rct.colliderect(ane2.rct):
            score-=100
            anemy2.rct.move_ip(1800,ysp)
            anemy2.rct.centery = random.randint(0,900)


        #tekiが画面外に出たときの処理
        if anemy.rct.bottom<=0: # 領域外  
            anemy.rct.move_ip(xsp,900)
            anemy.rct.centery = random.randint(1800,0) 

        if  anemy1.rct.bottom<=0:# 領域外
            anemy1.rct.move_ip(xsp,900)
            anemy1.rct.centery = random.randint(1800,0)

        if anemy2.rct.bottom<=0: # 領域外
            anemy2.rct.centery = random.randint(1800,0)


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