#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Created by Mario Chen, 02.05.2021, Shenzhen
# My Github site: https://github.com/Mario-Hero

import random
import time

SHOW_IMAGE = True  # show image or not

#from PIL import Image
try:
    import matplotlib.pyplot as plt
    import matplotlib.pyplot as plt 
    import matplotlib.image as mpimg 
except:
    print ('import matplotlib error.......')
    os.system('pip install matplotlib')
    import matplotlib.pyplot as plt
    import matplotlib.pyplot as plt 
    import matplotlib.image as mpimg
    
import numpy as np



BIG_CARD = ["愚者","魔术师","女祭司","女皇","皇帝","教皇","恋人","战车","力量","隐者","命运之轮","正义","倒吊人","死神","节制","恶魔","塔","星星","月亮","太阳","审判","世界"]

SMALL_CARD_TYPE = ["权杖","星币","圣杯","宝剑"] 
SMALL_CARD_TYPE_PIC = ["w","p","c","s"] 

SMALL_CARD = ["国王","王后","骑士","随从","十","九","八","七","六","五","四","三","二","首牌"]
SMALL_CARD_PIC = ["ki","qu","kn","pa","10","09","08","07","06","05","04","03","02","ac"]

if __name__ == '__main__':
    print("Please think of your question, ")
    time.sleep(1)
    print("then input something randomly.(Input q to quit)")
    time.sleep(1)
    print("Then press enter.")
    FIRST_TIME = True
    while True:
        inStr = input()
        if inStr == "q" or inStr == "quit":
            sys.exit(0)
        sun = 0
        for wd in inStr:
            sun = sun + ord(wd)*random.randint(0,77) 
        ans = sun % 78
        card = ""
        cardName = ""
        if ans < 22:
            card = "maj_" + "%02d" % ans
            cardName = BIG_CARD[ans]
        else:
            mNum = ans - 22
            small_type = int(mNum/14)
            small_card = mNum-14*int(mNum/14)
            card = "min_" + SMALL_CARD_TYPE_PIC[small_type] + "_" + SMALL_CARD_PIC[small_card]
            cardName = SMALL_CARD_TYPE[small_type]+SMALL_CARD[small_card]
        print(cardName)
        if SHOW_IMAGE:
            plt.ion()
            plt.axis('off')
            cardPath = "./tarot/"+card + ".jpg"
            #Image.open(cardPath).show()
            if not FIRST_TIME:
                plt.figure()
                plt.axis('off')
            try:
                plt.imshow(mpimg.imread(cardPath))
            except:
                print("Pictures not found.")
            FIRST_TIME = False
        print("You can continue or leave.")


