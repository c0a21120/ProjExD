import datetime
from random import randint
st=datetime.datetime.now()
def diff(a):
    quiz=["サザエの旦那の名前は?","カツオの妹の名前は?","タラオはカツオから見てどんな関係？"]
    kotae1=["マスオ","ワカメ","甥"]
    kotae2=["ますお","わかめ","おい"]
    kotae3=[1,2,"甥っ子"]
    kotae4=[1,2,"おいっこ"]

    q=a
    return quiz[q]

def main(void):
    kota=diff(randint(0.2))

    ans=input("答えを入力してください:")



    if (ans==kota):
        print("正解！")
    else:
        print("不正解")
    ed=datetime.datetime.now()
    print(f"解答まで{(ed-st).seconds}秒かかりました")