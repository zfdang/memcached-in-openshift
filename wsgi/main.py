from flask import Flask
import index
import pi

app = Flask(__name__)
app.config.from_object('settings.DevelopmentConfig')

# init memcache client, use python-memcache
import memcache
app.config['cache'] = memcache.Client(app.config['MEMCACHED_SERVERS'], debug=0)


app.register_blueprint(index.bp, url_prefix='/')
app.register_blueprint(pi.bp, url_prefix='/pi')


if __name__ == "__main__":
    print app.url_map
    app.run()
