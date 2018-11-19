# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 下午11:20
# @Author  : JackColor
# @File    : spider.py
from collections import namedtuple

import requests
from bs4 import BeautifulSoup

Result = namedtuple("Res", "name,url")


def get_page_url(start_url=None):
    if not start_url:
        return []
    res = requests.get(start_url).content
    page_soup = BeautifulSoup(res, "lxml")
    page_div = page_soup.find("div", attrs={"class": "paginator"})
    yield from page_div.find_all("a")


def get_movie_result(soup: BeautifulSoup):
    every_page_movie = soup.find_all("div", attrs={"class": "hd"})
    result = list()
    for movie in every_page_movie:
        for v in movie.find("span", attrs={"class": "title"}):
            res = Result(name=v, url=movie.find("a").get("href"))
            result.append(res)


if __name__ == '__main__':
    url = "http://movie.douban.com/top250"
