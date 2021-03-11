#Modules
from flask import Flask

#Initializations
app = Flask(__name__)

#Run server
if __name__ == '__main__':
    app.run(port = 3000, debug = True)