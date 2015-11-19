#!/usr/bin/env python
# coding=utf-8
import tornado.web
import configs

__author__ = 'qingfeng'


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.db = configs.client.sitenav

    def data_received(self, chunk):
        pass

    def get_current_user(self):
        user_id = self.get_secure_cookie("user")
        if not user_id: return None
        return self.get_secure_cookie("user")

    def get(self, *args, **kwargs):
        self.write("test")


class UserBaseHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def prepare(self):
        print 'prepare'

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        print('test')


class UIModule(tornado.web.UIModule):

    def __init__(self, handler):
        super(UIModule, self).__init__(handler)
        self.db = configs.client.sitenav

    def render(self, *args, **kwargs):
        pass
