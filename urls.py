#!/usr/bin/env python
# coding=utf-8
from handlers import index,login

__author__ = 'qingfeng'


urls = [
    (r"/", index.IndexHandler),
    (r"/login", login.LoginHandler),
    (r"/logout", login.LogoutHandler),
    (r"/addcate", index.AddCateHandler),
    (r"/addsite", index.AddSitehandler)
]
