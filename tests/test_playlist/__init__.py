#coding:utf8
"""
测试播放列表
"""
import unittest

from unittest import mock
from netmusic import PlayList

class PlayListTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.pl = PlayList()


    def test_endpoint(self):
        self.assertEqual("/weapi/v6/playlist/detail", self.pl.endpoint, "解析播放属性信息不正确")


    def test_request(self):
        res = self.pl.request(604911722)
        self.assertTrue("trackIds" in res.text, "播放请求不正确")