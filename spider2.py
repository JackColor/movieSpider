# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 下午10:50
# @Author  : JackColor
# @File    : spider.py
from collections import namedtuple
from pprint import pprint

import requests
from bs4 import BeautifulSoup

Result = namedtuple("Res", "name,url")

res = requests.get("http://movie.douban.com/top250")

soup = BeautifulSoup(res.content, "lxml")

every_page_movie = soup.find_all("div", attrs={"class": "hd"})
result = list()
for movie in every_page_movie:
    for v in movie.find("span", attrs={"class": "title"}):
        res = Result(name=v, url=movie.find("a").get("href"))
        result.append(res)

pprint(result)


def get_movie_result(soup: BeautifulSoup):
    every_page_movie = soup.find_all("div", attrs={"class": "hd"})
    result = list()
    for movie in every_page_movie:
        for v in movie.find("span", attrs={"class": "title"}):
            res = Result(name=v, url=movie.find("a").get("href"))
            result.append(res)
