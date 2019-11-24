#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

"""获取图片文件路径
path: 文件路径
"""
def get_img_src(path):
    img_list = []

    with open(path,'r+',encoding='utf-8') as wallpapers:
        for line in wallpapers:
            wall_src = {}
            wall_src['img_src'] = re.search( r'img_src:(.*), *', line).group(1)
            wall_src['img_alt'] = re.search( r'img_alt:(.*)?"', line).group(1)
            img_list.append(wall_src)
            # print(wall_src)
    return img_list

if __name__ == "__main__":
    img_src_list = get_img_src('./wallpaper.txt')
    print(img_src_list)
