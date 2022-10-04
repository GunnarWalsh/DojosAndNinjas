from flask import Flask
app = Flask(__name__)
# ADDED: secret key for session (and other things soon!)
app.secret_key = "grootgroot"