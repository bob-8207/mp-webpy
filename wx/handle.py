# -*- coding: utf-8 -*-
# filename: handle.py
import web

import receive
import reply
from basic import Basic
from media import Media


class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)

            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    content =  "Hi,welcome attention Fancytech WeChat!          ∩( ・ω・)∩萌萌哒"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    myMedia = Media()
                    accessToken = Basic().get_access_token()
                    myMedia.get(accessToken, mediaId, toUser)
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()

            else:
                print "暂且不处理"
                return reply.Msg().send()
        except Exception, Argment:
            return Argment