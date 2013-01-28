# Flask configuration files
# https://flask.readthedocs.org/en/0.6.1/config/
import os


class Config(object):
    # memcached server URL
    MEMCACHED_SERVERS = []
    if 'OPENSHIFT_APP_UUID' in os.environ:
        MEMCACHED_SERVERS.append('%s:22322' % (os.environ['OPENSHIFT_INTERNAL_I']))
    else:
        MEMCACHED_SERVERS.append('192.168.0.204:22322')


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
