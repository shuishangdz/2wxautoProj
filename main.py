# 这是一个使用wxauto包去实现个人微信的收发消息
import wxauto
from wxauto import *
import time

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')


print(f'Hi, 123123')
send_msg = '你好'
who = '文件传输助手'
keyword = "测试" # 触发关键字
wx = WeChat()
wx.ChatWith(who)
wx.SendMsg(send_msg)

def receive_msg():
    while True:
        messages = wx.GetLastMessage() # 接收消息
        for i in range(len(messages)):
            msg = messages[i]
            if msg.msgtype == "text": # 文本消息
                if keyword in msg.info["content"]: # 消息中有关键字
                    wx.SendMsg(send_msg) #发送消息
                    return # 结束程序
        time.sleep(0.1)
receive_msg()
