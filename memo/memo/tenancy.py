import os
from django.db import connections
from django.conf import settings

def dbname(dbnum):
    return "tenancy{}".format(str(dbnum))

def ensure_connect(dbnum):
    # 接続設定がされていなかったら動的に追加
    if not dbname(dbnum) in connections.databases:
        connections.databases[dbname(dbnum)] = {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(settings.BASE_DIR, 'db.tenancy{}'.format(str(dbnum))),
        }
