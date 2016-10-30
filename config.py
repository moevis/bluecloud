import ConfigParser
import os
import getpass
import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

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
    username = raw_input('Username: ')
    password = getpass.getpass()
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