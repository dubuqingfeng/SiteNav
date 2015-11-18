#!/usr/bin/env python
# coding=utf-8
import tornado.ioloop
import tornado.web
from handlers.index import GetSonCateModule, GetCateSiteModule, GetCateTagModule
from urls import urls
from setting import settings

__author__ = 'qingfeng'


class RightCateModule(tornado.web.UIModule):
    def render(self, cate_item):
        return self.render_string('modules/right_cate.html', cate_item=cate_item)


if __name__ == "__main__":
    application = tornado.web.Application(
        handlers=urls,
        ui_modules={
            'RightCate': RightCateModule,
            'GetSonCate': GetSonCateModule,
            'GetCateSite': GetCateSiteModule,
            'GetSiteTag': GetCateTagModule,
        },
        **settings
    )
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
