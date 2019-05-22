# -*- coding: utf-8 -*-
# filename: handle.py
import web
import receive
import reply
from basic import Basic
from media import Media
#import xml.dom.minidom

class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            myMedia = Media()
            #print recMsg
            #print recMsg.MsgType
            if isinstance(recMsg, receive.Event ):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'event':
                    event = recMsg.Event
                    if event == 'subscribe':
                        content = "Hi, thanks for attention Fancytech WeChat! /::D"
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
            elif isinstance(recMsg, receive.Msg ):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    Content = recMsg.Content
                    print Content
                    if Content == '111':
                        content = "别浪费流量，乱发消息！/:wipe"
                    else:
                        content =  "Hi, Can I help you ? /::,@"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    print "反馈文字信息成功！！！！！！！！！"
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    content = "图片已经接收...Thanks♪(･ω･)ﾉ"
                    mediaId = recMsg.MediaId
                    accessToken = Basic().get_access_token()
                    myMedia.get(accessToken, mediaId, toUser)
                    replyMsg = reply.TextMsg(toUser,fromUser, content)
                    #replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                print "暂且不处理"
                return reply.Msg().send()
        except Exception, Argment:
            return Argment