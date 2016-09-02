#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import html
from config import getConfig
from util import isWindow
import os
import codecs


login_url = 'https://bluecloud.xyz/auth/login'
if isWindow():
    template  = codecs.open('shadowsocks_win_tpl.bat', encoding='utf-8').read()
else:
    template  = codecs.open('shadowsocks_tpl.sh', encoding='utf-8').read()

def sendRequest(form):
    session = requests.Session()
    response = session.post(login_url, data=form)
    tree = html.fromstring(response.content)
    myService = tree.xpath(u'//h2[text()="我的服务"]')[0].getparent()
    shadowsocksPage = myService.xpath('//a[starts-with(@href, "https://bluecloud.xyz/shadowsock")]/@href')
    for url in shadowsocksPage:
        getShadowsocksInfo(session, url)

def getShadowsocksInfo(session, url):
    response = session.get(url)
    tree = html.fromstring(response.content)
    entries = tree.xpath('//*[@class="row"]')
    serviceName = entries[0].xpath('//h4/text()')[0]
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
    texts = entry.xpath('.//p/text()')
    _, _, server, _, _, method = texts[0].split(' ')
    arr = texts[1].split(' ')
    password, port, ratio = arr[1], arr[3], arr[7]
    extra = u'\n'.join(map(lambda x: u'echo ' + x, texts[2:]))
    command = template.format(server=server, method=method, password=password, port=port, ratio=ratio, extra=extra)
    with codecs.open(folder + '/' + server + '.bat', 'w', encoding='utf-8') as file:
        file.write(command)
    print server

def generateFile(folder, entry):
    texts = entry.xpath('.//p/text()')
    _, _, server, _, _, method = texts[0].split(' ')
    arr = texts[1].split(' ')
    password, port, ratio = arr[1], arr[3], arr[7]
    extra = '\n'.join(texts[2:])
    command = template.format(server=server, method=method, password=password, port=port, ratio=ratio, extra=extra)
    with codecs.open(folder + '/' + server + '.sh', 'w', encoding='utf-8') as file:
        file.write(command)
    os.chmod(folder + '/' + server + '.sh', 0700)
    print server

def main():
    sendRequest(getConfig())

main()