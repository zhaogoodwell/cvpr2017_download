#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 14:02:50 2017

@author: zhao
"""

import re
import requests
from multiprocessing import Pool

proxies = {
    'http': 'socks5://127.0.0.1:1080',
    'https': 'socks5://127.0.0.1:1080'
}


def download_single(info):
    proxies = {
            'http': 'socks5://127.0.0.1:1080',
            'https': 'socks5://127.0.0.1:1080'
            }
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
    if info == None:
        return 0
    
    url_base = r'http://openaccess.thecvf.com/content_cvpr_2017/'
    file_url = url_base+info[0]+'/'+info[1]+'.pdf'
    print(file_url)
    
    file = requests.get(file_url,headers = headers, proxies=proxies)
    with open(info[1]+'.pdf','wb') as f:
        f.write(file.content)

def Print_info(im):
    if im == None:
        pass
    print(im)


target_url = r'http://openaccess.thecvf.com/CVPR2017.py'
r = requests.get(target_url)
info  = r.text
patern = re.compile(r"content_cvpr_2017/([\w]+?)/([\w]+?)\.pdf")
group = re.findall(patern,info)

p = Pool(16)
p.map(download_single,group)