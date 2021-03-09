#coding:utf8
import urllib
import requests

class Request:
    """
    网络请求
    """
    HOST = "https://music.163.com"
    def __init__(self) -> None:
        pass
    
    def request(self, url, method="POST", **kwargs):
        """发出网络请求"""
        if "http" not in url:
            url = urllib.parse.urljoin(self.HOST, url)
        
        response = requests.request(method, url, **kwargs)

        if response.status_code != 200:
            raise requests.RequestException(f"请求异常，状态码为: {response.status_code}")
            
        if len(response.text) == 0:
            raise Exception("响应内容异常")

        return response