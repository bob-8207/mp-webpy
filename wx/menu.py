# -*- coding: utf-8 -*-
# filename: menu.py
import urllib
from basic import Basic

class Menu(object):
    def __init__(self):
        pass
    def create(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        if isinstance(postData, unicode):
            postData = postData.encode('utf-8')
        urlResp = urllib.urlopen(url=postUrl, data=postData)
        print urlResp.read()

    def query(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

    def delete(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

    #获取自定义菜单配置接口
    def get_current_selfmenu_info(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

if __name__ == '__main__':
    myMenu = Menu()
    postJson = """
    {
        "button":
        [
            {
                "name": "【资讯】",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "政策法规",
                        "url": "http://6666.natappvip.cc/"
                    },
                    {
                        "type": "view",
                        "name": "减油措施",
                        "url": "https://mp.weixin.qq.com/s?__biz=Mzg4MTE2MTM5Mg==&tempkey=MTAwOV9xa3laVFJZakFYY1B4dFJjRGRxS1BOeHJXd24xc3phNU5QVUppQ05nYVY4T3BKRnEyZmJVYUdGRFlIQUJLWnVvcnVFVFdES21GMF9RYi1BMzU1ZHdYQWxCTG1RSi1XNkl6ZGJPNkRiazZYU1prLXZnSkFmUHk5bU9xWUNacFVSbmJ3Mm9Kbi1SQmNJa1pULTByZGN0Z3o3OFpJMkNjM0J5Y1hqUkRRfn4%3D&chksm=4f6b64cc781ceddaf152676dfb60e91c0a0a99e693607116294d22537c18168f4edd7a99e728##"
                    },
                    {
                        "type": "view_limited",
                        "name": "新闻报导",
                        "media_id": "QrBLM_chUEA-NCVqiPCL6XT2x1NaKwpjoS0QE32ogjc"
                    },
                    {
                        "type": "view",
                        "name": "减油排行",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    }
                ]
            },
            {
                "name": "【核查】",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "考核培训",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "接单系统",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "pic_photo_or_album", 
                        "name": "考核记录", 
                        "key": "rselfmenu_0_0", 
                        "sub_button": [ ]
                    },
                    {
                        "name": "考勤定位", 
                        "type": "location_select", 
                        "key": "rselfmenu_0_1", 
                        "sub_button": [ ]
                    } 
                ]
            },
           {
                "name": "【服务】",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "政策宣讲",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "在线客服",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "微社区",
                        "url": "http://www.fancytech.ai"
                    },
                    {
                        "type": "view",
                        "name": "最优惠",
                        "url": "https://www.163.com"
                    },
                    {
                        "type": "view",
                        "name": "我的",
                        "url": "http://wx.fancytech.ai:8091"
                    }
                ]
            }
          ]
    }
    
    """
    accessToken = Basic().get_access_token()
    #myMenu.delete(accessToken)
    myMenu.create(postJson, accessToken)
