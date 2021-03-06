#coding:utf8

import json
from .utils.decrypt import get_params
from .utils.base import Request

class PlayList(Request):
    """
    获取收藏列表

    通过列表 ID，获取收藏列表中的歌单信息
    """
    def __init__(self) -> None:
        self.endpoint = "/weapi/v6/playlist/detail"

    def request(self, id, **kwargs):
        # 请求需要的表单数据
        item = {
            "id":str(id), 
            "offset": "0", 
            "total":True, 
            "limit":"1000",
            "n":"1000"
        }
        # 请求参数
        params = {"csrf_token": ""}

        # 获取请求体参数
        item.update(params)
        data = get_params(item)

        response = super().request(self.endpoint, "POST", params=params, data=data)
        return response


class Track(Request):
    """
    获取歌曲详情信息
    """
    def __init__(self) -> None:
        self.endpoint = "/weapi/v3/song/detail"

    
    def request(self, ids, **kwargs):
        """多任务请求歌曲详情"""
        ids = ids if isinstance(ids, list) else [ids]
        item = {"c": json.dumps([{'id': str(id)} for id in ids])}
        
        # 请求参数
        params = {"csrf_token": ""}
        item.update(params)
        
        data = get_params(item)

        response = super().request(self.endpoint, "POST", params=params, data=data, **kwargs)
        return response