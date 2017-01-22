from flask import Flask
from config import DevConfig
import wt_forms

app = Flask(__name__)


views = __import__('views')

app.config.from_object(DevConfig)

if __name__ == '__main__':

    app.run()