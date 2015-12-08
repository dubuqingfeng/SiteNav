#!/usr/bin/env python
# coding=utf-8
from base import BaseHandler

__author__ = 'qingfeng'


class LoginHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):

        right_classify = self.db.right_classify

        right_cate = right_classify.find({"classify_parent": ""})
        left_item = self.db.left_item.find()

        right_classify_item = right_classify.find()
        classify = right_classify.find({"classify_parent": ""})
        if self.get_current_user():
            self.redirect(self.get_argument('next', '/'))
        else:
            self.render('base.html', isLogin=False, user=None, left_items=left_item,
                        right_cate=right_cate, right_classify_items=right_classify_item, classify=classify)

    def post(self, *args, **kwargs):
        email = self.get_argument('email')
        password = self.get_argument('password')

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
