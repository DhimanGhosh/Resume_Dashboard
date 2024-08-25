from app import app
from flask_frozen import Freezer

if __name__ == '__main__':
    freezer = Freezer(app)
    freezer.freeze()
