import ConfigParser
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