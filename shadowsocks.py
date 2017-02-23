#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import html
from config import getConfig
from util import isWindow
import os
import codecs


login_url = 'https://monocloud.net/login'
if isWindow():
    template  = codecs.open('shadowsocks_win_tpl.bat', encoding='utf-8').read()
else:
    template  = codecs.open('shadowsocks_tpl.sh', encoding='utf-8').read()

def sendRequest(form):
    session = requests.Session()
    response = session.get(login_url)
    token = html.fromstring(response.content).xpath('/html/body/div[3]/div[1]/div[2]/form/input')[0].value
    form['_token'] = token
    response = session.post(login_url, data=form)
    # response = session.get('https://monocloud.net/home')
    tree = html.fromstring(response.content)
    # import ipdb; ipdb.set_trace()

    myService = tree.xpath(u'//*[@id="sidebar-menu"]/ul')[0]
   
    shadowsocksPage = myService.xpath('//a[starts-with(@href, "https://monocloud.net/service/")]/@href')
    for url in shadowsocksPage:
        getShadowsocksInfo(session, url.replace('service', 'shadowsocks'))

def getShadowsocksInfo(session, url):
    response = session.get(url)
    tree = html.fromstring(response.content)
    entries = tree.xpath('//table[@class="table"]')
    serviceName = tree.xpath('//*[@class="page-title"]/text()')[0]
    if "Classic" in serviceName:
        return
    print serviceName
    print "================="
    if not os.path.isdir(serviceName):
        os.mkdir(serviceName)
    if isWindow():
        for entry in entries:
            generateFileWin(serviceName, entry)
    else:
        for entry in entries:
            generateFile(serviceName, entry)

def generateFileWin(folder, entry):
    texts = entry.xpath('.//td/text()')
    extra, server, port, ratio, password, method = texts
    command = template.format(server=server, method=method, password=password, port=port, ratio=ratio, extra=extra)
    with codecs.open(folder + '/' + server + '.bat', 'w', encoding='utf-8') as file:
        file.write(command)
    print server

def generateFile(folder, entry):
    texts = entry.xpath('.//td/text()')
    extra, server, port, ratio, password, method = texts
    command = template.format(server=server, method=method, password=password, port=port, ratio=ratio, extra=extra)
    with codecs.open(folder + '/' + server + '.sh', 'w', encoding='utf-8') as file:
        file.write(command)
    os.chmod(folder + '/' + server + '.sh', 0700)
    print server

def main():
    sendRequest(getConfig())

main()