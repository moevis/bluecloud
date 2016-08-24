#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import html
from config import getConfig

login_url = 'https://bluecloud.xyz/auth/login'

def sendRequest(form):
    session = requests.Session()
    response = session.post(login_url, data=form)
    tree = html.fromstring(response.content)
    segment = tree.xpath('//*[@id="home"]/div[3]/div[3]')
    if len(segment) > 0:
        segment = segment[0]
        service_name = segment.xpath('//h4/text()')
        service_usage = segment.xpath('//div[@class="label"]/text()')
        myService = tree.xpath(u'//h2[text()="我的服务"]')[0].getparent()
        periods = myService.xpath('p/text()')
    else:
        print "Error!"
        print "Maybe wrong username or password."
        return
    for name, usage, period in zip(service_name, service_usage, periods):
        print name
        print usage
        print period.replace('&nbsp', '')
        print '--------------------------\n'

def main():
    form = getConfig()
    sendRequest(form)

if __name__ == '__main__':
    main()
