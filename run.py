from app.endpoints import app
from config import *


if __name__=="__main__":
    app.run(port=8080,debug=True)