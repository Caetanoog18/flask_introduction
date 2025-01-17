from flask import Flask
'''
It creates an instance of the Flask class, which will be our WSGI ( Web Server Gateway Interface) application
'''
# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Test Flask"

@app.route("/index")
def index():
    return "Test Index Page"

if __name__ == '__main__':
    app.run(debug=True)