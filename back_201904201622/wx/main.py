# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle
urls = (
    '/wx', 'Handle',
)
"""
class Handle(object):
    def GET(self):
        web.header('Content-Type', 'text/html;charset=UTF-8')
        return "<h1>您好，这是公众测试页面！this is handle view!</h1>"
"""
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
