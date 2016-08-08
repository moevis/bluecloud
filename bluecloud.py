# -*- coding: utf-8 -*-
import ConfigParser
import requests
from lxml import html

def getConfig():
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    identity = config.get('account', 'username')
    password = config.get('account', 'password')

    form = {
        'identity': identity,
        'password': password
    }
    return form

def sendRequest(url, form):
    session = requests.Session()
    response = session.post(url, data=form)
    tree = html.fromstring(response.content)
    segment = tree.xpath('//*[@id="home"]/div[3]/div[3]')[0]
    service_name = segment.xpath('//h4/text()')
    service_usage = segment.xpath('//div[@class="label"]/text()')

    for name, usage in zip(service_name, service_usage):
        print name
        print usage
        print '--------------------------'

def main():
    form = getConfig()
    sendRequest('https://bluecloud.xyz/auth/login', form)

if __name__ == '__main__':
    main()
