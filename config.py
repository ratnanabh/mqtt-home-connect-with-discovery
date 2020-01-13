import os
project_dir = os.path.dirname(os.path.abspath(__file__))


class Config(object):
    DEBUG = True
    # SERVER_NAME = '0.0.0.0:80'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(project_dir, 'homeConnect.db'))
