#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-15 16:42:15
# @Author  : James—jiajia (976033262@qq.com)
# @Link    : http://example.org
# @Version : $Id$

from urllib import request
from lxml import etree
import os


class MzSpider():
    def __init__(self):
        # 爬虫的开关，True是打开，False是关闭
        self.switch = True
        # cid是图片类型
        self.cid = input("请输入你想要起飞的图片类型：\n 0.所有 \n 2.大胸妹 \n 3.美腿控 \n 4.有颜值 \n 5.大杂烩 \n 6.小翘臀 \n 7.黑丝袜 \n")
        # pager是图片的页数
        self.pager = 1

    def load_cid(self, url):
        headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}
        # link = "http://www.dbmeinv.com/index.htm?cid=6&pager_offset=1"
        req = request.Request(url, headers = headers)
        response = request.urlopen(req).read()
        # print(response)
        self.load_pager(response)

    def load_pager(self, response):
        html = etree.HTML(response)
        src_list = html.xpath('//img[@class="height_min"]/@src')
        for src in src_list:
            src = src.replace("bmiddle","large")
            self.write_img(src)

    def write_img(self, url):
        req = request.Request(url)
        response = request.urlopen(req).read()
        image_name = url[-10:]
        print("正在下载%s" % image_name)
        with open(image_name, "wb") as f:
            f.write(response)

    def start_work(self):
        while self.switch:
            # 将cid和pager拼接成完整的链接
            url = "https://www.dbmeinv.com/index.htm?cid=" + self.cid + "&pager_offset=" + str(self.pager)
            print("正在进入网址")
            self.load_cid(url)
            common = input("下载完成，是否继续下载下一页:(yes or no)")
            if common == "yes":
                self.pager += 1
                self.start_work()
            else:
                self.switch = False
        print("谢谢使用")


if __name__ == "__main__":
    doubanmz = MzSpider()
    doubanmz.start_work()



