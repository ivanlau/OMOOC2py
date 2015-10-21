# -*- coding:UTF-8 -*-
import sys,os
import time,datetime
shijian=time.strftime("%Y-%m-%d %X", time.localtime())
var = 1
while var == 1:
#选择运行的功能
    gongneng=raw_input("请输入希望运行的功能所对应的数字：1.录入日记，2.查看日记；输入其他任意字符程序自动退出。(☆ﾟ∀ﾟ)：")
#录入日记
    if gongneng=="1":
        neirong=raw_input("请输入新增内容 (→_→):")
        xinneirong="\n" + shijian+' ' + neirong
        print "将被记录的内容是(≖ ‿ ≖)✧:" + xinneirong
        if os.path.exists("riji.txt"):
            pass
        else:
            f = open("riji.txt", "w")
            f.close()
    
        with open("riji.txt","r+") as f:
            old=f.read()
            f.seek(0)
            f.write(xinneirong + old)
   
    elif gongneng=="2":
        f = open("riji.txt", "r")  
        print f.read()

    else:
      print ("再见(｡･ω･)ﾉﾞ")
      exit()


