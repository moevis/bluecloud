#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser
import requests
from lxml import html
import os

def getConfig():
    config = ConfigParser.ConfigParser()
    if os.path.isfile('config.ini'):
        config.read('config.ini')
        identity = config.get('account', 'username')
        password = config.get('account', 'password')

        form = {
            'identity': identity,
            'password': password
        }
    else:
        form = createConfig()
    return form

def createConfig():
    username = raw_input('username: ')
    password = raw_input('password: ')
    form = {
        'identity': username,
        'password': password
    }
    configFile = open('config.ini', 'w')
    config = ConfigParser.ConfigParser()
    config.add_section('account')
    config.set('account', 'username', username)
    config.set('account', 'password', password)
    config.write(configFile)
    return form

def sendRequest(url, form):
    session = requests.Session()
    response = session.post(url, data=form)
    tree = html.fromstring(response.content)
    segment = tree.xpath('//*[@id="home"]/div[3]/div[3]')
    if len(segment) > 0:
        segment = segment[0]
        service_name = segment.xpath('//h4/text()')
        service_usage = segment.xpath('//div[@class="label"]/text()')
    else:
        print "Error!"
        print "Maybe wrong username or password."
        return
    for name, usage in zip(service_name, service_usage):
        print name
        print usage
        print '--------------------------'

def main():
    form = getConfig()
    sendRequest('https://bluecloud.xyz/auth/login', form)

if __name__ == '__main__':
    main()
