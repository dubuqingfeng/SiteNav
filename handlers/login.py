#!/usr/bin/env python
# coding=utf-8
from pymongo import MongoClient
import tornado

from base import BaseHandler
import configs

__author__ = 'qingfeng'

db = configs.client.sitenav

left_items = db.left_item
right_classify_items = db.right_classify


class LoginHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        left_item = left_items.find()
        right_classify_it = right_classify_items.find()
        if self.get_current_user():
            self.redirect(self.get_argument('next', '/'))
        else:
            self.render('base.html', isLogin=False, user=None, left_items=left_item,
                        right_classify_it=right_classify_it)

    def post(self, *args, **kwargs):
        email = self.get_argument('email')
        password = self.get_argument('password')
        print(password)

        self.set_secure_cookie("user", email)
        self.redirect(self.get_argument('next', '/'))


class LogoutHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        if self.get_argument("logout", None):
            self.clear_all_cookies()
            self.redirect("/")
        self.redirect("/")
