from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pizzastore',
        'USER': 'postgres',
        'PASSWORD': 'test',
        # 'HOST': 'localhost',
        # 'PORT': '61470',
     }
}
