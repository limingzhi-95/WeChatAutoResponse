#coding=utf8
import itchat
import time
from WeChat.msg_processor import TuRingApi

"""
参数    类型     Text 键值
TEXT	文本	文本内容(文字消息)
MAP	地图	位置文本(位置分享)
CARD	名片	推荐人字典(推荐人的名片)
SHARING	分享	分享名称(分享的音乐或者文章等)
PICTURE 下载方法	 	图片/表情
RECORDING	语音	下载方法
ATTACHMENT	附件	下载方法
VIDEO	小视频	下载方法
FRIENDS	好友邀请	添加好友所需参数
SYSTEM	系统消息	更新内容的用户或群聊的UserName组成的列表
NOTE	通知	通知文本(消息撤回等)

"""
# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register(["Text", 'Picture', 'Recording'])
def text_reply(msg):
    # 当消息不是由自己发出的时候
    print(msg)
    if not msg['FromUserName'] == myUserName:
        api_wrapper = TuRingApi(api_key="", user_id="")
        msg_info = {'text': msg['Text']}
        msg = api_wrapper.send_msg(msg_info, msg_type=api_wrapper.MsgType.Text)

        # 回复给好友
        return u'{}'.format(msg)


# todo 加好友信息识别,做配置文件, supervisor 启动, 加多种类型信息的支持,加每天定期发送特定信息
if __name__ == '__main__':
    itchat.auto_login()

    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()
