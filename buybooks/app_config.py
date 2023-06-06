from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER


class BaseConfig():
    SECRET_KEY = 'eenwachtwoorddatnietteradenvalt'
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
        DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)

    DEBUG = False
    
    FORMAT_DATE_TIME = '%d/%m/%Y %H:%M'
    UPLOAD_FOLDER = 'static'
    ALLOWED_IMAGE_EXTENSIONS = ["PNG", "JPG", "JPEG"]
    MAX_CONTENT_LENGTH = 1024*1024*1024

    
class TestConfig(BaseConfig):
    pass
    
class DevConfig(BaseConfig):
    DEBUG = True


class ServerConfig(BaseConfig):
    DEBUG = False
    