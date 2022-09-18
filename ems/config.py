from pathlib import Path
DEBUG = True
ROOT = Path.home()
DOMAIN_ROOT = 'public_html'

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES_SQLITE3 = {
'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
    }
}


DATABASES_MYSQL = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'ems',
    'USER': 'root',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': '3306',
    'OPTIONS':{
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}