import os

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db-name}?charset=utf8'.format(**{
    'user': os.getenv('USERNAME'),
    'password': os.getenv('PASSWORD'),
    'host': os.getenv('HOST'),
    'db-name': os.getenv('DB_NAME'),
    })