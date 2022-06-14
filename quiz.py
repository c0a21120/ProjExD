import datetime
from random import randint
st=datetime.datetime.now()
quiz=["サザエの旦那の名前は?","カツオの妹の名前は?","タラオはカツオから見てどんな関係？"]
kotae1=["マスオ","ワカメ","甥"]
kotae2=["ますお","わかめ","おい"]
kotae3=[1,2,"甥っ子"]
kotae4=[1,2,"おいっこ"]

q=randint(0,2)
print(quiz[q])
f"{quiz[q]}"
ans=input("答えを入力してください:")
if (ans==kotae1[q] or ans==kotae2[q] or ans==kotae3[q] or ans==kotae4[q]):
    print("正解！")
else:
    print("不正解")
ed=datetime.datetime.now()
print(f"解答まで{(ed-st).seconds}秒かかりました")