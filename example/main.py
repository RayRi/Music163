#coding:utf8
"""
示例代码: 解析 JSON 数据
通过网易音乐中列表 ID(ID 在 https://music.163.com/.../music/playlist?id=251915293)，获取其中歌曲信息
* 歌曲名
* 专辑名
* 歌手名
"""
import time
import random
import arrow

from hashlib import md5
from collections import defaultdict

from netmusic import PlayList, Track




def _timestamp():
    return int(arrow.now().float_timestamp)


def _random_jsession_id():
    seq = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZ\\/+'
    random_seq = random.choices(seq, k=176)
    return ''.join(random_seq) + ':' + str(_timestamp())


def _random_nuid(with_timestamp=True):
    seq = '0123456789abcdefghijklmnopqrstuvwxyz'
    random_seq = random.choices(seq, k=32)
    if with_timestamp:
        return ''.join(random_seq) + ',' + str(_timestamp())
    else:
        return ''.join(random_seq)


base_cookies = {
    'JSESSIONID-WYYY': _random_jsession_id(),
    '_iuqxldmzr_': '32',
    '_ntes_nnid': _random_nuid(),
    '_ntes_nuid': _random_nuid(with_timestamp=False)
}



# 实例化对象
play = PlayList()
track = Track()



def main(ids):
    """列表信息

    """
    data = defaultdict(list)
    _ids = []
    for i in ids:
        # 获取每个列表中的歌曲 ID
        res = play.request(i)
        try:
            track_ids = [i['id'] for i in res.json()['playlist']['trackIds']]

            # 获取歌曲信息
            time.sleep(3)
            res = track.request(track_ids)#, cookies=base_cookies)
            filter_ids = [i for i in track_ids if i not in data['id']]
            data['id'].append(filter_ids)
            if "songs" not in res.json():
                data['id'] = [None] * len(filter_ids)
                continue
            
            for song in res.json()['songs']:
                if song['name'] in data['name'] and song['al']['name'] in data['album']:
                    continue
                data['name'].append(song['name'])
                data['artists'].append([artist['name'] for artist in song['ar']])
                # import ipdb; ipdb.set_trace()
                data['album'].append(song['al']['name'])
                data['album_url'].append(song['al']['picUrl'])
            
            time.sleep(3)
        except KeyError as err:
            _ids.append(i)
    return data, _ids






if __name__ == "__main__":
    # 获取播放列表信息，解析其中的 id
    # ids = [251915293, 25191529, 2519152]
    ids = [
        25191893, 2617985655, 2107269110, 2057213560, 1992161263, 951600874, 
        645613981, 535776283, 367404135, 323097603, 155959274,155236210,
        125643559, 125633514, 122188905, 70042452, 66738827, 57382378, 30353798
    ]
    data = main(ids)