class Config(object):
    """Base config class."""
    SECRET_KEY = 'b0cb3e2d2b7f55292b089fdc7dfc62d8'

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/myblog'
