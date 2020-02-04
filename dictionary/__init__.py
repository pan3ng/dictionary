from flask import Flask

app = Flask(__name__)

from dictionary import routes
