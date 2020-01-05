ngrok = 'https://8937c8a0.ngrok.io'
#http://8937c8a0.ngrok.io/Data/getData?LineID=aaaaaaaa,0,test
import requests
import re
import json
import random
import configparser
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from imgurpython import ImgurClient

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
# line_bot_api
line_bot_api = LineBotApi('4XZuwm1PtF5Mo9hsm9pxvVDkzB/3Hpk6guO/yR6t+lh5Bm9MAmc3zaWTZr3+oWfaItY7e2tfPxOAjGxA7MlqGFkfEBSi15Kv5zKESAJqJdMNvP7fZmZUZB53/JqHMM2S13Y/G1epWlwuFd6EYcXb/AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('3e451da8bec99b211fb6142824891424')


# 監聽所有來自 /callback 的 Post Request
# @app.route('/') 為網址根目錄，當使用者瀏覽時，就會執行 index() 函式
@app.route("/callback", methods=['POST'])  
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    
    # get request body as text
    body = request.get_data(as_text=True)
    #app.logger.info("Request body: " + body)
    bodyjson=json.loads(body)
    #app.logger.error("Request body: " + bodyjson['events'][0]['message']['text'])
    app.logger.error("Request body: " + body)

    
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'



# 包裝回傳jason
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    USER_ID = event.source.user_id
    #print((event.source, event.message.text)) # 抓出(usertype,userid, text)
    
    
    Sent = [['蛋蛋測試區','新鮮度測驗','作答完3個選項即可點選「4.看雞蛋測驗結果」'],
        ['1.購買天數','請輸入雞蛋買了幾天？格式為：半形阿拉伯數字/天。例：3/天。如輸入正確，系統會回應您下一題題目','請再回答兩個問題'],
        ['2.是否為洗選蛋','2.選擇是否為洗選蛋','是洗選蛋','我買的是洗選蛋','不是洗選蛋','我買的不是洗選蛋'],
        ['3.儲存環境', '3.選擇儲存環境', '再回答3.儲存環境','室溫','我把雞蛋放在室溫','冰箱','我把雞蛋放在冰箱'],
        ['4.看雞蛋測驗結果','4.我要看雞蛋測驗結果'],
        ['蛋蛋長知識'],
        ['食安快訊']
           ]
    
 #預設忽略訊息
    
    

#給西瓜        
    # TO_WaterM = json.loads(requests.get(ngrok+'/Data/getData?LineID='+USER_ID).text) 
    #Re_Sent = [Sent[2][3], Sent[2][5], Sent[3][4], Sent[3][5], Sent[4][1]]

    
#簡化
    def MTAct(a,b,c,d):
        MessageTemplateAction(
            label = Sent[a][b],
            text  = Sent[c][d] )
    
    
    if event.message.text == Sent[0][0]:
        buttons_template = TemplateSendMessage(
            alt_text = Sent[0][1],
            template = ButtonsTemplate(
                title= Sent[0][1],
                text=  Sent[0][2],
                thumbnail_image_url='https://i.imgur.com/M8u7F7a.png',
                #image_background_color = '#FFE5CC'
                actions=[
                    MessageTemplateAction(
                        label= Sent[1][0],
                        text = Sent[1][1]
                    ),                    
                    MessageTemplateAction(
                        label= Sent[2][0],
                        text = Sent[2][1]
                    ),
                    
                    MessageTemplateAction(
                        label= Sent[3][0],
                        text = Sent[3][1],
                    ),
                    MessageTemplateAction(
                        label= Sent[4][0],
                        text = Sent[4][1]
                    )
                ]
            )
        )
        returnObj = buttons_template
#天數
    elif event.message.text == ('1' or '2' or '3' or '4'or '5'or '6'or '7'or '8'or '9'or '10'or '11'or '12'or '13'or '14'or '15'or '16'or '17'or '18' or'19'or '20'or '21'or '22'or '23'or '24'or '25'or '26'or '27'or '28'or '29'or '30' +'/天') :
        A = (event.message.text).split('/')[0]
        #print(A)
        buttons_template = TemplateSendMessage(
            alt_text = Sent[0][1],
            template = ButtonsTemplate(
                label= Sent[0][1] ,
                #title = label= Sent[0][1] ,
                text  = Sent[1][3],
                #thumbnail_image_url='https://i.imgur.com/M8u7F7a.png',
                #image_background_color = '#FFE5CC'
                actions=[                 
                    MessageTemplateAction(
                        label= Sent[2][0],
                        text = Sent[2][1]
                    ),
                    
                    MessageTemplateAction(
                        label= Sent[3][0],
                        text = Sent[3][1],
                    )
                ]
            )
        )
        #returnObj = buttons_template     　 
        returnObj = (buttons_template, TextSendMessage(text = '您購買了' + event.message.text ))
        # TO_WaterM


#2.洗選蛋       
    elif event.message.text == Sent[2][1] :
        buttons_template = TemplateSendMessage(
            alt_text =  Sent[2][1], #在不支援按鈕的裝置上會顯示的文字 通常是電腦
            template = ButtonsTemplate(
                text = Sent[2][1],
                actions=[
                    MTAct(2,2,2,3),
                    MTAct(2,4,2,5),
                    MTAct(3,2,3,1)
                ]
            )
        )     
        returnObj = buttons_template
        
        
         

 
 #3.儲存環境
    elif event.message.text == Sent[3][1] :
        #Confirm_template = TemplateSendMessage(
        buttons_template = TemplateSendMessage(
            alt_text = Sent[3][1] , 
            #在不支援按鈕的裝置上會顯示的文字 通常是電腦
            template = ConfirmTemplate(
                text = Sent[3][0],
                actions=[
                    MessageTemplateAction(
                        label = Sent[3][3] ,
                        text = Sent[3][4]
                    ),
                    MessageTemplateAction(
                        label = Sent[3][5],
                        text = Sent[3][6]
                    )
                ]
            )
        )     
        returnObj = buttons_template
        #returnObj = Confirm_template

#蛋知識        
    elif event.message.text == "蛋蛋長知識":
        #aa = json.loads(requests.get(ngrok+'/Data/getData?LineID='+USER_ID).text)
        #aa['Q_DESC']
        #aa['Q_MEMO']
        
        returnObj =  TextSendMessage(text='aa')        
        line_bot_api.reply_message(
        event.reply_token,
        returnObj)     

#食安快訊        
    elif event.message.text == "食安快訊":
             
        Image_Carousel = TemplateSendMessage(
        alt_text='觀看食安快訊',
            template=ImageCarouselTemplate(
            columns=[
            ImageCarouselColumn(
                image_url='https://i.imgur.com/M8u7F7a.png',
                action = URITemplateAction(
                    label='新聞1',
                    uri= 'http://www.tmu.edu.tw/students/super_pages.php?ID=students'
                )
            ),
            ImageCarouselColumn(
                image_url='https://i.imgur.com/M8u7F7a.png',
                action = URITemplateAction(
                    label='新聞2',
                    uri= 'http://www.tmu.edu.tw/students/super_pages.php?ID=students'
                )
            )
            ]
            )
        )
        returnObj = Image_Carousel
    
    # 回傳給西瓜區 缺天數
    #elif event.message.text == Sent[2][3] or Sent[2][5] or Sent[3][4] or Sent[3][5] or Sent[4][1] :
        # TO_WaterM
    
    # 預設忽略部分系統訊息        
    elif event.message.text == Sent[1][1] :
        return(0)
    
    
    else:
        returnObj = TextSendMessage(
            text = "歡迎使用蛋BOT！請點選「查看更多資訊」選擇功能")
    
    #returnObj =  TextSendMessage(text=event.message.text) 回聲
    
    
    line_bot_api.reply_message(
        event.reply_token,
        returnObj)

    #reply_Token是每次的訊息編號

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
