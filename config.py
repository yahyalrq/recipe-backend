from dotenv import load_dotenv
import os

load_dotenv()


class Config(object):
    SECRET_KEY = 'this needs to be'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
        dbuser=os.getenv('DBUSER')+"@jseijas-dbsrv",
        dbpass=os.getenv('DBPASS'),
        dbhost=os.getenv('DBHOST') + ".postgres.database.azure.com",
        dbname='ylaraqui-assignment-prod-db'
    )

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
        dbuser=os.getenv('DBUSER')+"@jseijas-dbsrv",
        dbpass=os.getenv('DBPASS'),
        dbhost=os.getenv('DBHOST')+".postgres.database.azure.com",
        dbname='ylaraqui-assignment-dev-db'
    )


class GithubCIConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlitefile.db'
    DEBUG = True
