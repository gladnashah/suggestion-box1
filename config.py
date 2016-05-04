import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# from flask.ext.sqlalchemy import SQLAlchemy
# import os

# basedir = os.path.abspath(os.path.dirname(__file__))


# app.config['SQLALCHEMY_DATABASE_URI'] =\
# 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# db = SQLAlchemy(app)

# class Config:
#     '''class containing config variables
#     '''

#     SECRET_KEY = '257778gfbnmlllfeetui'
#     SQLALCHEMY_DATABASE_URI = \
#         'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#     SQLALCHEMY_COMMIT_ON_TEARDOWN = True
#     MAIL_SERVER = 'smtp.googlemail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
#     MAIL_PASSWORD = os.environ.get ('MAIL_PASSWORD')
#     MAIL_SENDER = 'Admin <name@example.com>'


#     @staticmethod
#     def init_app(app):
#         pass


# config = {
#     'default': Config
# }