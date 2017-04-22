#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import html
from config import getConfig
import os

login_url       = 'https://monocloud.net/login'
server_list_url = 'https://monocloud.co/server'
template        = open('openconnect_tpl.sh').read()

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

    anyconnectPage = myService.xpath('//a[starts-with(@href, "https://monocloud.net/service/") and contains(text(), "Classic")]/@href')
    anyconnectName = myService.xpath('//a[starts-with(@href, "https://monocloud.net/service/") and contains(text(), "Classic")]/text()')

    if not os.path.isdir('openconnect'):
        os.mkdir('openconnect')

    for (name, url) in zip(anyconnectName, anyconnectPage):
        getAnyconnectInfo(session, url.replace('service', 'server'), name, form)

def getAnyconnectInfo(session, url, name, form):
    print url
    response = session.get(url)
    tree = html.fromstring(response.content)
    entries = tree.xpath('//div[@class="member-info"]//span/text()')
    # import ipdb; ipdb.set_trace()
    addresses = entries[::2]
    urls = entries[1::2]

    print name
    print "================="

    if not os.path.isdir(name):
        os.mkdir(name)
    for (address, server) in zip(addresses, urls):
        command = template.format(password=form['password'], user=form['email'], server=server)
        filename = 'openconnect/{}.sh'.format(server)
        open(filename, 'w').write(command)
        os.chmod(filename, 0700)
        print server, "script generated!"


def main():
    form = getConfig()
    sendRequest(form)

if __name__ == '__main__':
    main()
