import os

db_type = os.getenv('DB_TYPE', 'mysql')

if db_type == 'postgresql':
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/{db-name}'.format(**{
        'user': os.getenv('USERNAME'),
        'password': os.getenv('PASSWORD'),
        'host': os.getenv('HOST'),
        'db-name': os.getenv('DB_NAME'),
    })
else:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db-name}?charset=utf8'.format(**{
        'user': os.getenv('USERNAME'),
        'password': os.getenv('PASSWORD'),
        'host': os.getenv('HOST'),
        'db-name': os.getenv('DB_NAME'),
    })
