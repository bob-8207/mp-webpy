# -*- coding: utf-8 -*-
# filename: media.py
import urllib2
import json
from basic import Basic
import time
import random
from mysqldb import DBmysql
import pymysql
pymysql.install_as_MySQLdb()


class Media(object):
    """"""公众号接收到的图片按照指定路径和名称保存""""""
    def get(self, accessToken, mediaId, fromUser):
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (accessToken, mediaId)
        urlResp = urllib2.urlopen(postUrl)
        exclude_code = ''.join(str(random.choice(range(10))) for _ in range(10))
        now_datetime= (time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())))
        pic_code = str(now_datetime) + "-" +str(exclude_code)
        pic_name = pic_code +".jpg"
        pic_path = "/usr/local/bin/pic/"
        headers = urlResp.info().__dict__['headers']
        if ('Content-Type: application/json\r\n' in headers) or ('Content-Type: text/plain\r\n' in headers):
            jsonDict = json.loads(urlResp.read())
            print jsonDict
        else:
            buffer = urlResp.read()   #素材的二进制
            mediaFile = file( pic_path + pic_code +".jpg", "wb")
            mediaFile.write(buffer)
            conn = pymysql.connect(host='192.168.1.221', port=3306, user='root', passwd='cmdbcmdb', db='WECHAT_DATA')
            cur = conn.cursor()
            cur.execute('INSERT INTO PIC_UPLOAD_RECORD(openid,SAVE_PATH,PIC_NAME,UPLOAD_TIME) VALUES(%s, %s, %s, %s)',(fromUser, pic_path, pic_name, now_datetime))
            #cur.execute('INSERT INTO PIC_UPLOAD_RECORD(openid,SAVE_PATH,PIC_NAME,UPLOAD_TIME) VALUES(%s,%s,%s,%s)' %(fromUser, pic_path, pic_names, DTIME))
            cur.execute('select * from PIC_UPLOAD_RECORD')
            for s in cur.fetchall():
                print(s)
            conn.commit()
            cur.close()
            conn.close()


            print "get successful"

if __name__ == '__main__':
    myMedia = Media()
    accessToken = Basic().get_access_token()
    mediaId = "V5EpKZGrKkyYVEt_WlS25UsMJwdhCn50TS0isCeoYvuy0lq9xJwZuUaeM7SdKzFK"
    fromUser = 'sadfasdfasdfdfxcvcfsdf'
    myMedia.get(accessToken, mediaId, fromUser)
    #print exclude_code