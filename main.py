from pywinauto.application import Application
import pywinauto.mouse as mouse
import datetime
import pygame
pygame.mixer.init()
track = pygame.mixer.music.load('./1.mp3')

WECHAT_PATH = "D:/Tencent/WeChat/WeChat.exe"
CHANGE = True

app = Application(backend='uia').connect(path=WECHAT_PATH)

win = app.window(title="微信")

def click(ele_name,win=win,control_type=None):
    ele = win.window(best_match=ele_name,control_type=control_type)
    # print(ele.criteria)
    element_position = ele.rectangle()
    pos = (int((element_position.left + element_position.right) / 2),int((element_position.top + element_position.bottom) / 2))
    ele.set_focus()
    mouse.click(button='left',coords=pos)

def find_text(totext):
    global CHANGE
    chatbox = win.window(title='会话',control_type="List")
    chats = chatbox.wrapper_object().descendants(depth=4)
    # print(chats)
    c = 0
    for chat in chats:
        if (chat.friendly_class_name() == "Static"):
            text = chat.window_text()
            if text == totext:
                c += 1
                if CHANGE:
                    print("\n")
                    CHANGE = False
                print("\rFound red envelope - %s"%datetime.datetime.now().strftime("%H:%M:%S"),end="          ")
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play()
                chat.draw_outline(colour="red")
        if chat == chats[-1] and c==0:
            if not CHANGE:
                print("\n")
                CHANGE = True
            print("\rCan't find:%s"%datetime.datetime.now().strftime("%H:%M:%S"),end='      ')
               
while 1:
    #r'收到红包，请在手机上查看'
    find_text(r'收到红包，请在手机上查看')
