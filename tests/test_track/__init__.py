#coding:utf8
"""
测试音乐详情信息
"""
import unittest
import pytest
import json
from os import path
from unittest import mock
from netmusic import Track



@pytest.fixture
def response():
    with open(path.join(path.dirname(__file__), "response.json"), "r") as file:
        data = json.dump(file)
    return data

class TrackTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.tr = Track()


    def test_endpoint(self):
        self.assertEqual("/weapi/v3/song/detail", self.tr.endpoint, "解析歌曲属性信息不正确")


    def test_request(self):
        res = self.tr.request(31040907)
        self.assertTrue("name" in res.text, "播放请求不正确")