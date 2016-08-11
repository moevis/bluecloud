#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import html
from config import getConfig
import os

login_url       = 'https://bluecloud.xyz/auth/login'
server_list_url = 'https://bluecloud.xyz/server'
template        = open('openconnect_tpl.sh').read()

def sendRequest(form):
    session = requests.Session()
    session.post(login_url, data=form)
    response =session.get(server_list_url)
    tree = html.fromstring(response.content)
    server_link = tree.xpath('//*[@id="home"]/div[3]/table/tbody/tr/td[1]/text()')
    protocol_support = tree.xpath('//*[@id="home"]/div[3]/table/tbody/tr/td[2]/text()')
    if not os.path.isdir('openconnect'):
        os.mkdir('openconnect')
    for server, protocol in zip(server_link, protocol_support):
        if protocol.find(u'AnyConnect') != -1 and server.find('hk') != 0:
            command = template.format(password=form['password'], user=form['identity'], server=server)
            filename = 'openconnect/{}.sh'.format(server)
            open(filename, 'w').write(command)
            os.chmod(filename, 0700)
            print server, "script generated!"

def main():
    form = getConfig()
    sendRequest(form)

if __name__ == '__main__':
    main()
