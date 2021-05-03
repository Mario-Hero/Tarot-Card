#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Created by Mario Chen, 02.05.2021, Shenzhen
# My Github site: https://github.com/Mario-Hero

import random
import time
import os

SHOW_IMAGE = True  # show image or not

LANGUAGE_CN = 0          # 简体中文
LANGUAGE_EN = 1          # English
LANGUAGE = LANGUAGE_CN   # 修改语言 change the language

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

try:
    import numpy as np
except:
    os.system('pip install numpy')
    import numpy as np
try:
    import scipy.misc
    from scipy import ndimage
except:
    os.system('pip install scipy')
    import scipy.misc
    from scipy import ndimage


BIG_CARD_CN = ["愚者","魔术师","女祭司","女皇","皇帝","教皇","恋人","战车","力量","隐者","命运之轮","正义","倒吊人","死神","节制","恶魔","塔","星星","月亮","太阳","审判","世界"]
BIG_CARD_EN = ["The Fool","The Magician","The High Priestess","The Empress","The Emperor","The Hierophant","The Lovers","The Chariot","Strength","The Hermit","Wheel of Fortune","Justice","The Hanged Man","Death","Temperance","The Devil","The Tower","The Star","The Moon","The Sun","Judgement","The World"]

UPSIDEDOWN_CN = ["正位","逆位"]
UPSIDEDOWN_EN = ["Upright","Reversed"]

SMALL_CARD_TYPE_CN = ["权杖","星币","圣杯","宝剑"] 
SMALL_CARD_TYPE_EN = ["Wands","Pentacles","Cups","Swords"] 
SMALL_CARD_TYPE_PIC = ["w","p","c","s"] 

SMALL_CARD_CN = ["国王","王后","骑士","随从","十","九","八","七","六","五","四","三","二","首牌"]
SMALL_CARD_EN = ["King","Queen","Knight","Page","Ten","Nine","Eight","Seven","Six","Five","Four","Three","Two","Ace"]
SMALL_CARD_PIC = ["ki","qu","kn","pa","10","09","08","07","06","05","04","03","02","ac"]

if __name__ == '__main__':
    if LANGUAGE == LANGUAGE_EN:
        print("Please think of your question carefully... ")
        print("then input something randomly.(Input q to quit)")
        print("Then press enter.")
    elif LANGUAGE == LANGUAGE_CN:
        print("仔细思考你的问题……")
        print("随意在键盘上输入……(输入 q 以离开此地)")
        print("然后按下回车……")
    FIRST_TIME = True
    while True:
        inStr = input()
        if inStr == "q" or inStr == "quit":
            sys.exit(0)
        sun = 0
        for wd in inStr:
            sun = (sun + ord(wd)*random.randint(0,155))%156 
        ans = sun
        card = ""
        cardName = ""
        positiveCard = ans%2
        ans = int(ans / 2)
        if ans < 22:
            card = "maj_" + "%02d" % ans
            if LANGUAGE == LANGUAGE_CN:
                cardName = BIG_CARD_CN[ans] + " - " + UPSIDEDOWN_CN[positiveCard]
            elif LANGUAGE == LANGUAGE_EN:
                cardName = BIG_CARD_EN[ans] + " - " + UPSIDEDOWN_EN[positiveCard]
        else:
            mNum = ans - 22
            small_type = int(mNum/14)
            small_card = mNum-14*int(mNum/14)
            card = "min_" + SMALL_CARD_TYPE_PIC[small_type] + "_" + SMALL_CARD_PIC[small_card]
            if LANGUAGE == LANGUAGE_CN:
                cardName = SMALL_CARD_TYPE_CN[small_type]+SMALL_CARD_CN[small_card] + " - " + UPSIDEDOWN_CN[positiveCard]
            elif LANGUAGE == LANGUAGE_EN:
                cardName = SMALL_CARD_EN[small_card] + " of " + SMALL_CARD_TYPE_EN[small_type] +  " - " + UPSIDEDOWN_EN[positiveCard]
            
        print("\n" + cardName + "\n")
        if SHOW_IMAGE:
            plt.ion()
            plt.axis('off')
            cardPath = "./tarot/"+card + ".jpg"
            #Image.open(cardPath).show()
            if not FIRST_TIME:
                plt.figure()
                plt.axis('off')
            try:
                imgCard = mpimg.imread(cardPath)
                if positiveCard == 1:
                    imgCard = ndimage.rotate(imgCard, 180)
                plt.imshow(imgCard)
            except:
                print("Pictures not found.")
            FIRST_TIME = False
        if LANGUAGE == LANGUAGE_EN:
            print("Continue or leave...")
        elif LANGUAGE == LANGUAGE_CN:
            print("继续，亦或是离开……")


