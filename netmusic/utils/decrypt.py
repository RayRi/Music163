#coding:utf8
"""
解决请求参数处理的问题，生成表单请求参数
"""
import execjs
import json
from os import path

# 加密需要的基本参数
e = "010001"
g = "0CoJUm6Qyw8W8jud"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17" \
    "a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c9387011" \
    "4af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef5" \
    "2741d546b8e289dc6935b3ece0462db0a22b8e7"

# 编译 JS 文件，以调用相关方法
fpath = path.join(path.dirname(__file__), "../lib/node/decryptV2.js")
cwd = path.join(path.dirname(__file__), "../lib/node/node_modules")

with open(fpath, "r", errors="ignore") as file:
    js = file.read()
    ctx = execjs.compile(js, cwd=cwd)



def get_params(data):
    """获取请求需要的参数

    Args:
    -------
    data: dict, 需要加密的相关参数

    Result:
    --------
    返回包含 'params' 和 'encSecKey' 键的字典
    """
    result = ctx.call("asrsea", json.dumps(data), e, f, g)
    return {
        "params": result["encText"],
        "encSecKey": result["encSecKey"]
    }