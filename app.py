from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/name')
def display_name():
    return 'Hello, Kyle!'

@app.route('/school')
def display_school():
    return "I'm studying in PUPT"

if __name__ == '__main__':
    app.run()