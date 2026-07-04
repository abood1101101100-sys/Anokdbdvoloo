import redis
r = redis.Redis('localhost',decode_responses=True)

token = "8662212748:AAH8s9BaxeEWh9cXNCpkoReXnsu-H9bAXWU"
Dev_Zaid = token.split(':')[0]
sudo_id = 7273666832
botUsername = "Uvvbbbot"

from kvsqlite.sync import Client as DB
ytdb = DB('ytdb.sqlite')
sounddb = DB('sounddb.sqlite')
wsdb = DB('wsdb.sqlite')