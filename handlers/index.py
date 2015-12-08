#!/usr/bin/env python
# coding=utf-8
from bson import ObjectId, DBRef
import tornado
from base import UserBaseHandler, UIModule

__author__ = 'qingfeng'


class IndexHandler(UserBaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        # user = {"username": "Dubuqingfeng", "password": "password", "email": "1135326346@qq.com",
        #        "site_type": "public", "theme": "default", "login_time": datetime.datetime.utcnow()}
        # user_id = users.insert_one(user).inserted_id
        user = self.db.user.find_one({"username": "Dubuqingfeng"})
        # left_item = {
        #     "classify_url": "http://www.baidus.csom/",
        #     "classify_name": "分类名",
        #     "classify_open": "target",
        #     "sort_order" : 255,
        #     "classify_color": "default",
        #     "classify_item": [
        #         {"left_item_url": "http://www.sohu.com/", "left_item_name": "搜狐", "left_item_open": "target"},
        #         {"left_item_url": "http://www.zhihu.com/", "left_item_name": "zhihu", "left_item_open": "target"}
        #         , {"left_item_url": "http://www.test.com/", "left_item_name": "test", "left_item_open": "target"}
        #         , {"left_item_url": "http://www.ts.com/", "left_item_name": "test2", "left_item_open": "target"}],
        # }
        # left_item_it = left_items.insert_one(left_item).inserted_id
        right_classify = self.db.right_classify

        right_cate = right_classify.find({"classify_parent": ""})
        right_classify_item = right_classify.find()
        left_item = self.db.left_item.find()
        classify = right_classify.find({"classify_parent": ""})

        if self.current_user:
            self.render('base.html', isLogin=True, user=user, left_items=left_item,
                        right_cate=right_cate, right_classify_items=right_classify_item, classify=classify)
        self.render('base.html', isLogin=False, user=user, left_items=left_item,
                    right_cate=right_cate,
                    right_classify_items=right_classify_item, classify=classify)


class AddCateHandler(UserBaseHandler):
    def data_received(self, chunk):
        pass

    def post(self, *args, **kwargs):
        object_parent_id = ""
        classify_name = self.get_argument("classify_name")
        classify_url = self.get_argument("classify_url")
        parent_classify_id = self.get_argument("classify_parent")
        if parent_classify_id != "":
            object_parent_id = ObjectId(parent_classify_id)
        right_classify_item = {
            "classify_name": classify_name,
            "classify_url": classify_url,
            "classify_color": "default",
            "classify_parent": object_parent_id,
            "classify_son": []
        }
        # 更新父类
        right_classify_item_id = self.db.right_classify.insert_one(right_classify_item).inserted_id
        if right_classify_item_id:
            self.db.right_classify.update({"_id": parent_classify_id},
                                        {"$push": {"classify_son": DBRef('right_classify', right_classify_item_id)}},
                                        multi=True)
            self.redirect("/")


class AddSitehandler(UserBaseHandler):
    def data_received(self, chunk):
        pass

    def post(self, *args, **kwargs):
        site_classify_item = ""
        site_classify_id = self.get_argument("site_cate")
        if site_classify_id != "":
            site_classify_item = ObjectId(site_classify_id)
        right_item = {
            "site_url": self.get_argument("site_url"),
            "site_open": "default",
            "site_type": self.get_argument("site_type"),
            "site_color": "default",
            "site_name": self.get_argument("site_name"),
            "classify_id": site_classify_item,
        }
        right_item_id = self.db.right_item.insert_one(right_item).inserted_id
        if right_item_id:
            # print(right_item_id)
            self.redirect("/")


class GetSonCateModule(UIModule):
    def render(self, cate_item):
        right_item = self.db.right_classify.find({"classify_parent": ObjectId(cate_item['_id'])})
        return self.render_string('modules/get_cate_son.html', cate_items=right_item)


class GetCateSiteModule(UIModule):
    def render(self, cate_item):
        right_item = self.db.right_item.find({"classify_id": ObjectId(cate_item['_id'])})
        return self.render_string('modules/get_cate_site.html', site_items=right_item)


class GetCateTagModule(UIModule):
    def render(self, cate_item):
        right_item = self.db.right_item.find({"classify_id": ObjectId(cate_item['_id']), "site_type": {"$ne": "default"}})
        return self.render_string('modules/get_site_tag.html', site_items=right_item)
