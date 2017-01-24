class Config(object):
    """Base config class."""
    SECRET_KEY = 'b0cb3e2d2b7f55292b089fdc7dfc62d8'
    # reCAPTCHA Public key and Private key
    # RECAPTCHA_PUBLIC_KEY = "6Lce9BIUAAAAAM4pVhshhH62gPozN4LtFbD5EFWa"
    # RECAPTCHA_PRIVATE_KEY = "6Lce9BIUAAAAAFcXfFbYx05fgDWrWU2f2endrf5-"

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/myblog'
